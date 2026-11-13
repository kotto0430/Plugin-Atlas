# PDF画像からの名前収集

`pip install -r tools/pdf_inventory/requirements.txt` と Tesseract OCR (`eng`) が必要。

```
python tools/pdf_inventory/extract.py input.pdf --config tools/pdf_inventory/b003-layout.json --work /tmp/pdf-work --output inventory/example
```

原画像または465dpi画像、左右タイトル領域、番号付き画像、OCR原文と未確認状態を出力する。設定は入力固有であり、画像幅・各列のタイトル範囲・輝度しきい値・先頭除外範囲をPDFごとに調整する。列の配置や文字色が異なるPDFでは自動適用できない。OCR結果だけでは網羅性・正確性は保証されない。ページ境界と検出漏れは元画像を手動確認する。

B003の目視修正をまとめるには、作業ブランチで次を実行する。`--baseline-ref` は照合時点の main コミットを指定する。

```
python tools/pdf_inventory/finalize.py --directory inventory/B003_verified --baseline-ref <main-commit>
```

この集計はB003固有の review.json と B001/B002 記録を使用する。ページ別行数、連結参照、元PDFハッシュを検査してから出力する。確認できない名前は candidate_text に残し、display_name は空にする。review.json の変更には画像照合が必要。
