"""
evaluation.py
Funciones para evaluar la calidad de la reconstrucción de señales EEG.
"""

from typing import Dict, Any
import numpy as np
from scipy.spatial.distance import euclidean
from scipy.signal import detrend


def evaluate_signals(original: np.ndarray, reconstructed: np.ndarray, metrics: list = None) -> Dict[str, Any]:
    """
    Calcula métricas de desempeño entre señales originales y reconstruidas.
    - original: matriz (N_instantes, N_electrodos)
    - reconstructed: matriz (N_instantes, N_electrodos)
    - metrics: lista de métricas a calcular ['mae', 'rmse', 'dtw', 'snr']
    Retorna un diccionario con los valores de cada métrica.
    """
    if metrics is None:
        metrics = ['mae', 'rmse', 'dtw', 'snr']
    results = {}
    for metric in metrics:
        if metric == 'mae':
            results['mae'] = mean_absolute_error(original, reconstructed)
        elif metric == 'rmse':
            results['rmse'] = root_mean_squared_error(original, reconstructed)
        elif metric == 'dtw':
            results['dtw'] = dtw_distance(original, reconstructed)
        elif metric == 'snr':
            results['snr'] = snr(original, reconstructed)
    return results


def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    mask = ~np.isnan(y_true)
    return np.mean(np.abs(y_true[mask] - y_pred[mask]))


def root_mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    mask = ~np.isnan(y_true)
    return np.sqrt(np.mean((y_true[mask] - y_pred[mask]) ** 2))


def dtw_distance(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    # DTW promedio sobre canales
    try:
        from dtaidistance import dtw
    except ImportError:
        raise ImportError('Instale dtaidistance para usar DTW')
    N, D = y_true.shape
    dist = 0.0
    count = 0
    for d in range(D):
        mask = ~np.isnan(y_true[:, d])
        if np.sum(mask) < 2:
            continue
        dist += dtw.distance(y_true[mask, d], y_pred[mask, d])
        count += 1
    return dist / count if count > 0 else np.nan


def snr(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    # SNR promedio sobre canales
    N, D = y_true.shape
    snr_vals = []
    for d in range(D):
        mask = ~np.isnan(y_true[:, d])
        signal = y_true[mask, d]
        noise = y_true[mask, d] - y_pred[mask, d]
        if np.var(noise) == 0:
            continue
        snr_vals.append(10 * np.log10(np.var(signal) / np.var(noise)))
    return np.mean(snr_vals) if snr_vals else np.nan
