"""
reporting.py
Herramientas para análisis, visualización y reporte de resultados del pipeline EEG-GSP.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any


def results_to_table(results: list, filename: str = None) -> pd.DataFrame:
    """
    Convierte una lista de diccionarios de resultados en una tabla pandas.
    Si filename se especifica, guarda la tabla como CSV.
    """
    df = pd.DataFrame(results)
    if filename:
        df.to_csv(filename, index=False)
    return df


def plot_metric_comparison(df: pd.DataFrame, metric: str, method_col: str = 'method', dataset_col: str = 'dataset', savepath: str = None):
    """
    Genera un boxplot/comparación de una métrica entre métodos y datasets.
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=method_col, y=metric, hue=dataset_col, data=df)
    plt.title(f'Comparación de {metric}')
    plt.tight_layout()
    if savepath:
        plt.savefig(savepath)
    plt.show()


def summary_report(df: pd.DataFrame, metrics: list = None) -> str:
    """
    Genera un resumen textual de los resultados principales.
    """
    if metrics is None:
        metrics = ['mae', 'rmse', 'dtw', 'snr']
    report = "Resumen de resultados:\n"
    for metric in metrics:
        if metric not in df.columns:
            continue
        if metric.lower() == 'snr':
            best_row = df.loc[df[metric].idxmax()]
        else:
            best_row = df.loc[df[metric].idxmin()]
        report += f"Mejor {metric}: Método={best_row['method']}, Dataset={best_row['dataset']}, Valor={best_row[metric]:.4f}\n"
    return report
