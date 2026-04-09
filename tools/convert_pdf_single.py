#!/usr/bin/env python3
import sys
from pathlib import Path
import fitz

def convert_pdf(src, dst, width=1200):
    src = Path(src)
    dst = Path(dst)
    if dst.suffix.lower() != '.png':
        dst = dst.with_suffix('.png')
    try:
        doc = fitz.open(src)
        page = doc.load_page(0)
        rect = page.rect
        scale = float(width) / rect.width if rect.width > 0 else 1.0
        mat = fitz.Matrix(scale, scale)
        pix = page.get_pixmap(matrix=mat, alpha=True)
        dst.parent.mkdir(parents=True, exist_ok=True)
        pix.save(str(dst))
        print(f"OK:{src} -> {dst}")
        return 0
    except Exception as e:
        print(f"ERR:{src} -> {dst} : {e}")
        return 2

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: convert_pdf_single.py src.pdf dest.png')
        sys.exit(2)
    rc = convert_pdf(sys.argv[1], sys.argv[2])
    sys.exit(rc)
