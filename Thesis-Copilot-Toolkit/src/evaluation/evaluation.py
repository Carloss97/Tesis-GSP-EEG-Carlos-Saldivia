"""Funciones de evaluacion para reconstruccion/interpolacion EEG."""

import os
from typing import Any, Dict

import numpy as np


def _downsample_1d(arr: np.ndarray, max_points: int) -> np.ndarray:
    if max_points <= 0 or arr.size <= max_points:
        return arr
    idx = np.linspace(0, arr.size - 1, num=max_points, dtype=int)
    return arr[idx]


def evaluate_signals(
    original: np.ndarray,
    reconstructed: np.ndarray,
    metrics: list | None = None,
    normalize: bool | None = None,
    norm_method: str | None = None,
) -> Dict[str, Any]:
    """Evaluate metrics between `original` and `reconstructed`.

    If `normalize` is None, the environment variable `NORMALIZE_DATASETS`
    controls behavior (0/1). `norm_method` defaults to env `NORM_METHOD` or 'rms'.
    """
    if metrics is None:
        metrics = ["mae", "rmse", "dtw", "snr"]

    # env-driven defaults
    if normalize is None:
        try:
            normalize = bool(int(os.environ.get("NORMALIZE_DATASETS", "0")))
        except Exception:
            normalize = False
    if norm_method is None:
        norm_method = os.environ.get("NORM_METHOD", "rms")

    if normalize:
        orig_n, rec_n = _normalize_signals(original, reconstructed, method=norm_method)
    else:
        orig_n, rec_n = original, reconstructed

    results: Dict[str, Any] = {}
    for metric in metrics:
        key = metric.lower()
        if key == "mae":
            results["mae"] = mean_absolute_error(orig_n, rec_n)
        elif key == "rmse":
            results["rmse"] = root_mean_squared_error(orig_n, rec_n)
        elif key == "dtw":
            results["dtw"] = dtw_distance(orig_n, rec_n)
        elif key == "snr":
            results["snr"] = snr(orig_n, rec_n)
    return results


def evaluate_reconstruction(signals_true: np.ndarray, signals_reconstructed: np.ndarray, metrics: list = None) -> Dict[str, Any]:
    return evaluate_signals(signals_true, signals_reconstructed, metrics=metrics)


def _normalize_signals(y_true: np.ndarray, y_pred: np.ndarray, method: str = "rms") -> tuple[np.ndarray, np.ndarray]:
    """Normalize pairs (y_true, y_pred) per-dataset (per-channel for 2D) using method.

    Supported methods: 'rms', 'median', 'zscore'. Returns normalized copies.
    """
    if method is None:
        return y_true, y_pred

    # Work on copies
    a = y_true.copy()
    b = y_pred.copy()

    if a.ndim == 1:
        mask = ~np.isnan(a)
        if np.sum(mask) == 0:
            return a, b

        if method == "rms":
            scale = float(np.sqrt(np.mean(a[mask] ** 2)))
            if scale <= 0:
                scale = 1.0
            return a / scale, b / scale
        if method == "median":
            scale = float(np.median(np.abs(a[mask])))
            if scale <= 0:
                scale = 1.0
            return a / scale, b / scale
        if method == "zscore":
            mu = float(np.mean(a[mask]))
            sigma = float(np.std(a[mask]))
            if sigma <= 0:
                sigma = 1.0
            return (a - mu) / sigma, (b - mu) / sigma
        return a, b

    # 2D: normalize per channel
    _, n_ch = a.shape
    a_out = a.copy()
    b_out = b.copy()
    for d in range(n_ch):
        mask = ~np.isnan(a[:, d])
        if np.sum(mask) == 0:
            continue
        col = a[mask, d]
        if method == "rms":
            scale = float(np.sqrt(np.mean(col ** 2)))
            if scale <= 0:
                scale = 1.0
            a_out[mask, d] = a[mask, d] / scale
            b_out[mask, d] = b[mask, d] / scale
        elif method == "median":
            scale = float(np.median(np.abs(col)))
            if scale <= 0:
                scale = 1.0
            a_out[mask, d] = a[mask, d] / scale
            b_out[mask, d] = b[mask, d] / scale
        elif method == "zscore":
            mu = float(np.mean(col))
            sigma = float(np.std(col))
            if sigma <= 0:
                sigma = 1.0
            a_out[mask, d] = (a[mask, d] - mu) / sigma
            b_out[mask, d] = (b[mask, d] - mu) / sigma

    return a_out, b_out


def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    mask = ~np.isnan(y_true)
    return float(np.mean(np.abs(y_true[mask] - y_pred[mask])))


def root_mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    mask = ~np.isnan(y_true)
    return float(np.sqrt(np.mean((y_true[mask] - y_pred[mask]) ** 2)))


def dtw_distance(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    max_points = int(os.environ.get("B2_DTW_MAX_POINTS", "80"))

    # Prefer the fast external library but fall back to a local DTW
    # implementation when it's not installed. This prevents a missing
    # optional dependency from aborting whole iterations.
    use_lib = True
    try:
        from dtaidistance import dtw  # type: ignore
    except Exception:
        dtw = None
        use_lib = False

    # Soporta entrada 1D (vector) o 2D (matriz)
    if y_true.ndim == 1:
        mask = ~np.isnan(y_true)
        if np.sum(mask) < 2:
            return float("nan")
        a = _downsample_1d(y_true[mask], max_points=max_points)
        b = _downsample_1d(y_pred[mask], max_points=max_points)
        if use_lib and dtw is not None:
            return float(dtw.distance(a, b))
        return float(_dtw_distance_fallback(a, b, max_points))
    else:
        _, n_channels = y_true.shape
        dist = 0.0
        count = 0
        for d in range(n_channels):
            mask = ~np.isnan(y_true[:, d])
            if np.sum(mask) < 2:
                continue
            a = _downsample_1d(y_true[mask, d], max_points=max_points)
            b = _downsample_1d(y_pred[mask, d], max_points=max_points)
            if use_lib and dtw is not None:
                dist += dtw.distance(a, b)
            else:
                dist += _dtw_distance_fallback(a, b, max_points)
            count += 1
        return float(dist / count) if count > 0 else float("nan")


def _dtw_distance_fallback(x: np.ndarray, y: np.ndarray, max_points: int = 80) -> float:
    """Deterministic bounded DTW fallback used when `dtaidistance` is not available.

    This is a pragmatic, downsampled dynamic-programming implementation copied
    from the lightweight evaluation helper to avoid optional-dependency failures.
    """
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
    # Soporta entrada 1D (vector) o 2D (matriz)
    if y_true.ndim == 1:
        mask = ~np.isnan(y_true)
        signal = y_true[mask]
        noise = y_true[mask] - y_pred[mask]
        noise_var = np.var(noise)
        if noise_var == 0:
            return float("nan")
        return float(10.0 * np.log10(np.var(signal) / noise_var))
    else:
        _, n_channels = y_true.shape
        snr_vals = []
        for d in range(n_channels):
            mask = ~np.isnan(y_true[:, d])
            signal = y_true[mask, d]
            noise = y_true[mask, d] - y_pred[mask, d]
            noise_var = np.var(noise)
            if noise_var == 0:
                continue
            snr_vals.append(10.0 * np.log10(np.var(signal) / noise_var))
        return float(np.mean(snr_vals)) if snr_vals else float("nan")
