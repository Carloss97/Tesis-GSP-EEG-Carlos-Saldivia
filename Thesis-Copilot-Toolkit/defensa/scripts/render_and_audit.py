#!/usr/bin/env python3
"""Render PDF pages and emit deterministic visual-QA metadata/contact sheets."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


def render(pdf_path: Path, out_dir: Path, dpi: int) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("page-*.png"):
        old.unlink()
    doc = fitz.open(pdf_path)
    pages = []
    scale = dpi / 72
    matrix = fitz.Matrix(scale, scale)
    for idx, page in enumerate(doc, 1):
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        dest = out_dir / f"page-{idx:02d}.png"
        pix.save(dest)
        text = page.get_text("text").strip()
        pages.append(
            {
                "page": idx,
                "width_pt": round(page.rect.width, 2),
                "height_pt": round(page.rect.height, 2),
                "text_chars": len(text),
                "image": dest.name,
            }
        )
    return {"pdf": str(pdf_path), "pages": len(doc), "dpi": dpi, "page_data": pages}


def contact_sheet(out_dir: Path, columns: int, thumb_width: int) -> Path:
    paths = sorted(out_dir.glob("page-*.png"))
    if not paths:
        raise RuntimeError(f"No rendered pages in {out_dir}")
    with Image.open(paths[0]) as first:
        ratio = first.height / first.width
    thumb_height = int(thumb_width * ratio)
    caption = 28
    rows = (len(paths) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * thumb_width, rows * (thumb_height + caption)), "#d9dde1")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for i, path in enumerate(paths):
        with Image.open(path) as image:
            image = image.convert("RGB")
            image.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            x = (i % columns) * thumb_width
            y = (i // columns) * (thumb_height + caption)
            sheet.paste(image, (x, y))
            draw.text((x + 8, y + thumb_height + 6), f"Página {i + 1}", fill="black", font=font)
    dest = out_dir / "contact-sheet.png"
    sheet.save(dest, quality=92)
    return dest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument("--dpi", type=int, default=150)
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--thumb-width", type=int, default=420)
    args = parser.parse_args()
    metadata = render(args.pdf, args.out, args.dpi)
    metadata["contact_sheet"] = str(contact_sheet(args.out, args.columns, args.thumb_width))
    report = args.out / "render-report.json"
    report.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"pdf": str(args.pdf), "pages": metadata["pages"], "contact_sheet": metadata["contact_sheet"]}))


if __name__ == "__main__":
    main()
