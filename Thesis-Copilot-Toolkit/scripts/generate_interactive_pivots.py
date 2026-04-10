#!/usr/bin/env python3
"""
Generate interactive HTML visualizations for pivot tables using Plotly.

Outputs saved to `results/analysis/batches/interactive/`:
- heatmap_graph.html
- heatmap_dataset.html
- heatmap_missing.html
- best_method_counts.html
- index.html (links)
"""
from pathlib import Path
import pandas as pd
import argparse
import sys

try:
    import plotly.graph_objects as go
    import plotly.offline as pyo
except Exception:
    print("Plotly not installed. Run: .venv\\Scripts\\python.exe -m pip install plotly", file=sys.stderr)
    sys.exit(1)


def load_pivot(path: Path):
    if not path.exists():
        print(f"Missing pivot file: {path}")
        return None
    try:
        df = pd.read_csv(path, index_col=0)
        df.index = df.index.astype(str)
        df.columns = df.columns.astype(str)
        df = df.apply(pd.to_numeric, errors='coerce')
        return df
    except Exception as e:
        print(f"Error reading pivot {path}: {e}")
        return None


def make_heatmap(df, title):
    z = df.values
    x = df.columns.tolist()
    y = df.index.tolist()
    fig = go.Figure(data=go.Heatmap(z=z, x=x, y=y, colorscale='Viridis', colorbar=dict(title='mean MAE')))
    fig.update_layout(title=title, xaxis_title='columns', yaxis_title='methods', height=max(600, 20 * len(y)))
    return fig


def make_bar_counts(df_counts):
    df = df_counts.sort_values('best_count', ascending=True)
    fig = go.Figure(go.Bar(x=df['best_count'], y=df['method'], orientation='h'))
    fig.update_layout(title='Best-method counts', xaxis_title='count', yaxis_title='method', height=max(400, 20 * len(df)))
    return fig


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--batches-dir', default=None)
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    root = script_path.parent.parent
    default_batches = root / 'results' / 'analysis' / 'batches'
    batches_dir = Path(args.batches_dir) if args.batches_dir else default_batches
    if not batches_dir.exists():
        print(f'Batches dir not found: {batches_dir}')
        sys.exit(1)

    out_dir = batches_dir / 'interactive'
    out_dir.mkdir(parents=True, exist_ok=True)

    files = {
        'graph': batches_dir / 'pivot_method_by_graph_mean_mae.csv',
        'dataset': batches_dir / 'pivot_method_by_dataset_mean_mae.csv',
        'missing': batches_dir / 'pivot_method_by_missing_ratio_mean_mae.csv',
        'counts': batches_dir / 'best_method_counts.csv',
    }

    written = []

    # Heatmaps
    for key in ('graph', 'dataset', 'missing'):
        p = files[key]
        df = load_pivot(p)
        if df is None or df.empty:
            print(f'Skipping {key} heatmap; source missing or empty: {p}')
            continue
        title = {'graph': 'Mean MAE: method × graph', 'dataset': 'Mean MAE: method × dataset', 'missing': 'Mean MAE: method × missing_ratio'}[key]
        fig = make_heatmap(df, title)
        out = out_dir / f'heatmap_{key}.html'
        pyo.plot(fig, filename=str(out), auto_open=False, include_plotlyjs='cdn')
        print(f'Wrote {out}')
        written.append(out)

    # Best-method counts bar
    pcounts = files['counts']
    if pcounts.exists():
        try:
            dfc = pd.read_csv(pcounts)
            fig = make_bar_counts(dfc)
            out = out_dir / 'best_method_counts.html'
            pyo.plot(fig, filename=str(out), auto_open=False, include_plotlyjs='cdn')
            print(f'Wrote {out}')
            written.append(out)
        except Exception as e:
            print(f'Error creating counts plot: {e}')
    else:
        print(f'Counts file not found: {pcounts}')

    # index
    idx = out_dir / 'index.html'
    with idx.open('w', encoding='utf-8') as fh:
        fh.write('<html><head><meta charset="utf-8"><title>Interactive pivots</title></head><body>')
        fh.write('<h1>Interactive pivot visualizations</h1>\n<ul>')
        for f in sorted(written):
            fh.write(f'<li><a href="{f.name}">{f.name}</a></li>\n')
        fh.write('</ul></body></html>')
    print(f'Wrote {idx}')
    print('Done.')


if __name__ == '__main__':
    main()
