"""
evaluation.py
Funciones para evaluar la calidad de la reconstrucción de señales EEG.
"""

from typing import Dict, Any
import numpy as np


def evaluate_signals(original: np.ndarray, reconstructed: np.ndarray, metrics: list = None) -> Dict[str, Any]:
    """
    Calcula métricas de desempeño entre señales originales y reconstruidas.
    - original: matriz (N_instantes, N_electrodos)
    - reconstructed: matriz (N_instantes, N_electrodos)
    - metrics: lista de métricas a calcular ['mae', 'rmse', 'dtw', 'snr']
    Retorna un diccionario con los valores de cada métrica.
    """
    if metrics is None:
        metrics = ['mae', 'rmse', 'dtw', 'snr', 'lsd', 'coherence_mean']
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
        elif metric == 'lsd':
            results['lsd'] = log_spectral_distance(original, reconstructed)
        elif metric == 'coherence_mean':
            results['coherence_mean'] = coherence_mean(original, reconstructed)
    return results


def log_spectral_distance(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Average log spectral distance (LSD) over channels."""
    _, n_ch = y_true.shape
    values = []
    for ch in range(n_ch):
        mask = ~np.isnan(y_true[:, ch])
        if np.sum(mask) < 2:
            continue
        x = y_true[mask, ch]
        y = y_pred[mask, ch]
        x_mag = np.abs(np.fft.rfft(x)) + 1e-12
        y_mag = np.abs(np.fft.rfft(y)) + 1e-12
        lx = np.log(x_mag)
        ly = np.log(y_mag)
        values.append(float(np.sqrt(np.mean((lx - ly) ** 2))))
    return float(np.mean(values)) if values else np.nan


def coherence_mean(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Average magnitude-squared coherence over channels."""
    try:
        from scipy.signal import coherence as scipy_coherence
    except Exception:
        return np.nan

    _, n_ch = y_true.shape
    values = []
    for ch in range(n_ch):
        mask = ~np.isnan(y_true[:, ch])
        n = int(np.sum(mask))
        if n < 4:
            continue
        x = y_true[mask, ch]
        y = y_pred[mask, ch]
        try:
            _, coh = scipy_coherence(x, y, nperseg=min(256, n))
            values.append(float(np.nanmean(coh)))
        except Exception:
            continue
    return float(np.mean(values)) if values else np.nan


def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    mask = ~np.isnan(y_true)
    return np.mean(np.abs(y_true[mask] - y_pred[mask]))


def root_mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    mask = ~np.isnan(y_true)
    return np.sqrt(np.mean((y_true[mask] - y_pred[mask]) ** 2))


def dtw_distance(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    # DTW promedio sobre canales.
    # If dtaidistance is not available, use a deterministic bounded fallback.
    dtw_lib = None
    try:
        from dtaidistance import dtw as dtw_lib
    except ImportError:
        dtw_lib = None

    N, D = y_true.shape
    dist = 0.0
    count = 0
    for d in range(D):
        mask = ~np.isnan(y_true[:, d])
        if np.sum(mask) < 2:
            continue
        series_true = y_true[mask, d]
        series_pred = y_pred[mask, d]
        if dtw_lib is not None:
            dist += dtw_lib.distance(series_true, series_pred)
        else:
            dist += _dtw_distance_fallback(series_true, series_pred)
        count += 1
    return dist / count if count > 0 else np.nan


def _dtw_distance_fallback(x: np.ndarray, y: np.ndarray, max_points: int = 80) -> float:
    """Compute a bounded DTW distance with downsampling for performance stability."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.size > max_points:
        step_x = int(np.ceil(x.size / max_points))
        x = x[::step_x]
    if y.size > max_points:
        step_y = int(np.ceil(y.size / max_points))
        y = y[::step_y]

    n = x.size
    m = y.size
    window = max(abs(n - m), int(0.15 * max(n, m)))

    inf = np.inf
    dp = np.full((n + 1, m + 1), inf, dtype=float)
    dp[0, 0] = 0.0

    for i in range(1, n + 1):
        j_start = max(1, i - window)
        j_end = min(m, i + window)
        for j in range(j_start, j_end + 1):
            cost = abs(x[i - 1] - y[j - 1])
            dp[i, j] = cost + min(dp[i - 1, j], dp[i, j - 1], dp[i - 1, j - 1])

    return float(dp[n, m])


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
