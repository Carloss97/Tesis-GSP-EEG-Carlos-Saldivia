#!/usr/bin/env python3
"""Create legible qualitative figure derivatives from existing raster result images.

The original time-series figure contains six vertically stacked methods and is too
dense for the thesis body. This script crops the most informative panels
(TRSS, MNE, and the challenging spline baseline) and enlarges them without
altering the plotted data. The PSD figure is also cropped to remove an overly
long title and given a concise Spanish header.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"

font_big = ImageFont.load_default(size=36)
font_med = ImageFont.load_default(size=26)


def add_header(img: Image.Image, title: str, subtitle: str = "") -> Image.Image:
    pad = 70 if subtitle else 48
    out = Image.new("RGB", (img.width, img.height + pad), "white")
    out.paste(img, (0, pad))
    d = ImageDraw.Draw(out)
    d.text((22, 12), title, fill=(0, 0, 0), font=font_big)
    if subtitle:
        d.text((22, 45), subtitle, fill=(80, 80, 80), font=font_med)
    return out


def clean_timeseries():
    src = FIG / "res_opt_final__erp_timeseries_mne_sample_nearby_0.4.png"
    img = Image.open(src).convert("RGB")
    w, h = img.size
    # Manual crops based on the source layout: title + six equal vertical panels.
    top = 170
    panel_h = 285
    gap = 22
    # Keep full horizontal plot area and crop selected method panels.
    panels = [
        ("TRSS (GSP)", 0),
        ("MNE interpolate_bads", 4),
    ]
    crops = []
    for label, idx in panels:
        y0 = top + idx * (panel_h + gap)
        y1 = min(y0 + panel_h, h)
        crop = img.crop((60, max(0, y0-10), w-25, min(h, y1+12)))
        # Add a clear method label outside the data region.
        label_band = Image.new("RGB", (crop.width, 42), "white")
        d = ImageDraw.Draw(label_band)
        d.text((10, 8), label, fill=(0,0,0), font=font_med)
        combined = Image.new("RGB", (crop.width, crop.height + label_band.height), "white")
        combined.paste(label_band, (0,0))
        combined.paste(crop, (0,label_band.height))
        crops.append(combined)
    width = max(c.width for c in crops)
    total_h = sum(c.height for c in crops) + 18 * (len(crops)-1)
    body = Image.new("RGB", (width, total_h), "white")
    y = 0
    for c in crops:
        body.paste(c, ((width-c.width)//2, y))
        y += c.height + 18
    body = add_header(body, "Reconstrucción temporal: comparación cualitativa", "MNE Sample, pérdida cercana 40%; comparación ampliada de dos métodos principales")
    # Downscale slightly to keep file size reasonable while preserving legibility.
    max_w = 1700
    if body.width > max_w:
        scale = max_w / body.width
        body = body.resize((max_w, int(body.height*scale)), Image.Resampling.LANCZOS)
    body.save(FIG / "res_opt_final__erp_timeseries_mne_sample_nearby_0.4_clean.png", dpi=(220,220))


def clean_psd():
    src = FIG / "res_opt_final__best_psd_comparison.png"
    img = Image.open(src).convert("RGB")
    # Preserve the original plot (it carries the actual PSD rendering), but add
    # explicit white margins so title, legend and tick labels never appear cut
    # in the thesis PDF or in contact-sheet QA. Avoid adding new accented text
    # with PIL's default bitmap font, which can render UTF-8 characters poorly.
    margin_l, margin_r, margin_t, margin_b = 42, 52, 38, 44
    out = Image.new("RGB", (img.width + margin_l + margin_r, img.height + margin_t + margin_b), "white")
    out.paste(img, (margin_l, margin_t))
    out.save(FIG / "res_opt_final__best_psd_comparison_clean.png", dpi=(220,220))


if __name__ == "__main__":
    clean_timeseries()
    clean_psd()
    print("saved cleaned qualitative PNG figures")
