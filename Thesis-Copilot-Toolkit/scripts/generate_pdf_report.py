#!/usr/bin/env python3
"""Generate a multipage PDF report with summaries, tables and figures.

Writes: results/analysis/batches/report_summary.pdf

Usage: python scripts/generate_pdf_report.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import textwrap
import datetime
import sys


def add_text_pages(pdf, title, text, lines_per_page=40, width=100, fontsize=10):
    lines = []
    for para in text.splitlines():
        if not para.strip():
            lines.append("")
            continue
        wrapped = textwrap.wrap(para, width=width)
        if not wrapped:
            lines.append("")
        else:
            lines.extend(wrapped)

    for i in range(0, len(lines), lines_per_page):
        chunk = lines[i : i + lines_per_page]
        fig = plt.figure(figsize=(8.27, 11.69))
        ax = fig.add_subplot(111)
        ax.axis("off")
        ax.text(0.5, 0.97, title, ha="center", fontsize=16, weight="bold")
        y = 0.92
        for line in chunk:
            ax.text(0.02, y, line, ha="left", va="top", fontsize=fontsize, family="monospace")
            y -= 0.02
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)


def add_table_pages(pdf, title, df, rows_per_page=28):
    # chunk dataframe into pages
    total_rows = len(df)
    if total_rows == 0:
        return
    for start in range(0, total_rows, rows_per_page):
        sub = df.iloc[start : start + rows_per_page]
        fig = plt.figure(figsize=(8.27, 11.69))
        ax = fig.add_subplot(111)
        ax.axis("off")
        ax.text(0.5, 0.97, title, ha="center", fontsize=14, weight="bold")
        table = ax.table(
            cellText=sub.values,
            colLabels=sub.columns,
            loc="center",
            cellLoc="left",
        )
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 1.2)
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)


def add_image_page(pdf, img_path, caption=None):
    try:
        img = plt.imread(img_path)
    except Exception:
        return
    fig = plt.figure(figsize=(8.27, 11.69))
    ax = fig.add_subplot(111)
    ax.axis("off")
    ax.imshow(img)
    if caption:
        ax.text(0.5, 0.02, caption, ha="center", va="bottom", fontsize=10, color="black", bbox=dict(facecolor="white", alpha=0.7, pad=3))
    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def main():
    ROOT = Path(__file__).resolve().parents[1]
    batches = ROOT / "results" / "analysis" / "batches"
    out_pdf = batches / "report_summary.pdf"
    figures_dir = batches / "figures"

    # gather short numeric summary (falls back to stats CSV)
    stats_csv = batches / "best_method_by_combo_stats.csv"
    try:
        stats = pd.read_csv(stats_csv)
    except Exception:
        stats = pd.DataFrame()

    sig_csv = batches / "significant_combinations.csv"
    try:
        sig = pd.read_csv(sig_csv)
    except Exception:
        sig = pd.DataFrame()

    summary = {}
    summary["generated_on"] = datetime.datetime.now().isoformat()
    summary["total_combos"] = int(len(stats)) if not stats.empty else None
    summary["significant_combos"] = int(len(sig)) if not sig.empty else None
    if not stats.empty and "best_method" in stats.columns:
        summary["best_method_top10"] = stats["best_method"].value_counts().head(10).to_dict()

    # Read textual summaries if available
    global_md = batches / "global_summary.md"
    global_text = ""
    if global_md.exists():
        global_text = global_md.read_text(encoding="utf-8")

    readable_txt = batches / "readable_best_summary.txt"
    readable_text = readable_txt.read_text(encoding="utf-8") if readable_txt.exists() else ""

    # Prepare tables
    top_counts_csv = batches / "top_method_counts.csv"
    if top_counts_csv.exists():
        top_counts = pd.read_csv(top_counts_csv)
    else:
        top_counts = pd.DataFrame()

    top20_csv = batches / "top20_delta_combos.csv"
    if top20_csv.exists():
        top20 = pd.read_csv(top20_csv)
    else:
        top20 = pd.DataFrame()

    best_sorted_csv = batches / "best_by_combo_sorted.csv"
    if best_sorted_csv.exists():
        best_sorted = pd.read_csv(best_sorted_csv)
    else:
        best_sorted = pd.DataFrame()

    # build PDF
    with PdfPages(out_pdf) as pdf:
        # Title page
        fig = plt.figure(figsize=(8.27, 11.69))
        ax = fig.add_subplot(111)
        ax.axis("off")
        ax.text(0.5, 0.8, "Análisis de resultados — B1–B4, it1–it130", ha="center", fontsize=20, weight="bold")
        ax.text(0.5, 0.72, f"Generado: {summary.get('generated_on')}", ha="center", fontsize=10)
        if summary.get("total_combos") is not None:
            ax.text(0.5, 0.68, f"Combinaciones totales: {summary['total_combos']}", ha="center", fontsize=11)
        if summary.get("significant_combos") is not None:
            ax.text(0.5, 0.65, f"Combinaciones significativas: {summary['significant_combos']}", ha="center", fontsize=11)
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)

        # global summary markdown
        if global_text:
            add_text_pages(pdf, "Resumen global", global_text)

        # readable best summary
        if readable_text:
            add_text_pages(pdf, "Resumen legible: mejores métodos", readable_text)

        # top method counts table
        if not top_counts.empty:
            # ensure small width
            add_table_pages(pdf, "Top method counts", top_counts)

        # top20 delta combos
        if not top20.empty:
            add_table_pages(pdf, "Top20 combos por delta", top20)

        # best_by_combo top rows
        if not best_sorted.empty:
            add_table_pages(pdf, "Mejores combinaciones (ordenadas) — primeras filas", best_sorted.head(200), rows_per_page=30)

        # include figures (all PNGs in figures_dir)
        if figures_dir.exists():
            imgs = sorted(figures_dir.glob("*.png"))
            for p in imgs:
                add_image_page(pdf, p, caption=p.name)

        # final page: file index
        files_index = []
        for p in sorted(batches.glob("**/*")):
            if p.is_file():
                rel = p.relative_to(ROOT)
                files_index.append(str(rel))

        add_text_pages(pdf, "Archivos incluidos (índice)", "\n".join(files_index), lines_per_page=80, width=110, fontsize=8)

    print(f"Wrote PDF: {out_pdf}")


if __name__ == "__main__":
    main()
