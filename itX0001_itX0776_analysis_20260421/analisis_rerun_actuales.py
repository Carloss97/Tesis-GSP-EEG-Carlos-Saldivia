import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Configuración de directorios
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ANALYSIS_DIR = os.path.dirname(os.path.abspath(__file__))


# Buscar archivos itX####_raw.csv (itX0001_*, itX0002_*, ..., itX0776_*)
raw_files = sorted(glob.glob(os.path.join(RESULTS_DIR, 'itX[0-9][0-9][0-9][0-9]_raw.csv')))
significance_files = sorted(glob.glob(os.path.join(RESULTS_DIR, 'itX[0-9][0-9][0-9][0-9]_significance.csv')))
stats_files = sorted(glob.glob(os.path.join(RESULTS_DIR, 'itX[0-9][0-9][0-9][0-9]_stats.csv')))
metadata_files = sorted(glob.glob(os.path.join(RESULTS_DIR, 'itX[0-9][0-9][0-9][0-9]_run_metadata.json')))

# Cargar y agregar todos los resultados raw
raw_dfs = []
for f in raw_files:
    try:
        df = pd.read_csv(f)
        df['run_file'] = os.path.basename(f)
        raw_dfs.append(df)
    except Exception as e:
        print(f"Error leyendo {f}: {e}")

if not raw_dfs:
    raise RuntimeError("No se encontraron archivos itX####_raw.csv para analizar.")

raw_all = pd.concat(raw_dfs, ignore_index=True)

# Ejemplo: resumen por método y dataset
summary = raw_all.groupby(['method', 'dataset']).agg({'mae': ['mean', 'std'], 'snr': ['mean', 'std']}).reset_index()
summary.columns = ['method', 'dataset', 'mae_mean', 'mae_std', 'snr_mean', 'snr_std']
summary.to_csv(os.path.join(ANALYSIS_DIR, 'summary_by_method_dataset.csv'), index=False)




# Figuras: boxplot MAE y SNR por dataset, mostrando todos los métodos en X y grafo como hue (1 figura por dataset)
def plot_metric_by_method_and_graph(df, metric, fname_prefix):
    datasets = df['dataset'].unique()
    for ds in datasets:
        data_ds = df[df['dataset'] == ds].copy()
        if 'graph' in data_ds.columns:
            hue = 'graph'
        else:
            hue = None
        # Excluir outliers usando IQR
        Q1 = data_ds[metric].quantile(0.25)
        Q3 = data_ds[metric].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        data_inlier = data_ds[(data_ds[metric] >= lower) & (data_ds[metric] <= upper)]
        outlier_methods = data_ds[data_ds[metric] > upper]['method'].unique().tolist()
        plt.figure(figsize=(14, 7))
        sns.boxplot(data=data_inlier, x='method', y=metric, hue=hue, showfliers=True)
        plt.title(f'{metric.upper()} por método' + (f' y grafo - {ds}' if hue else f' - {ds}') + ' (sin outliers extremos)')
        plt.xticks(rotation=45)
        # Anotar valores extremos
        for m in outlier_methods:
            vals = data_ds[(data_ds['method'] == m) & (data_ds[metric] > upper)][metric]
            if not vals.empty:
                x = list(data_inlier['method'].unique()).index(m) if m in data_inlier['method'].unique() else len(data_inlier['method'].unique())
                for v in vals:
                    plt.scatter(x, upper*1.02, marker='x', color='red', label=f'{m} extremo' if metric==metric and m==outlier_methods[0] else "")
                    plt.annotate(f'{v:.2f}', (x, upper*1.02), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='red')
        plt.tight_layout()
        plt.savefig(os.path.join(ANALYSIS_DIR, f'{fname_prefix}_by_method_{ds}.png'))
        plt.close()

# Graficar MAE y SNR por dataset (1 figura por dataset, grafo como hue si existe)
plot_metric_by_method_and_graph(raw_all, 'mae', 'mae')
plot_metric_by_method_and_graph(raw_all, 'snr', 'snr')


# Top 3 (o top 6 si hay baseline en top3) métodos por dataset, garantizando al menos 3 no baseline
def is_baseline(method_name):
    baseline_set = {'rbfi_tps', 'linear', 'spherical_spline', 'ica'}
    return method_name.strip().lower() in baseline_set

top_methods = []
for ds in summary['dataset'].unique():
    df_ds = summary[summary['dataset'] == ds].sort_values('mae_mean')
    top3 = df_ds.head(3)
    n_baseline = top3['method'].apply(is_baseline).sum()
    if n_baseline > 0:
        # Expandir a top 7 y asegurar al menos 3 no baseline
        expanded = df_ds.head(7)
        non_baseline = expanded[~expanded['method'].apply(is_baseline)]
        baseline = expanded[expanded['method'].apply(is_baseline)]
        # Tomar hasta 3 no baseline, y el resto baseline hasta completar 7
        n_non_baseline = min(3, len(non_baseline))
        n_baseline_needed = 7 - n_non_baseline
        top_methods.append(pd.concat([non_baseline.head(n_non_baseline), baseline.head(n_baseline_needed)]))
    else:
        top_methods.append(top3)
top_methods_df = pd.concat(top_methods).drop_duplicates(['dataset', 'method'])
top_methods_df.to_csv(os.path.join(ANALYSIS_DIR, 'top_methods_by_dataset.csv'), index=False)

# Resumen de mejores métodos (menor MAE) por dataset (solo el mejor)
best_methods = summary.sort_values('mae_mean').groupby('dataset').first().reset_index()
best_methods.to_csv(os.path.join(ANALYSIS_DIR, 'best_methods_by_dataset.csv'), index=False)


# Guardar reporte resumen extendido
with open(os.path.join(ANALYSIS_DIR, 'reporte_resumen.txt'), 'w', encoding='utf-8') as f:
    f.write('Resumen de mejores métodos por dataset (menor MAE):\n')
    f.write(best_methods.to_string(index=False))
    f.write('\n\nTop métodos por dataset (ver top_methods_by_dataset.csv):\n')
    f.write(top_methods_df.to_string(index=False))
    f.write('\n\nTotal de runs analizados: %d\n' % len(raw_files))
    f.write('Archivos procesados:\n')
    for fname in raw_files:
        f.write(' - %s\n' % os.path.basename(fname))


# Análisis de combinaciones dataset-grafo-método y figuras detalladas si existe la columna 'graph'
if 'graph' in raw_all.columns:
    combo_summary = raw_all.groupby(['dataset', 'graph', 'method']).agg({'mae': ['mean', 'std'], 'snr': ['mean', 'std']}).reset_index()
    combo_summary.columns = ['dataset', 'graph', 'method', 'mae_mean', 'mae_std', 'snr_mean', 'snr_std']
    combo_summary.to_csv(os.path.join(ANALYSIS_DIR, 'summary_by_dataset_graph_method.csv'), index=False)

    # Figuras: boxplot MAE y SNR por método para cada dataset-grafo
    def plot_metric_by_method_per_dataset_graph(df, metric, fname_prefix):
        datasets = df['dataset'].unique()
        for ds in datasets:
            graphs = df[df['dataset'] == ds]['graph'].unique()
            for gr in graphs:
                data_dg = raw_all[(raw_all['dataset'] == ds) & (raw_all['graph'] == gr)].copy()
                if data_dg.empty:
                    continue
                # Excluir outliers usando IQR
                Q1 = data_dg[metric].quantile(0.25)
                Q3 = data_dg[metric].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR
                data_inlier = data_dg[(data_dg[metric] >= lower) & (data_dg[metric] <= upper)]
                outlier_methods = data_dg[data_dg[metric] > upper]['method'].unique().tolist()
                plt.figure(figsize=(12, 6))
                sns.boxplot(data=data_inlier, x='method', y=metric, showfliers=True, color='skyblue')
                plt.title(f'{metric.upper()} por método - {ds} - {gr} (sin outliers extremos)')
                plt.xticks(rotation=45)
                # Anotar valores extremos
                for m in outlier_methods:
                    vals = data_dg[(data_dg['method'] == m) & (data_dg[metric] > upper)][metric]
                    if not vals.empty:
                        x = list(data_inlier['method'].unique()).index(m) if m in data_inlier['method'].unique() else len(data_inlier['method'].unique())
                        for v in vals:
                            plt.scatter(x, upper*1.02, marker='x', color='red', label=f'{m} extremo' if metric==metric and m==outlier_methods[0] else "")
                            plt.annotate(f'{v:.2f}', (x, upper*1.02), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='red')
                plt.tight_layout()
                fname = f'{fname_prefix}_by_method_{ds}_graph_{gr}.png'.replace("/", "_").replace(" ", "_")
                plt.savefig(os.path.join(ANALYSIS_DIR, fname))
                plt.close()

    plot_metric_by_method_per_dataset_graph(raw_all, 'mae', 'mae')
    plot_metric_by_method_per_dataset_graph(raw_all, 'snr', 'snr')

print('Análisis completado. Resultados y figuras guardados en:', ANALYSIS_DIR)
