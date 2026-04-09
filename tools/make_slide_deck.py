#!/usr/bin/env python3
"""Create a multipage PDF from three PNG slides.
Usage: python tools/make_slide_deck.py
"""
from pathlib import Path
import sys

try:
    from PIL import Image
except Exception as e:
    print("Pillow not installed. Install with: pip install pillow")
    raise

slides = [
    Path("informes/weekly_summary_2026-04-01_2026-04-07/figures/canonical_family_boxplot.png"),
    Path("informes/weekly_summary_2026-04-01_2026-04-07/figures/it08_fig05_tv_vs_instant_family.png"),
    Path("informes/weekly_summary_2026-04-01_2026-04-07/figures/it11_fig02_rmse_boxplot.png"),
]

existing = [p for p in slides if p.exists()]
if not existing:
    print("No input images found. Checked paths:")
    for p in slides:
        print(" -", p)
    sys.exit(2)

imgs = []
for p in existing:
    im = Image.open(p)
    if im.mode != "RGB":
        im = im.convert("RGB")
    imgs.append(im.copy())

out_pdf = Path("informes/weekly_summary_2026-04-01_2026-04-07/weekly_slides_2026-04-01_2026-04-07.pdf")

try:
    imgs[0].save(out_pdf, "PDF", save_all=True, append_images=imgs[1:])
    print("Wrote:", out_pdf)
except Exception as e:
    print("Failed to write PDF:", e)
    sys.exit(3)
