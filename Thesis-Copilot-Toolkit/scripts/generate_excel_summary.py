#!/usr/bin/env python3
"""
Collect summary CSVs and figures into a single Excel workbook with filters.

Output: `results/analysis/batches/summary_report.xlsx`

Writes one sheet per available CSV and a `Figures` sheet embedding PNGs.
"""
from pathlib import Path
import pandas as pd
import argparse
import sys


def read_csv_if_exists(path: Path):
    if path.exists():
        try:
            return pd.read_csv(path)
        except Exception as e:
            print(f"Error reading {path}: {e}", file=sys.stderr)
    return None


def autofilter_and_format(worksheet, df):
    # worksheet is xlsxwriter worksheet; df is pandas DataFrame
    if df is None:
        return
    nrows, ncols = df.shape
    # set autofilter covering header + rows
    try:
        worksheet.autofilter(0, 0, nrows, max(0, ncols - 1))
    except Exception:
        pass
    # set reasonable column widths
    for i, col in enumerate(df.columns):
        try:
            col_vals = df[col].astype(str)
            maxlen = max(col_vals.map(len).max(), len(str(col)))
            width = min(60, maxlen + 2)
            worksheet.set_column(i, i, width)
        except Exception:
            try:
                worksheet.set_column(i, i, max(10, len(str(col)) + 2))
            except Exception:
                pass
    try:
        worksheet.freeze_panes(1, 0)
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(description='Export summary CSVs and figures into an Excel workbook')
    parser.add_argument('--batches-dir', default=None, help='Path to results/analysis/batches')
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    root = script_path.parent.parent
    default_batches = root / 'results' / 'analysis' / 'batches'
    batches_dir = Path(args.batches_dir) if args.batches_dir else default_batches
    if not batches_dir.exists():
        print(f'Batches dir not found: {batches_dir}', file=sys.stderr)
        sys.exit(1)

    out_xlsx = batches_dir / 'summary_report.xlsx'

    # Priority files to include (if present). We'll also append any other CSV summaries
    priority = [
        'best_method_by_combo_stats.csv',
        'best_method_by_combo.csv',
        'best_method_counts.csv',
        'pivot_best_method_by_graph_counts.csv',
        'pivot_method_by_graph_mean_mae.csv',
        'pivot_method_by_dataset_mean_mae.csv',
        'pivot_method_by_missing_ratio_mean_mae.csv',
        'overall_method_ranking.csv',
        'global_by_method.csv',
        'global_by_graph.csv',
        'global_by_dataset.csv',
        'global_by_missing_ratio.csv',
        'global_by_combo.csv',
        'global_by_iteration.csv',
        'consolidated_all_batches.csv',
        'top20_methods_by_mean_mae.csv',
        'top3_by_block_counts.csv',
        'top3_by_dataset_counts.csv',
        'global_method_stats.csv',
    ]

    # discover other CSVs in the folder (exclude per-batch raw files)
    all_csvs = sorted([p.name for p in batches_dir.glob('*.csv')])
    files = []
    used = set()
    for fname in priority:
        if fname in all_csvs:
            files.append((fname, fname.replace('.csv', '')))
            used.add(fname)
    # Add remaining CSVs that look like summaries (skip batch_ files)
    for fname in all_csvs:
        if fname in used:
            continue
        if fname.startswith('batch_'):
            continue
        if fname == out_xlsx.name:
            continue
        files.append((fname, fname.replace('.csv', '')))

    # Use xlsxwriter for image insertion
    def _sanitize_sheet(name, existing, maxlen=31):
        # replace problematic chars and truncate
        safe = ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in name)
        safe = safe[:maxlen]
        base = safe
        i = 1
        while safe in existing:
            suffix = f"_{i}"
            safe = (base[: maxlen - len(suffix)]) + suffix
            i += 1
        existing.add(safe)
        return safe

    try:
        with pd.ExcelWriter(out_xlsx, engine='xlsxwriter') as writer:
            workbook = writer.book
            existing_sheets = set()

            for fname, sheet in files:
                fp = batches_dir / fname
                df = read_csv_if_exists(fp)
                if df is None:
                    print(f'Skipping missing {fp}')
                    continue
                safe_sheet = _sanitize_sheet(sheet, existing_sheets)
                df.to_excel(writer, sheet_name=safe_sheet, index=False)
                worksheet = writer.sheets[safe_sheet]
                autofilter_and_format(worksheet, df)
                print(f'Wrote sheet {safe_sheet} from {fname}')

            # Add a sheet with the global_summary text if present
            md = batches_dir / 'global_summary.md'
            if md.exists():
                try:
                    with md.open('r', encoding='utf-8') as fh:
                        lines = fh.readlines()
                    # create a simple sheet for text
                    text_sheet = 'global_summary'
                    # write lines into a small dataframe for nicer formatting
                    df_text = pd.DataFrame({'line': [l.rstrip('\n') for l in lines]})
                    df_text.to_excel(writer, sheet_name=text_sheet, index=False)
                    ws = writer.sheets[text_sheet]
                    ws.set_column(0, 0, 120)
                except Exception as e:
                    print('Error writing global_summary.md into Excel: ', e, file=sys.stderr)

            # Insert figures on a dedicated sheet
            fig_dir = batches_dir / 'figures'
            # Insert all available PNG figures into a dedicated sheet
            try:
                fig_sheet = workbook.add_worksheet('Figures')
                row = 0
                col = 0
                if fig_dir.exists():
                    pngs = sorted(fig_dir.glob('*.png'))
                else:
                    pngs = []
                for imgp in pngs:
                    try:
                        # insert image; let xlsxwriter decide sizing
                        fig_sheet.insert_image(row, col, str(imgp))
                    except Exception as e:
                        print(f'Could not insert image {imgp}: {e}', file=sys.stderr)
                    # advance row to avoid overlap
                    row += 30
                print(f'Inserted {len(pngs)} figures into Figures sheet')
            except Exception as e:
                print('Error creating Figures sheet: ', e, file=sys.stderr)

            # Create an index of interactive HTML files if present
            try:
                interactive_dir = batches_dir / 'interactive'
                if interactive_dir.exists():
                    htmls = sorted(interactive_dir.glob('*.html'))
                    if htmls:
                        idx_sheet = workbook.add_worksheet('interactive_index')
                        idx_sheet.set_column(0, 0, 80)
                        idx_sheet.write(0, 0, 'file')
                        idx_sheet.write(0, 1, 'path')
                        r = 1
                        for h in htmls:
                            # write hyperlink (relative path)
                            rel = str(h.relative_to(batches_dir))
                            try:
                                idx_sheet.write_url(r, 0, 'internal:' + rel + '!A1', string=h.name)
                            except Exception:
                                # fallback to plain text path
                                idx_sheet.write(r, 0, h.name)
                            idx_sheet.write(r, 1, str(h))
                            r += 1
                        print(f'Wrote interactive index with {len(htmls)} files')
            except Exception as e:
                print('Error creating interactive index sheet: ', e, file=sys.stderr)

            # finalize
            print(f'Wrote Excel workbook: {out_xlsx}')
    except Exception as e:
        print('Failed to create Excel workbook: ', e, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
