from pathlib import Path
import argparse
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_RESULTS_DIR = ROOT / "results"
DEFAULT_OUTPUT_DIR = DEFAULT_RESULTS_DIR / "plots"

METRIC_COLUMNS = ["MAE", "RMSE", "DTW", "SNR", "LSD", "COHERENCE_MEAN"]
LOWER_IS_BETTER = {"MAE", "RMSE", "DTW", "LSD"}
BASELINE_METHODS = {"linear", "ica", "spherical_spline", "rbfi_tps", "rbfi"}
TV_METHODS = {
    "graph_time_tikhonov",
    "trss",
    "tv",
    "temporal_laplacian",
    "sobolev_temporal",
    "directed_tv",
    "heat_diffusion_temporal",
    "wavelet_temporal",
}
FAMILY_ORDER = ["Baseline", "GSP Instantáneo", "TV/Tiempo"]


def _safe_name(value):
    return str(value).replace(" ", "_").replace("/", "_")


def _canonical_family(method):
    method_name = str(method).lower()
    if method_name in BASELINE_METHODS or "spline" in method_name:
        return "Baseline"
    if method_name in TV_METHODS:
        return "TV/Tiempo"
    return "GSP Instantáneo"


def _rename_columns(df):
    rename_map = {}
    for column in df.columns:
        lower = column.lower()
        if lower in {"mae", "rmse", "dtw", "snr"}:
            rename_map[column] = lower.upper()
        elif lower == "lsd":
            rename_map[column] = "LSD"
        elif lower == "coherence_mean":
            rename_map[column] = "COHERENCE_MEAN"
        elif lower in {"method_family", "family"}:
            rename_map[column] = "Familia"
        elif lower == "method":
            rename_map[column] = "Metodo"
        elif lower in {"missing_level", "missing_ratio"}:
            rename_map[column] = "Missing_Level"
        elif lower == "dataset":
            rename_map[column] = "Dataset"
        elif lower in {"graph", "graph_method"}:
            rename_map[column] = "Grafo"
        elif lower == "reconstructed_signal":
            rename_map[column] = "reconstructed_signal"
    return df.rename(columns=rename_map)


def _ensure_core_columns(df):
    for column in ["Dataset", "Grafo", "Metodo"]:
        if column not in df.columns:
            df[column] = "N/A"
    df["Dataset"] = df["Dataset"].fillna("N/A")
    df["Grafo"] = df["Grafo"].fillna("N/A")
    df["Metodo"] = df["Metodo"].fillna("N/A")

    # Garantizar que las métricas sean numéricas para evitar errores de cálculo en mean/median
    for metric in METRIC_COLUMNS:
        if metric in df.columns:
            df[metric] = pd.to_numeric(df[metric], errors="coerce")

    if "Familia" not in df.columns:
        df["Familia"] = df["Metodo"].apply(_canonical_family)
    else:
        df["Familia"] = df["Familia"].fillna("").astype(str)
        missing_family = df["Familia"].eq("") | df["Familia"].str.lower().eq("nan")
        df.loc[missing_family, "Familia"] = df.loc[missing_family, "Metodo"].apply(_canonical_family)

    df["Combinacion"] = (
        df["Dataset"].astype(str) + " | " + df["Grafo"].astype(str) + " | " + df["Metodo"].astype(str)
    )
    return df


def _available_metrics(df):
    return [metric for metric in METRIC_COLUMNS if metric in df.columns]


def _filter_extremes(data, metric):
    if metric not in data.columns or data[metric].isnull().all():
        return data
    q_low, q_high = data[metric].quantile(0.05), data[metric].quantile(0.95)
    return data[(data[metric] >= q_low) & (data[metric] <= q_high)]


def _plot_family_metric_grid(df_dataset, dataset_name, dataset_metrics, output_dir):
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle(f"Desempeño promedio por familia - Dataset: {dataset_name}", fontsize=16)

    for index, metric in enumerate(dataset_metrics):
        ax = axes[index // 3, index % 3]
        df_metric_filtered = _filter_extremes(df_dataset, metric)
        sns.barplot(
            data=df_metric_filtered,
            x="Familia",
            y=metric,
            order=FAMILY_ORDER,
            ax=ax,
            capsize=0.1,
            errorbar="sd",
            palette="viridis",
        )
        metric_label = "coherence_mean" if metric == "COHERENCE_MEAN" else metric
        ax.set_title(metric_label)
        ax.set_xlabel("")
        ax.set_ylabel(f"{metric_label} ({'Menor' if metric in LOWER_IS_BETTER else 'Mayor'} es mejor)")
        ax.tick_params(axis="x", rotation=25)

    for index in range(len(dataset_metrics), 6):
        axes[index // 3, index % 3].axis("off")

    plt.tight_layout()
    plt.savefig(output_dir / f"{dataset_name}_familia_metricas_promedio.png", dpi=300)
    plt.close(fig)


def _plot_family_dispersion_grid(df_dataset, dataset_name, dataset_metrics, output_dir):
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle(f"Dispersión por familia - Dataset: {dataset_name}", fontsize=16)

    for index, metric in enumerate(dataset_metrics):
        ax = axes[index // 3, index % 3]
        df_metric_filtered = _filter_extremes(df_dataset, metric)
        sns.boxplot(
            data=df_metric_filtered,
            x="Familia",
            y=metric,
            order=FAMILY_ORDER,
            ax=ax,
            palette="Set2",
        )
        metric_label = "coherence_mean" if metric == "COHERENCE_MEAN" else metric
        ax.set_title(metric_label)
        ax.set_xlabel("")
        ax.set_ylabel(metric_label)
        ax.tick_params(axis="x", rotation=25)

    for index in range(len(dataset_metrics), 6):
        axes[index // 3, index % 3].axis("off")

    plt.tight_layout()
    plt.savefig(output_dir / f"{dataset_name}_familia_metricas_dispersion.png", dpi=300)
    plt.close(fig)


def _plot_metric_comparison(df_dataset, dataset_name, metric, output_dir):
    df_filtered = _filter_extremes(df_dataset, metric)
    if df_filtered.empty:
        print(f"No hay datos para la métrica {metric} en el dataset {dataset_name} después de filtrar.")
        return

    unique_combs = df_filtered["Combinacion"].nunique()
    if unique_combs == 0:
        print(f"No hay combinaciones para graficar en el dataset {dataset_name}.")
        return

    ascending_order = metric in LOWER_IS_BETTER
    order = df_filtered.groupby("Combinacion")[metric].median().sort_values(ascending=ascending_order).index
    fig_height = max(8, unique_combs * 0.35)
    fig, ax = plt.subplots(figsize=(14, fig_height))

    sns.boxplot(
        data=df_filtered,
        x=metric,
        y="Combinacion",
        ax=ax,
        order=order,
        palette="tab20",
        orient="h",
    )
    metric_label = "coherence_mean" if metric == "COHERENCE_MEAN" else metric
    ax.set_title(f"Distribución de {metric_label} por combinación - Dataset: {dataset_name}", fontsize=16)
    ax.set_xlabel(f"{metric_label} {'(Menor es mejor)' if ascending_order else '(Mayor es mejor)'}")
    ax.set_ylabel("Combinación (Grafo | Método)")

    labels = [item.get_text().replace(f"{dataset_name} | ", "") for item in ax.get_yticklabels()]
    ax.set_yticklabels(labels)

    plt.tight_layout()
    plt.savefig(output_dir / f"{dataset_name}_combinacion_detallada_{metric.lower()}.png", dpi=300)
    plt.close(fig)


def _export_summary_tables(df, metrics, output_dir):
    # Guardar en una carpeta dedicada a las tablas para mayor claridad
    tables_dir = output_dir.parent / "tablas_resumen"
    tables_dir.mkdir(parents=True, exist_ok=True)
    print(f"\nExportando tablas de resumen a CSV en: {tables_dir} ...")

    summary_combinaciones = df.groupby(["Dataset", "Familia", "Combinacion"], as_index=False).agg(
        n_rows=("Metodo", "size"),
        **{metric: (metric, "median") for metric in metrics},
    )
    summary_combinaciones.to_csv(tables_dir / "resumen_combinaciones_mediana.csv", index=False)

    summary_combinaciones_mean = df.groupby(["Dataset", "Familia", "Combinacion"], as_index=False).agg(
        n_rows=("Metodo", "size"),
        **{metric: (metric, "mean") for metric in metrics},
    )
    summary_combinaciones_mean.to_csv(tables_dir / "resumen_combinaciones_medias.csv", index=False)

    family_agg = {"n_rows": ("Metodo", "size")}
    for metric in metrics:
        family_agg[f"{metric}_mean"] = (metric, "mean")
        family_agg[f"{metric}_median"] = (metric, "median")
        family_agg[f"{metric}_std"] = (metric, "std")

    summary_familias = df.groupby(["Dataset", "Familia"], as_index=False).agg(**family_agg)
    summary_familias.to_csv(tables_dir / "resumen_familias_stats.csv", index=False)

    # Top 5 recomendaciones (excluyendo Baseline)
    df_no_baseline = df[df["Familia"] != "Baseline"]
    recommendations = []
    
    # Sistema de puntuación ponderada (Priorizando dinámica sobre amplitud pura)
    target_weights = {
        "LSD": 0.35,
        "COHERENCE_MEAN": 0.25,
        "DTW": 0.20,
        "MAE": 0.15,
        "RMSE": 0.05,
        "SNR": 0.0
    }

    for dataset in df_no_baseline["Dataset"].unique():
        df_ds = df_no_baseline[df_no_baseline["Dataset"] == dataset]
        grouped = df_ds.groupby(["Familia", "Grafo", "Metodo", "Combinacion"], as_index=False)[metrics].mean()
        
        # Identificar qué métricas existen en este dataset específico
        dataset_metrics = [m for m in metrics if grouped[m].notna().any()]
        if not dataset_metrics:
            continue
        
        # Calcular Score Compuesto (0 a 1) normalizando las métricas (Min-Max Scaling)
        score = pd.Series(0.0, index=grouped.index)
        active_weights_sum = sum(target_weights.get(m, 0.1) for m in dataset_metrics)
        
        for m in dataset_metrics:
            c_min, c_max = grouped[m].min(), grouped[m].max()
            w = target_weights.get(m, 0.1) / active_weights_sum
            if c_max > c_min:
                norm = (c_max - grouped[m]) / (c_max - c_min) if m in LOWER_IS_BETTER else (grouped[m] - c_min) / (c_max - c_min)
            else:
                norm = pd.Series(1.0, index=grouped.index) # Sin varianza todos ganan
            score += norm.fillna(0.0) * w
            
        grouped.insert(4, "Composite_Score", score.round(4))
        grouped = grouped.sort_values(by="Composite_Score", ascending=False).head(5)
        grouped.insert(0, "Dataset", dataset)
        grouped.insert(0, "Rank", range(1, len(grouped) + 1))
        recommendations.append(grouped)
        
    if recommendations:
        df_recs = pd.concat(recommendations, ignore_index=True)
        df_recs.to_csv(tables_dir / "top5_combinaciones_recomendadas_gsp.csv", index=False)


def load_all_iterations(results_dir):
    """Busca y concatena todos los archivos it*_raw.csv del directorio."""
    results_path = Path(results_dir)
    raw_files = sorted(results_path.glob("it*_raw.csv"))

    if not raw_files:
        print("No se encontraron archivos crudos. Buscando stats...")
        stats_files = sorted(results_path.glob("it*_stats.csv"))
        if not stats_files:
            print("No se encontraron archivos de iteraciones en el directorio. Generando dummy data.")
            return simulate_dummy_data()

        print(f"Se encontraron {len(stats_files)} archivos stats, pero este analizador requiere el CSV crudo para combinar grafos y métricas. Generando dummy data.")
        return simulate_dummy_data()

    print(f"Cargando {len(raw_files)} archivos de iteraciones desde {results_path}...")
    df_list = [pd.read_csv(file_path) for file_path in raw_files]
    df_concat = pd.concat(df_list, ignore_index=True)
    df_concat = _rename_columns(df_concat)
    df_concat = _ensure_core_columns(df_concat)

    # Ignorar resultados que utilicen visibility_NNK
    df_concat = df_concat[~df_concat["Combinacion"].str.contains("visibility_nnk", case=False, na=False)]

    return df_concat


def generate_metric_plots(results_dir=DEFAULT_RESULTS_DIR, output_dir=DEFAULT_OUTPUT_DIR):
    """Genera 6 gráficos métricos y 2 gráficos de familia por dataset."""
    results_path = Path(results_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    df = load_all_iterations(results_path)
    metrics = _available_metrics(df)
    if not metrics:
        print("Las columnas de métricas no se encontraron en los datos cargados.")
        return

    sns.set_theme(style="whitegrid")

    datasets = [dataset for dataset in pd.unique(df["Dataset"]) if pd.notna(dataset)]
    print(f"Análisis encontrado para los siguientes datasets: {datasets}")

    # Exportar tablas ANTES de graficar asegura que los CSV salgan aunque falle algún gráfico
    _export_summary_tables(df, metrics, output_path)

    for dataset_name in datasets:
        print(f"\n--- Generando gráficos para el dataset: {dataset_name} ---")
        df_dataset = df[df["Dataset"] == dataset_name].copy()
        if df_dataset.empty:
            continue

        dataset_metrics = [m for m in metrics if df_dataset[m].notna().any()]
        if not dataset_metrics:
            print(f"No hay métricas válidas para el dataset {dataset_name}. Omitiendo gráficos.")
            continue

        safe_dataset = _safe_name(dataset_name)

        try:
            _plot_family_metric_grid(df_dataset, safe_dataset, dataset_metrics, output_path)
            _plot_family_dispersion_grid(df_dataset, safe_dataset, dataset_metrics, output_path)

            for metric in dataset_metrics:
                _plot_metric_comparison(df_dataset, safe_dataset, metric, output_path)
        except Exception as e:
            print(f"Error al generar gráficos para el dataset {dataset_name}: {e}. Omitiendo gráficos para este dataset.")

    print(f"\nProceso finalizado. Gráficos generados en {output_path}")


def simulate_dummy_data():
    """Genera un DataFrame dummy para probar el script."""
    np.random.seed(42)
    familias = ["Baseline", "GSP Instantáneo", "TV/Tiempo"]
    datasets = ["MNE", "PhysioNet"]
    data = []
    for ds in datasets:
        for fam in familias:
            for _ in range(25):
                if fam == "Baseline":
                    base_mae = 0.12 if ds == "MNE" else 0.18
                    data.append([
                        fam,
                        "Random",
                        0.2,
                        np.random.normal(base_mae, 0.01),
                        np.random.normal(base_mae + 0.03, 0.02),
                        np.random.normal(4.5, 0.5),
                        np.random.normal(18, 2),
                        np.random.normal(0.8, 0.08),
                        np.random.normal(0.62, 0.06),
                        ds,
                        "N/A",
                        "spherical_spline",
                    ])
                elif fam == "GSP Instantáneo":
                    base_mae = 0.11 if ds == "MNE" else 0.17
                    data.append([
                        fam,
                        "Random",
                        0.2,
                        np.random.normal(base_mae, 0.03),
                        np.random.normal(base_mae + 0.09, 0.10),
                        np.random.normal(4.3, 0.6),
                        np.random.normal(19, 4),
                        np.random.normal(0.9, 0.1),
                        np.random.normal(0.58, 0.07),
                        ds,
                        "knn",
                        "tikhonov",
                    ])
                else:
                    base_mae = 0.11 if ds == "MNE" else 0.16
                    data.append([
                        fam,
                        "Random",
                        0.2,
                        np.random.normal(base_mae, 0.02),
                        np.random.normal(base_mae + 0.05, 0.05),
                        np.random.normal(2.5, 0.3),
                        np.random.normal(22, 3),
                        np.random.normal(0.72, 0.05),
                        np.random.normal(0.75, 0.05),
                        ds,
                        "gaussian",
                        "trss",
                    ])

    return pd.DataFrame(
        data,
        columns=[
            "Familia",
            "Escenario",
            "Missing_Level",
            "MAE",
            "RMSE",
            "DTW",
            "SNR",
            "LSD",
            "COHERENCE_MEAN",
            "Dataset",
            "Grafo",
            "Metodo",
        ],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Análisis Global de Iteraciones")
    parser.add_argument(
        "--results_dir",
        type=str,
        default=str(DEFAULT_RESULTS_DIR),
        help="Directorio donde están los it*_raw.csv",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directorio de salida para los gráficos",
    )
    args = parser.parse_args()

    generate_metric_plots(args.results_dir, args.output_dir)