#!/usr/bin/env python3
"""Generate an expanded 6-slide PDF for the weekly meeting.
Slides order:
 - Title
 - Agenda
 - canonical_family_boxplot
 - it08_fig05_tv_vs_instant_family
 - it11_fig02_rmse_boxplot
 - Conclusions / Next steps

Usage: python tools/make_expanded_deck.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sys

BASE = Path("informes/weekly_summary_2026-04-01_2026-04-07")
FIG_DIR = BASE / "figures"
OUT_PDF = BASE / "weekly_slides_expanded_2026-04-01_2026-04-07.pdf"
SLIDE_SIZE = (1200, 720)
BG_COLOR = (255, 255, 255)
CAPTION_COLOR = (60, 60, 60)
TITLE_COLOR = (20, 20, 60)

slides = []

# helper fonts
try:
    title_font = ImageFont.truetype("arial.ttf", 56)
    subtitle_font = ImageFont.truetype("arial.ttf", 28)
    body_font = ImageFont.truetype("arial.ttf", 22)
    caption_font = ImageFont.truetype("arial.ttf", 18)
except Exception:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    body_font = ImageFont.load_default()
    caption_font = ImageFont.load_default()

# Title slide
im = Image.new("RGB", SLIDE_SIZE, BG_COLOR)
d = ImageDraw.Draw(im)
d.text((60, 80), "Weekly Summary: 2026-04-01 → 2026-04-07", fill=TITLE_COLOR, font=title_font)
d.text((60, 160), "Author: Carlos Saldivia", fill=CAPTION_COLOR, font=subtitle_font)
d.text((60, 200), "Prepared for 30-minute meeting — Key findings and next steps", fill=CAPTION_COLOR, font=body_font)
slides.append(im)

# Agenda slide
im = Image.new("RGB", SLIDE_SIZE, BG_COLOR)
d = ImageDraw.Draw(im)
d.text((60, 80), "Agenda (30')", fill=TITLE_COLOR, font=title_font)
ag = ["0–5': Objetivo y hallazgo principal",
      "5–15': Walkthrough de slides (sintéticos + real)",
      "15–25': Preguntas clave y decisión (replicar it11 vs reruns)",
      "25–30': Próximos pasos y asignaciones"]
for i, line in enumerate(ag):
    d.text((80, 180 + i * 50), f"• {line}", fill=CAPTION_COLOR, font=body_font)
slides.append(im)

# Content images
sources = [
    (FIG_DIR / "canonical_family_boxplot.png", "Canonical family boxplot: resumen por familia"),
    (FIG_DIR / "it08_fig05_tv_vs_instant_family.png", "it08 fig05 — sintético alto MR"),
    (FIG_DIR / "it11_fig02_rmse_boxplot.png", "it11 fig02 — physionet (mr=40%)"),
]

for src, caption in sources:
    if not src.exists():
        # create placeholder slide indicating missing image
        im = Image.new("RGB", SLIDE_SIZE, BG_COLOR)
        d = ImageDraw.Draw(im)
        d.text((60, 120), "[Imagen faltante]", fill=(200,0,0), font=title_font)
        d.text((60, 200), str(src), fill=CAPTION_COLOR, font=body_font)
        slides.append(im)
        continue
    img = Image.open(src).convert("RGB")
    # fit into SLIDE_SIZE with margin
    w, h = img.size
    max_w = SLIDE_SIZE[0] - 120
    max_h = SLIDE_SIZE[1] - 160
    ratio = min(max_w / w, max_h / h, 1.0)
    new_size = (int(w * ratio), int(h * ratio))
    img = img.resize(new_size, Image.LANCZOS)
    im = Image.new("RGB", SLIDE_SIZE, BG_COLOR)
    # paste centered
    x = (SLIDE_SIZE[0] - new_size[0]) // 2
    y = 60
    im.paste(img, (x, y))
    d = ImageDraw.Draw(im)
    # caption
    d.text((80, SLIDE_SIZE[1] - 60), caption, fill=CAPTION_COLOR, font=caption_font)
    slides.append(im)

# Conclusions slide
im = Image.new("RGB", SLIDE_SIZE, BG_COLOR)
d = ImageDraw.Draw(im)
d.text((60, 80), "Conclusions & Next Steps", fill=TITLE_COLOR, font=title_font)
concls = [
    "- TV/Time: alto rendimiento en sintéticos (RMSE gains 16–28%)",
    "- Reales: efecto localizado (it11); replicar con más seeds",
    "- Prioridad: integrar DTW (MET-01) → ejecutar MET-02 extendido",
]
for i, line in enumerate(concls):
    d.text((80, 200 + i * 50), line, fill=CAPTION_COLOR, font=body_font)
slides.append(im)

# save to PDF
if not slides:
    print("No slides generated.")
    sys.exit(1)

slides[0].save(OUT_PDF, "PDF", save_all=True, append_images=slides[1:])
print("Wrote:", OUT_PDF)
