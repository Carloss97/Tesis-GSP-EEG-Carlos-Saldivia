#!/usr/bin/env python3
import fitz
from pathlib import Path

sources = [
    "Thesis-Copilot-Toolkit/results/it08_high_missing_synthetic_figures/fig05_tv_vs_instant_family.pdf",
    "Thesis-Copilot-Toolkit/results/it11_physionet_high_missing_figures/fig02_rmse_boxplot.pdf",
    "Thesis-Copilot-Toolkit/results/it05b_synthetic_three_figures/fig02_rmse_boxplot.pdf",
    "Thesis-Copilot-Toolkit/results/it02_figures/fig05_tv_vs_instant_family.pdf",
]

report_pdf_dir = Path("informes/weekly_summary_2026-04-01_2026-04-07/figures")

def convert_pdf(src: Path, dst: Path, width: int = 1200):
    try:
        doc = fitz.open(src)
        page = doc.load_page(0)
        rect = page.rect
        if rect.width == 0:
            raise RuntimeError("page width is zero")
        scale = float(width) / rect.width
        mat = fitz.Matrix(scale, scale)
        pix = page.get_pixmap(matrix=mat, alpha=True)
        dst.parent.mkdir(parents=True, exist_ok=True)
        pix.save(str(dst))
        print(f"Converted {src} -> {dst}")
    except Exception as e:
        print(f"Failed converting {src} -> {dst}: {e}")


def main():
    targets = []
    for s in sources:
        p = Path(s)
        if p.exists():
            out = Path("informes/weekly_summary_2026-04-01_2026-04-07/figures") / (p.stem + ".png")
            targets.append((p, out))
        else:
            print(f"Source not found: {p}")

    if report_pdf_dir.exists():
        for pdf in report_pdf_dir.rglob("*.pdf"):
            out = pdf.with_suffix('.png')
            targets.append((pdf, out))

    # deduplicate
    seen = set()
    final = []
    for a, b in targets:
        key = str(a.resolve())
        if key not in seen:
            seen.add(key)
            final.append((a, b))

    for src, dst in final:
        if dst.exists():
            print(f"Already exists: {dst}")
            continue
        convert_pdf(src, dst)

if __name__ == '__main__':
    main()
