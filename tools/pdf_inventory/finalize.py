#!/usr/bin/env python3
"""Build reviewed inventories from raw extraction and explicit visual review."""
import argparse,csv,json,re,subprocess,unicodedata
from collections import defaultdict
from pathlib import Path

def norm(s):
 return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',s).strip()).casefold()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--directory',type=Path,required=True);ap.add_argument('--repo',type=Path,default=Path('.'));ap.add_argument('--baseline-ref',default='origin/main');a=ap.parse_args();p=a.directory
 raw=json.loads((p/'extraction_raw.json').read_text());review=json.loads((p/'review.json').read_text());assert raw['source_sha256']==review['source_sha256']
 rows=raw['rows']+review.get('added_fragments',[]); ids={x['row_id'] for x in rows};assert len(ids)==len(rows)
 for r in rows:
  rid=r['row_id']; candidate=review['corrections'].get(rid,r.get('display_name') or r['ocr_raw']);unc=review['unconfirmed'].get(rid)
  r['candidate_text']=candidate if unc else '';r['display_name']=None if unc else candidate;r['status']='要確認' if unc else '画像照合済み';r['review_note']=unc or review.get('notes',{}).get(rid,'');r['continuation_of']=review.get('continuations',{}).get(rid,'')
  assert not r['continuation_of'] or r['continuation_of'] in ids
 cols={(x['page'],x['column']):x for x in review['columns']};assert len(cols)==raw['page_count']*2
 for key,col in cols.items():
  found=sum((r['page'],r['column'])==key for r in rows);assert found==col['visual_display_rows'],(key,found,col['visual_display_rows']);assert col['reviewed']
 assert review['boundaries_reviewed']==list(range(1,raw['page_count']))
 b002=json.loads((a.repo/'inventory/B002_2026-11-13.json').read_text());old=set()
 for s in b002['categoryScreenshots']:
  for side in ('left','right'):old.update(norm(x) for x in s.get(side,[]))
 tracker=(a.repo/'SCREENSHOT_TRACKER.md').read_text();section=tracker.split('## 第1セット：人気')[1].split('### 名前の照合')[0]
 b001=set()
 for line in section.splitlines():
  m=re.match(r'\|\s*\d+\s*\|\s*([^|]+)',line)
  if m:b001.add(norm(m.group(1)))
 text=subprocess.check_output(['git','show',a.baseline_ref+':index.html'],cwd=a.repo,text=True);m=re.search(r'const catalog\s*=\s*',text);catalog=json.JSONDecoder().raw_decode(text[m.end():])[0];baseline={norm(x['name']) for x in catalog}
 slots=[r for r in rows if not r['continuation_of']];groups=defaultdict(list)
 for r in slots:
  if r['display_name']:groups[norm(r['display_name'])].append(r)
 apps=[]
 for key,items in sorted(groups.items()):
  names=sorted({x['display_name'] for x in items});apps.append({'display_name':names[0],'observed_variants':names,'occurrences':[x['row_id'] for x in items], 'matches_B001':key in b001,'matches_B002':key in old,'matches_main_catalog_name':key in baseline})
 payload={'source_pdf_sha256':raw['source_sha256'],'rows':rows,'apps':apps,'counts':{'page_column_observations':len(rows),'boundary_continuations':len(rows)-len(slots),'display_slots':len(slots),'unconfirmed_slots':sum(r['status']=='要確認' for r in slots),'confirmed_normalized_names':len(apps),'name_matches_B001_B002':sum(x['matches_B001'] or x['matches_B002'] for x in apps),'name_matches_main':sum(x['matches_main_catalog_name'] for x in apps)}}
 (p/'inventory.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
 def out(name,data,fields):
  with (p/name).open('w',encoding='utf-8-sig',newline='') as f:
   w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
 fields=['row_id','page','column','row','display_name','candidate_text','status','review_note','ocr_raw','continuation_of','evidence'];out('rows.csv',rows,fields);out('unconfirmed.csv',[r for r in slots if r['status']=='要確認'],fields)
 out('apps.csv',[dict(x,observed_variants=' | '.join(x['observed_variants']),occurrences=' | '.join(x['occurrences'])) for x in apps],['display_name','observed_variants','occurrences','matches_B001','matches_B002','matches_main_catalog_name'])
 report=['# B003 検証レポート','','15ページ・30列のタイトル画像および全14ページ境界を目視照合。PDF SHA-256: `'+raw['source_sha256']+'`。','',f"ページ列別の名前断片 {len(rows)}、境界にまたがる重複断片 {len(rows)-len(slots)}、掲載枠 {len(slots)}。判読保留 {payload['counts']['unconfirmed_slots']} 枠。確定表示名の正規化後 {len(apps)} 種。",f"確定表示名のうち B001/B002 名称一致 {payload['counts']['name_matches_B001_B002']} 種、main カタログ名称一致 {payload['counts']['name_matches_main']} 種。名称の不一致は新規アプリの確定を意味しない。",'','正規化は NFKC・前後および連続空白・大文字小文字のみ。同名であっても同一アプリとは限らない。未確認候補は集計から除外。OCR結果は原文として保持し、未確認名を補完しない。機能や公式IDは検証対象外。','','| ページ | 列 | 表示された名前断片 | 抽出行 | 要確認 |','|---:|:---:|---:|---:|---:|']
 for key,col in sorted(cols.items()):
  subset=[r for r in rows if (r['page'],r['column'])==key];report.append(f"| {key[0]} | {key[1]} | {col['visual_display_rows']} | {len(subset)} | {sum(r['status']=='要確認' for r in subset)} |")
 report += ['', '9ページ右47行は10ページ右1行の微小断片。13ページ左右47行は14ページ左右1行に連続し、各組は1掲載枠として数える。該当箇所は review.json の continuation_of に記録。', '抽出画像は evidence/ に保存。ページ列行番号は各ページ上からの順序。元画像の境界・クロップによる微細な字形、記号、UI上の省略は unconfirmed.csv を参照。', '既存の B003 OCR草稿・部分目視記録は参照資料として保持。B001 はトラッカーの画面表示名、B002 は原本JSON、main は指定refの index.html と名前のみ照合。']
 (p/'verification.md').write_text('\n'.join(report)+'\n');print(json.dumps(payload['counts'],ensure_ascii=False))
if __name__=='__main__':main()
