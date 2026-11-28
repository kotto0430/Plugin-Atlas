#!/usr/bin/env python3
"""Evidence-first image PDF title extraction. Never promotes OCR to verified names."""
import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import fitz
import numpy as np
from PIL import Image, ImageDraw, ImageOps


def bands(mask, gap=3):
    indices = np.flatnonzero(mask)
    return [g for g in np.split(indices, np.flatnonzero(np.diff(indices) > gap) + 1) if len(g) > 3]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('pdf', type=Path)
    ap.add_argument('--config', required=True, type=Path)
    ap.add_argument('--work', required=True, type=Path)
    ap.add_argument('--output', required=True, type=Path)
    args = ap.parse_args()
    cfg = json.loads(args.config.read_text())
    args.work.mkdir(parents=True, exist_ok=True)
    args.output.mkdir(parents=True, exist_ok=True)
    evidence = args.output / 'evidence'
    evidence.mkdir(exist_ok=True)
    doc = fitz.open(args.pdf)
    rows, pages, jobs = [], [], []
    for page_no, page in enumerate(doc, 1):
        images = page.get_image_info(xrefs=True)
        # Only directly extract an image when it is the sole painted image.
        if len(images) == 1 and images[0]['xref']:
            info = images[0]
            data = doc.extract_image(info['xref'])
            im = Image.open(io.BytesIO(data['image'])).convert('RGB')
            mode = 'embedded-original'
            bbox = info['bbox']
            dpi = [im.width / (bbox[2]-bbox[0])*72, im.height/(bbox[3]-bbox[1])*72]
        else:
            pix = page.get_pixmap(dpi=cfg.get('render_dpi', 465))
            im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
            mode, dpi = 'rendered', [cfg.get('render_dpi', 465)] * 2
        im.save(args.work / f'page-{page_no:02}.png')
        if im.width != cfg['reference_width']:
            raise ValueError(f'Page {page_no}: width {im.width} differs from configured geometry')
        a = np.array(im)
        pr = {'page': page_no, 'width': im.width, 'height': im.height, 'mode': mode, 'dpi': dpi, 'columns': []}
        page_rows = []
        for col in cfg['columns']:
            x0, x1 = col['title_x']
            signal = (a[:, x0:x1, :3].min(axis=2) > cfg['brightness_threshold']).sum(axis=1)
            groups = bands(signal > cfg['minimum_bright_pixels'])
            groups = [g for g in groups if g[0] >= cfg.get('start_y_by_page', {}).get(str(page_no), 0)]
            cr = []
            for n, g in enumerate(groups, 1):
                y0, y1 = max(0, int(g[0])-6), min(im.height, int(g[-1])+7)
                rid = f'p{page_no:02}{col["id"]}{n:02}'
                crop = ImageOps.invert(im.crop((x0, y0, x1, y1)).convert('L'))
                crop = ImageOps.expand(crop, border=12, fill='white').resize(((x1-x0+24)*2, (y1-y0+24)*2))
                target = args.work / f'{rid}.png'
                crop.save(target)
                row = {'row_id': rid, 'page': page_no, 'column': col['id'], 'row': n,
                       'bbox_native': [x0, y0, x1, y1], 'ocr_raw': '', 'display_name': None,
                       'status': '要確認', 'review_note': 'OCR候補。画像照合前',
                       'evidence': f'evidence/page-{page_no:02}.png'}
                rows.append(row); cr.append(row); jobs.append((row, target))
            pr['columns'].append({'column': col['id'], 'detected_title_bands': len(cr),
                                  'visual_display_rows': None, 'visually_reviewed': False})
            page_rows.append(cr)
        # Enlarged title strips retain original pixels and visible symbols; numbers are annotations.
        sheet = Image.new('RGB', (1360, 48 + max(map(len, page_rows), default=0)*42), 'white')
        draw = ImageDraw.Draw(sheet)
        for ci, cr in enumerate(page_rows):
            draw.text((ci*680+6, 10), f'PDF page {page_no} / {cfg["columns"][ci]["id"]} / native title pixels', fill='black')
            for row in cr:
                x0,y0,x1,y1 = row['bbox_native']
                strip=im.crop((x0,y0,x1,y1))
                yy=48+(row['row']-1)*42
                draw.text((ci*680+4, yy+9), str(row['row']), fill='black')
                sheet.paste(strip, (ci*680+38, yy))
        sheet.save(evidence / f'page-{page_no:02}.png')
        pages.append(pr)
    def ocr(job):
        row, path = job
        row['ocr_raw'] = subprocess.run(['tesseract', str(path), 'stdout', '-l', cfg.get('ocr_language','eng'), '--psm','7'], capture_output=True, text=True, check=True).stdout.strip()
    with ThreadPoolExecutor(max_workers=cfg.get('workers',4)) as pool:
        list(pool.map(ocr, jobs))
    result = {'schema_version': 1, 'source_pdf': args.pdf.name,
              'source_sha256': hashlib.sha256(args.pdf.read_bytes()).hexdigest(),
              'page_count': len(doc), 'config': cfg, 'pages': pages, 'rows': rows}
    (args.output/'extraction_raw.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'pages':len(pages),'rows':len(rows),'columns':[[c['detected_title_bands'] for c in p['columns']] for p in pages]}))


if __name__ == '__main__':
    main()
