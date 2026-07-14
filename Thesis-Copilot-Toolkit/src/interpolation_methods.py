"""Interpolation methods for EEG reconstruction with missing channels."""

import warnings
from typing import Any, Dict, List, Tuple

import numpy as np
from scipy.interpolate import Rbf, SmoothBivariateSpline
from scipy.special import lpmv

from src.interpolation_warning_registry import record_warning


def _nanmean_no_warn(values: np.ndarray, axis: int | None = None) -> np.ndarray:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        m = np.nanmean(values, axis=axis)
    if np.isscalar(m):
        return float(0.0 if np.isnan(m) else m)
    return np.where(np.isnan(m), 0.0, m)


def _pinv_matlab(a: np.ndarray) -> np.ndarray:
    # MATLAB-like tolerance: tol = max(size(A)) * eps(norm(A))
    u, s, vh = np.linalg.svd(a, full_matrices=False)
    if s.size == 0:
        return np.zeros_like(a.T)
    tol = max(a.shape) * np.spacing(np.linalg.norm(a, ord=2))
    s_inv = np.zeros_like(s)
    keep = s > tol
    s_inv[keep] = 1.0 / s[keep]
    return (vh.T * s_inv) @ u.T


def _normalize_positions_for_mne(positions: np.ndarray) -> np.ndarray:
    pos = np.asarray(positions, dtype=float)
    if pos.ndim != 2 or pos.shape[1] < 2:
        raise ValueError("'positions' must be a 2D array with at least 2 coordinates per channel.")

    if pos.shape[1] == 2:
        pos = np.column_stack([pos, np.zeros(pos.shape[0])])
    else:
        pos = pos[:, :3].copy()

    finite_rows = np.isfinite(pos).all(axis=1)
    if not np.any(finite_rows):
        return np.zeros((pos.shape[0], 3), dtype=float)

    center = np.mean(pos[finite_rows], axis=0)
    pos = pos - center
    radii = np.linalg.norm(pos[finite_rows], axis=1)
    scale = float(np.max(radii)) if radii.size else 1.0
    if not np.isfinite(scale) or scale <= 0:
        scale = 1.0
    pos = pos / scale
    pos[~finite_rows] = 0.0
    return pos


def _impute_missing_with_row_mean(data: np.ndarray) -> np.ndarray:
    filled = np.asarray(data, dtype=float).copy()
    if filled.ndim != 2:
        raise ValueError("data must be a 2D array.")

    row_mean = _nanmean_no_warn(filled, axis=1)
    if np.isscalar(row_mean):
        row_mean = np.full((filled.shape[0],), float(row_mean), dtype=float)
    row_mean = np.asarray(row_mean, dtype=float)
    row_mean[~np.isfinite(row_mean)] = 0.0

    missing = np.isnan(filled)
    if missing.any():
        filled[missing] = np.take(row_mean, np.where(missing)[0])
    return filled


def _build_mne_eeg_raw(
    signals: np.ndarray,
    positions: np.ndarray | None = None,
    sfreq: float = 250.0,
    ch_names: List[str] | None = None,
    bads: List[str] | None = None,
    normalize_positions: bool = True,
):
    try:
        import mne
    except Exception as exc:
        raise ImportError("mne is required for the MNE-based interpolation backends.") from exc

    data = np.asarray(signals, dtype=float)
    if data.ndim != 2:
        raise ValueError("signals must be a 2D array with shape (n_times, n_channels).")

    n_times, n_channels = data.shape
    if ch_names is None:
        ch_names = [f"EEG{idx:03d}" for idx in range(n_channels)]
    if len(ch_names) != n_channels:
        raise ValueError("ch_names must match the number of channels in signals.")

    info = mne.create_info(ch_names=ch_names, sfreq=float(sfreq), ch_types="eeg")

    if np.isnan(data).any():
        data = _impute_missing_with_row_mean(data)

    raw = mne.io.RawArray(data.T, info, verbose="ERROR")

    if positions is not None:
        pos = _normalize_positions_for_mne(positions) if normalize_positions else np.asarray(positions, dtype=float)
        if pos.ndim != 2 or pos.shape[1] < 2:
            raise ValueError("positions must be a 2D array with at least 2 coordinates per channel.")
        if pos.shape[1] == 2:
            pos = np.column_stack([pos, np.zeros(pos.shape[0])])
        else:
            pos = pos[:, :3].copy()
        if pos.shape[0] == n_channels and np.isfinite(pos).any():
            ch_pos = {name: tuple(pos[idx, :3]) for idx, name in enumerate(ch_names)}
            montage = mne.channels.make_dig_montage(ch_pos=ch_pos, coord_frame="head")
            raw.set_montage(montage, on_missing="ignore")
            for idx, channel in enumerate(raw.info["chs"]):
                channel["loc"][:3] = pos[idx, :3]
                channel["loc"][3:] = 0.0

    if bads:
        raw.info["bads"] = list(bads)

    return raw


def interpolate_mne_bads(
    signals: np.ndarray,
    positions: np.ndarray,
    sfreq: float = 250.0,
    ch_names: List[str] | None = None,
    method: str = "MNE",
) -> np.ndarray:
    data = np.asarray(signals, dtype=float)
    missing = np.isnan(data)
    bad_indices = np.where(np.all(missing, axis=0))[0]
    bad_names = None if bad_indices.size == 0 else []

    if bad_indices.size != 0:
        if ch_names is None:
            bad_names = [f"EEG{idx:03d}" for idx in bad_indices]
        else:
            bad_names = [ch_names[idx] for idx in bad_indices]

    raw = _build_mne_eeg_raw(
        signals,
        positions=positions,
        sfreq=sfreq,
        ch_names=ch_names,
        bads=bad_names,
        normalize_positions=False,
    )

    if bad_indices.size == 0:
        return data.copy()

    try:
        raw_interp = raw.copy().interpolate_bads(
            reset_bads=False,
            method=method,
            origin="auto",
            verbose="ERROR",
        )
    except Exception:
        raw_interp = raw.copy().interpolate_bads(
            reset_bads=False,
            method="spline",
            origin="auto",
            verbose="ERROR",
        )

    reconstructed = raw_interp.get_data().T
    if bad_indices.size and np.allclose(reconstructed[:, bad_indices], 0.0, atol=1e-15, rtol=1e-12):
        raw_interp = raw.copy().interpolate_bads(
            reset_bads=False,
            method="spline",
            origin="auto",
            verbose="ERROR",
        )
        reconstructed = raw_interp.get_data().T

    reconstructed[~missing] = data[~missing]
    return reconstructed


def interpolate_signals(
    method: str,
    signals: np.ndarray,
    adjacency: np.ndarray = None,
    **kwargs,
) -> Dict[str, Any]:
    method = method.lower()

    if method == "linear":
        reconstructed = interpolate_linear(signals)
        return {"reconstructed": reconstructed, "info": {"method": "linear"}}

    if method == "gsp":
        if adjacency is None:
            raise ValueError("Se requiere matriz de adyacencia para interpolacion GSP.")
        reconstructed = interpolate_gsp(signals, adjacency)
        return {"reconstructed": reconstructed, "info": {"method": "gsp"}}

    if method == "nearest":
        reconstructed = interpolate_nearest(signals)
        return {"reconstructed": reconstructed, "info": {"method": "nearest"}}

    if method == "mean":
        reconstructed = interpolate_mean(signals)
        return {"reconstructed": reconstructed, "info": {"method": "mean"}}

    if method == "ica":
        n_components = kwargs.get("n_components", None)
        random_state = kwargs.get("random_state", 0)
        reconstructed, warn_list = interpolate_ica(signals, n_components=n_components, random_state=random_state)
        info: Dict[str, Any] = {"method": "ica", "n_components": n_components, "random_state": int(random_state)}
        if warn_list:
            info["warnings"] = warn_list
        return {"reconstructed": reconstructed, "info": info}

    if method in {"ica_mne", "mne_ica"}:
        positions = kwargs.get("positions")
        sfreq = float(kwargs.get("sfreq", 250.0))
        n_components = kwargs.get("n_components", None)
        random_state = int(kwargs.get("random_state", 0))
        ica_method = kwargs.get("ica_method", kwargs.get("method", "picard"))
        reconstructed, warn_list = interpolate_ica_mne(
            signals,
            positions=positions,
            sfreq=sfreq,
            n_components=n_components,
            random_state=random_state,
            method=str(ica_method).lower(),
        )
        info: Dict[str, Any] = {
            "method": "ica_mne",
            "n_components": n_components,
            "random_state": random_state,
            "sfreq": sfreq,
            "ica_method": str(ica_method).lower(),
        }
        if warn_list:
            info["warnings"] = warn_list
        return {"reconstructed": reconstructed, "info": info}

    if method in {"mne_bads", "mne_interpolate_bads", "mne_interpolate"}:
        positions = kwargs.get("positions")
        if positions is None:
            raise ValueError("Se requieren 'positions' para la interpolacion MNE de canales malos.")
        sfreq = float(kwargs.get("sfreq", 250.0))
        ch_names = kwargs.get("ch_names")
        interpolate_method = str(kwargs.get("interpolate_method", "MNE"))
        reconstructed = interpolate_mne_bads(
            signals,
            positions=positions,
            sfreq=sfreq,
            ch_names=ch_names,
            method=interpolate_method,
        )
        return {
            "reconstructed": reconstructed,
            "info": {"method": "mne_bads", "sfreq": sfreq, "interpolate_method": interpolate_method},
        }

    if method == "random":
        reconstructed = interpolate_random(signals)
        return {"reconstructed": reconstructed, "info": {"method": "random"}}

    if method == "idw":
        positions = kwargs.get("positions")
        power = float(kwargs.get("power", 2.0))
        reconstructed = interpolate_idw(signals, positions=positions, power=power)
        return {"reconstructed": reconstructed, "info": {"method": "idw", "power": power}}

    if method in {"tikhonov", "graph_tikhonov"}:
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para Tikhonov en grafo.")
        alpha = float(kwargs.get("alpha", 1.0))
        reconstructed = interpolate_tikhonov(signals, adjacency=adjacency, alpha=alpha)
        return {"reconstructed": reconstructed, "info": {"method": "tikhonov", "alpha": alpha}}

    if method in {"bgsrp", "bandlimited"}:
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para BGSRP.")
        bandwidth = int(kwargs.get("bandwidth", max(2, min(signals.shape[1] // 4, signals.shape[1] - 1))))
        gamma = float(kwargs.get("gamma", 0.1))
        strict_matlab = bool(kwargs.get("strict_matlab", False))
        reconstructed = interpolate_bgsrp(
            signals,
            adjacency=adjacency,
            bandwidth=bandwidth,
            gamma=gamma,
            strict_matlab=strict_matlab,
        )
        return {
            "reconstructed": reconstructed,
            "info": {"method": "bgsrp", "bandwidth": bandwidth, "gamma": gamma, "strict_matlab": strict_matlab},
        }

    if method in {"gsmooth", "graph_regularization"}:
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para gsmooth.")
        lam = float(kwargs.get("lam", 0.5))
        n_iter = int(kwargs.get("n_iter", 50))
        reconstructed = interpolate_gsmooth(signals, adjacency=adjacency, lam=lam, n_iter=n_iter)
        return {"reconstructed": reconstructed, "info": {"method": "gsmooth", "lam": lam, "n_iter": n_iter}}

    if method in {"graph_time_tikhonov", "gtt"}:
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para Graph-Time Tikhonov.")
        alpha = float(kwargs.get("alpha", 1.0))
        beta = float(kwargs.get("beta", 0.1))
        reconstructed = interpolate_graph_time_tikhonov(signals, adjacency=adjacency, alpha=alpha, beta=beta)
        return {
            "reconstructed": reconstructed,
            "info": {"method": "graph_time_tikhonov", "alpha": alpha, "beta": beta},
        }

    if method == "trss":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para TRSS.")
        alpha = float(kwargs.get("alpha", 0.8))
        beta = float(kwargs.get("beta", 0.15))
        n_iter = int(kwargs.get("n_iter", 120))
        lr = float(kwargs.get("lr", 0.05))
        reconstructed = interpolate_trss(
            signals,
            adjacency=adjacency,
            alpha=alpha,
            beta=beta,
            n_iter=n_iter,
            lr=lr,
        )
        return {
            "reconstructed": reconstructed,
            "info": {"method": "trss", "alpha": alpha, "beta": beta, "n_iter": n_iter},
        }

    if method in {"tv", "graph_tv"}:
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para TV en grafo.")
        lam = float(kwargs.get("lam", 0.2))
        n_iter = int(kwargs.get("n_iter", 30))
        eps = float(kwargs.get("eps", 1e-5))
        reconstructed = interpolate_graph_tv(signals, adjacency=adjacency, lam=lam, n_iter=n_iter, eps=eps)
        return {
            "reconstructed": reconstructed,
            "info": {"method": "tv", "lam": lam, "n_iter": n_iter},
        }

    if method == "sobolev_temporal":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para sobolev_temporal.")
        alpha = float(kwargs.get("alpha", 0.5))
        beta = float(kwargs.get("beta", 0.2))
        n_iter = int(kwargs.get("n_iter", 100))
        lr = float(kwargs.get("lr", 0.05))
        reconstructed = interpolate_sobolev_temporal(
            signals,
            adjacency=adjacency,
            alpha=alpha,
            beta=beta,
            n_iter=n_iter,
            lr=lr,
        )
        return {
            "reconstructed": reconstructed,
            "info": {"method": "sobolev_temporal", "alpha": alpha, "beta": beta, "n_iter": n_iter, "lr": lr},
        }

    if method == "temporal_laplacian":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para temporal_laplacian.")
        alpha = float(kwargs.get("alpha", 0.7))
        beta = float(kwargs.get("beta", 0.25))
        n_iter = int(kwargs.get("n_iter", 120))
        lr = float(kwargs.get("lr", 0.05))
        reconstructed = interpolate_temporal_laplacian(
            signals,
            adjacency=adjacency,
            alpha=alpha,
            beta=beta,
            n_iter=n_iter,
            lr=lr,
        )
        return {
            "reconstructed": reconstructed,
            "info": {"method": "temporal_laplacian", "alpha": alpha, "beta": beta, "n_iter": n_iter, "lr": lr},
        }

    if method == "heat_diffusion_temporal":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para heat_diffusion_temporal.")
        alpha = float(kwargs.get("alpha", 0.5))
        beta = float(kwargs.get("beta", 0.3))
        n_iter = int(kwargs.get("n_iter", 80))
        reconstructed = interpolate_heat_diffusion_temporal(signals, adjacency=adjacency, alpha=alpha, beta=beta, n_iter=n_iter)
        return {
            "reconstructed": reconstructed,
            "info": {"method": "heat_diffusion_temporal", "alpha": alpha, "beta": beta, "n_iter": n_iter},
        }

    if method == "spline_temporal":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para spline_temporal.")
        alpha = float(kwargs.get("alpha", 0.6))
        s_temporal = float(kwargs.get("s_temporal", 0.1))
        reconstructed = interpolate_spline_temporal(signals, adjacency=adjacency, alpha=alpha, s_temporal=s_temporal)
        return {
            "reconstructed": reconstructed,
            "info": {"method": "spline_temporal", "alpha": alpha, "s_temporal": s_temporal},
        }

    if method == "wavelet_temporal":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para wavelet_temporal.")
        alpha = float(kwargs.get("alpha", 0.65))
        wavelet_level = int(kwargs.get("wavelet_level", 2))
        reconstructed = interpolate_wavelet_temporal(signals, adjacency=adjacency, alpha=alpha, wavelet_level=wavelet_level)
        return {
            "reconstructed": reconstructed,
            "info": {"method": "wavelet_temporal", "alpha": alpha, "wavelet_level": wavelet_level},
        }

    if method == "directed_tv":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para directed_tv.")
        alpha = float(kwargs.get("alpha", 0.5))
        beta = float(kwargs.get("beta", 0.15))
        n_iter = int(kwargs.get("n_iter", 50))
        eps = float(kwargs.get("eps", 1e-5))
        reconstructed = interpolate_directed_tv(signals, adjacency=adjacency, alpha=alpha, beta=beta, n_iter=n_iter, eps=eps)
        return {
            "reconstructed": reconstructed,
            "info": {"method": "directed_tv", "alpha": alpha, "beta": beta, "n_iter": n_iter},
        }

    if method in {"adaptive_temporal", "visibility_graphs", "visibility_graph", "visibility_nnk"}:
        alpha = float(kwargs.get("alpha", 0.55))
        beta = float(kwargs.get("beta", 0.2))
        # Support legacy visibility_nnk parameters from schedules.
        gamma = float(kwargs.get("gamma", kwargs.get("visibility_threshold", 0.05)))
        n_iter = int(kwargs.get("n_iter", 100))
        reconstructed = interpolate_visibility_graphs(signals, adjacency=adjacency, alpha=alpha, beta=beta, gamma=gamma, n_iter=n_iter)
        return {
            "reconstructed": reconstructed,
            "info": {
                "method": "visibility_graphs",
                "requested_method": method,
                "alpha": alpha,
                "beta": beta,
                "gamma": gamma,
                "n_iter": n_iter,
            },
        }

    if method == "puy":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para Puy.")
        alpha = float(kwargs.get("alpha", 0.5))
        reconstructed = interpolate_puy(signals, adjacency=adjacency, alpha=alpha)
        return {"reconstructed": reconstructed, "info": {"method": "puy", "alpha": alpha}}

    if method == "sobolev":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para Sobolev.")
        alpha = float(kwargs.get("alpha", 1.0))
        order = int(kwargs.get("order", 2))
        reconstructed = interpolate_sobolev(signals, adjacency=adjacency, alpha=alpha, order=order)
        return {
            "reconstructed": reconstructed,
            "info": {"method": "sobolev", "alpha": alpha, "order": order},
        }

    if method in {"spherical_spline", "rbfi_tps", "rbfi_mq", "spline_surface"}:
        positions = kwargs.get("positions")
        if positions is None:
            raise ValueError("Se requieren 'positions' para interpoladores espaciales.")

        if method == "spherical_spline":
            eps = float(kwargs.get("eps", 1e-6))
            reconstructed = interpolate_spherical_spline(signals, positions=positions, eps=eps)
        elif method == "rbfi_tps":
            smooth = float(kwargs.get("smooth", 0.0))
            reconstructed = interpolate_rbfi(signals, positions=positions, function="thin_plate", smooth=smooth)
        elif method == "rbfi_mq":
            smooth = float(kwargs.get("smooth", 0.0))
            reconstructed = interpolate_rbfi(signals, positions=positions, function="multiquadric", smooth=smooth)
        else:
            reconstructed = interpolate_spline_surface(signals, positions=positions)

        return {"reconstructed": reconstructed, "info": {"method": method}}

    raise NotImplementedError(f"Metodo de interpolacion no implementado: {method}")


def interpolate_linear(signals: np.ndarray) -> np.ndarray:
    reconstructed = signals.copy()
    n_samples, n_channels = signals.shape

    for i in range(n_samples):
        row = signals[i]
        observed = ~np.isnan(row)
        if np.sum(observed) < 2:
            continue
        x = np.arange(n_channels)
        reconstructed[i] = np.interp(x, x[observed], row[observed])

    return reconstructed


def interpolate_nearest(signals: np.ndarray) -> np.ndarray:
    reconstructed = signals.copy()
    n_samples, n_channels = signals.shape

    for i in range(n_samples):
        row = signals[i]
        observed = ~np.isnan(row)
        if np.sum(observed) == 0:
            continue
        x = np.arange(n_channels)
        for idx in np.where(~observed)[0]:
            nearest = x[observed][np.argmin(np.abs(idx - x[observed]))]
            reconstructed[i, idx] = row[nearest]

    return reconstructed


def interpolate_mean(signals: np.ndarray) -> np.ndarray:
    reconstructed = signals.copy()
    n_samples = signals.shape[0]

    for i in range(n_samples):
        row = signals[i]
        observed = ~np.isnan(row)
        if np.sum(observed) == 0:
            continue
        reconstructed[i, ~observed] = np.mean(row[observed])

    return reconstructed


def interpolate_random(signals: np.ndarray, random_state: int = 42) -> np.ndarray:
    reconstructed = signals.copy()
    n_samples = signals.shape[0]
    rng = np.random.default_rng(random_state)

    for i in range(n_samples):
        row = signals[i]
        observed = ~np.isnan(row)
        if np.sum(observed) == 0:
            continue
        obs = row[observed]
        low = float(np.min(obs))
        high = float(np.max(obs))
        if low == high:
            reconstructed[i, ~observed] = low
            continue
        reconstructed[i, ~observed] = rng.uniform(low, high, size=np.sum(~observed))

    return reconstructed


def interpolate_ica(signals: np.ndarray, n_components: int | None = None, random_state: int = 0) -> Tuple[np.ndarray, List[Dict[str, str]]]:
    """
    ICA-based reconstruction baseline.

    Strategy:
    - Impute missing entries with channel-wise mean.
    - Fit FastICA across time (samples x channels).
    - Inverse-transform to obtain reconstructed signals and use reconstructed
      values for the originally-missing entries.

    This is a pragmatic baseline that provides a source-separation reconstruction
    without requiring external training data.
    """
    try:
        from sklearn.decomposition import FastICA
    except Exception:
        raise ImportError("scikit-learn is required for ICA interpolation. Install scikit-learn.")

    y = signals.astype(float)
    mask = ~np.isnan(y)
    n_t, n_ch = y.shape

    # Impute missing values with column mean for ICA fitting
    col_mean = _nanmean_no_warn(y, axis=0)
    x = y.copy()
    miss = ~mask
    x[miss] = np.take(col_mean, np.where(miss)[1])

    # Determine number of components
    if n_components is None:
        comp = min(n_ch, max(1, n_ch - 1))
    else:
        comp = int(min(int(n_components), n_ch))
    comp = max(1, min(comp, n_ch))
    if n_t <= comp:
        comp = max(1, min(n_t - 1, n_ch)) if n_t > 1 else 1

    try:
        # Retry strategy for unstable FastICA convergence.
        attempts = [
            {"n_components": comp, "max_iter": 10000, "tol": 1e-4},
            {"n_components": max(1, comp - 1), "max_iter": 20000, "tol": 1e-3},
        ]

        selected_warns: List[Dict[str, str]] = []
        x_rec_selected = None

        for attempt in attempts:
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                ica = FastICA(
                    n_components=int(attempt["n_components"]),
                    random_state=int(random_state),
                    max_iter=int(attempt["max_iter"]),
                    tol=float(attempt["tol"]),
                )
                s_comp = ica.fit_transform(x)
                x_rec_try = ica.inverse_transform(s_comp)

            warn_list: List[Dict[str, str]] = []
            has_convergence_warning = False
            for ww in w:
                cat = getattr(ww, "category", None)
                cat_name = cat.__name__ if cat is not None else "Warning"
                msg = str(ww.message)
                warn_list.append({"category": cat_name, "message": msg})
                if "ConvergenceWarning" in cat_name or "did not converge" in msg:
                    has_convergence_warning = True
                try:
                    record_warning(
                        "ica",
                        cat_name,
                        msg,
                        severity="warning",
                        decision="investigate",
                        context={
                            "n_components": int(attempt["n_components"]),
                            "n_t": n_t,
                            "n_ch": n_ch,
                            "random_state": int(random_state),
                            "max_iter": int(attempt["max_iter"]),
                            "tol": float(attempt["tol"]),
                        },
                    )
                except Exception:
                    pass

            selected_warns = warn_list
            x_rec_selected = x_rec_try
            if not has_convergence_warning:
                break

        if x_rec_selected is None:
            raise RuntimeError("ICA reconstruction failed without output matrix")

        # If convergence warning persists after retries, use a deterministic fallback.
        if any(("ConvergenceWarning" in w.get("category", "") or "did not converge" in w.get("message", "")) for w in selected_warns):
            reconstructed = interpolate_linear(y)
            return reconstructed, [{"category": "ConvergenceWarning", "message": "FastICA no convergio tras reintentos; se aplico fallback lineal."}]

        reconstructed = y.copy()
        reconstructed[miss] = x_rec_selected[miss]
        return reconstructed, selected_warns
    except Exception as exc:
        # Safe fallback: fill missing with column mean and record error
        try:
            record_warning("ica", "Exception", str(exc), severity="error", decision="fallback", context={"n_components": comp, "n_t": n_t, "n_ch": n_ch, "random_state": int(random_state)})
        except Exception:
            pass
        reconstructed = y.copy()
        reconstructed[miss] = np.take(col_mean, np.where(miss)[1])
        return reconstructed, [{"category": "Exception", "message": str(exc)}]


def interpolate_ica_mne(
    signals: np.ndarray,
    positions: np.ndarray | None = None,
    sfreq: float = 250.0,
    n_components: int | None = None,
    random_state: int = 0,
    method: str = "picard",
) -> Tuple[np.ndarray, List[Dict[str, str]]]:
    try:
        from mne.preprocessing import ICA
    except Exception:
        return interpolate_ica(signals, n_components=n_components, random_state=random_state)

    data = np.asarray(signals, dtype=float)
    missing_mask = np.isnan(data)
    if not missing_mask.any():
        return data.copy(), []

    n_times, n_channels = data.shape
    if n_components is None:
        comp = min(n_channels, max(1, n_channels - 1))
    else:
        comp = int(min(int(n_components), n_channels))
    comp = max(1, min(comp, n_channels))
    if n_times <= comp:
        comp = max(1, min(n_times - 1, n_channels)) if n_times > 1 else 1

    bad_indices = np.where(np.all(missing_mask, axis=0))[0]
    bad_names = None if bad_indices.size == 0 else [f"EEG{idx:03d}" for idx in bad_indices]
    raw = _build_mne_eeg_raw(
        data,
        positions=positions,
        sfreq=sfreq,
        bads=bad_names,
        normalize_positions=False,
    )
    if method == "auto":
        candidate_methods = ["picard", "infomax", "fastica"]
    else:
        candidate_methods = [method, "picard", "infomax", "fastica"]

    ordered_methods: List[str] = []
    seen_methods: set[str] = set()
    for candidate in candidate_methods:
        if candidate not in seen_methods:
            ordered_methods.append(candidate)
            seen_methods.add(candidate)

    last_error: Exception | None = None
    for candidate in ordered_methods:
        try:
            fit_params = {"extended": True} if candidate == "infomax" else None
            ica = ICA(
                n_components=comp,
                random_state=random_state,
                method=candidate,
                fit_params=fit_params,
                max_iter="auto",
            )
            ica.fit(raw, picks="eeg", reject_by_annotation=False, verbose="ERROR")
            reconstructed_raw = ica.apply(raw.copy(), exclude=[], n_pca_components=comp, verbose="ERROR")
            if bad_names:
                reconstructed_raw.info["bads"] = list(bad_names)
                try:
                    reconstructed_raw = reconstructed_raw.interpolate_bads(
                        reset_bads=False,
                        method="MNE",
                        origin="auto",
                        verbose="ERROR",
                    )
                except Exception:
                    reconstructed_raw = reconstructed_raw.interpolate_bads(
                        reset_bads=False,
                        method="spline",
                        origin="auto",
                        verbose="ERROR",
                    )
            reconstructed = reconstructed_raw.get_data().T
            reconstructed[~missing_mask] = data[~missing_mask]
            return reconstructed, [
                {
                    "category": "Info",
                    "message": f"MNE ICA backend used method={candidate!r} with n_components={comp}.",
                }
            ]
        except Exception as exc:
            last_error = exc

    fallback_reconstructed, fallback_warnings = interpolate_ica(signals, n_components=comp, random_state=random_state)
    fallback_warnings.append(
        {
            "category": "Warning",
            "message": f"MNE ICA backend failed, falling back to sklearn FastICA. Last error: {last_error}",
        }
    )
    return fallback_reconstructed, fallback_warnings


def interpolate_idw(signals: np.ndarray, positions: np.ndarray = None, power: float = 2.0) -> np.ndarray:
    if positions is None:
        raise ValueError("Se requieren 'positions' para interpolacion IDW.")

    reconstructed = signals.copy()
    dists = np.linalg.norm(positions[:, None, :] - positions[None, :, :], axis=2)
    np.fill_diagonal(dists, np.inf)
    n_samples = signals.shape[0]

    for i in range(n_samples):
        row = signals[i].copy()
        observed = ~np.isnan(row)
        missing_idx = np.where(~observed)[0]
        observed_idx = np.where(observed)[0]
        if observed_idx.size == 0:
            continue

        for m in missing_idx:
            d = dists[m, observed_idx]
            d = np.maximum(d, 1e-12)
            w = 1.0 / np.power(d, power)
            w_sum = np.sum(w)
            if w_sum == 0:
                continue
            row[m] = float(np.dot(w, row[observed_idx]) / w_sum)

        reconstructed[i] = row

    return reconstructed


def interpolate_gsp(signals: np.ndarray, adjacency: np.ndarray) -> np.ndarray:
    from scipy.sparse import csgraph

    reconstructed = signals.copy()
    laplacian = csgraph.laplacian(adjacency, normed=False)
    n_samples = signals.shape[0]

    for i in range(n_samples):
        y = signals[i]
        observed = ~np.isnan(y)
        if np.all(observed):
            continue

        known_idx = np.where(observed)[0]
        unknown_idx = np.where(~observed)[0]
        if known_idx.size == 0:
            continue

        l_uu = laplacian[np.ix_(unknown_idx, unknown_idx)]
        l_uk = laplacian[np.ix_(unknown_idx, known_idx)]
        y_known = y[known_idx]

        try:
            x = np.linalg.solve(l_uu, -l_uk @ y_known)
            y_rec = y.copy()
            y_rec[unknown_idx] = x
            reconstructed[i] = y_rec
        except np.linalg.LinAlgError:
            # Fallback estable cuando el sistema es singular.
            mean_val = np.nanmean(y)
            reconstructed[i, unknown_idx] = mean_val

    return reconstructed


def _graph_tikhonov_single(y: np.ndarray, laplacian: np.ndarray, alpha: float) -> np.ndarray:
    n_channels = y.shape[0]
    observed = ~np.isnan(y)
    if np.all(observed):
        return y.copy()
    if not np.any(observed):
        return np.zeros_like(y)

    m = np.diag(observed.astype(float))
    b = np.nan_to_num(y, nan=0.0)
    a = m + alpha * laplacian
    try:
        return np.linalg.solve(a, m @ b)
    except np.linalg.LinAlgError:
        y_fallback = y.copy()
        y_fallback[~observed] = np.nanmean(y)
        return np.nan_to_num(y_fallback, nan=0.0)


def interpolate_tikhonov(signals: np.ndarray, adjacency: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    from scipy.sparse import csgraph

    laplacian = csgraph.laplacian(adjacency, normed=False)
    reconstructed = np.zeros_like(signals)
    for i in range(signals.shape[0]):
        reconstructed[i] = _graph_tikhonov_single(signals[i], laplacian, alpha=alpha)
    return reconstructed


def interpolate_bgsrp(
    signals: np.ndarray,
    adjacency: np.ndarray,
    bandwidth: int = 8,
    gamma: float = 0.1,
    reg: float = 1e-8,
    strict_matlab: bool = False,
) -> np.ndarray:
    from scipy.sparse import csgraph

    a = np.asarray(adjacency, dtype=float)
    a = np.nan_to_num(a, nan=0.0, posinf=0.0, neginf=0.0)
    a = np.maximum(a, a.T)
    np.fill_diagonal(a, 0.0)

    laplacian = csgraph.laplacian(a, normed=False)
    evals, evecs = np.linalg.eigh(laplacian)

    # RKHS BGSRP usa base bandlimited excluyendo componente DC.
    n_nodes = evecs.shape[0]
    if n_nodes < 3:
        return np.nan_to_num(signals, nan=0.0)
    n = int(np.clip(bandwidth, 2, n_nodes - 1))
    u_n = evecs[:, 1:n]
    mu_n = evals[1:n]
    mu_n = np.nan_to_num(mu_n, nan=reg, posinf=reg, neginf=reg)
    if not strict_matlab:
        mu_n = np.maximum(mu_n, reg)
    mu_n = np.where(np.abs(mu_n) < reg, reg, mu_n)
    phi_n = np.diag(1.0 / mu_n)

    reconstructed = signals.copy()
    for i in range(signals.shape[0]):
        y = signals[i]
        observed = ~np.isnan(y)
        if np.all(observed):
            continue
        if np.sum(observed) < 1:
            reconstructed[i] = np.zeros_like(y)
            continue

        x0 = np.where(observed)[0]
        y0 = y[x0]
        ell = x0.size

        b_mat = u_n[x0, :]
        a_center = np.eye(ell) - np.ones((ell, ell), dtype=float) / float(ell)

        try:
            core = phi_n @ (b_mat.T @ a_center @ b_mat) @ phi_n
            g_mat = b_mat @ (gamma * phi_n + core) @ b_mat.T
            d_vec = b_mat @ phi_n @ b_mat.T @ a_center @ y0

            if strict_matlab:
                xi = _pinv_matlab(g_mat) @ d_vec
            else:
                xi = np.linalg.pinv(g_mat + reg * np.eye(ell)) @ d_vec
            g_vec = u_n @ phi_n @ b_mat.T @ xi

            # Termino constante z de la formulacion original.
            z = -np.sum(g_vec[x0] - y0) / float(ell)
            x_rec = g_vec + z
            x_rec = np.nan_to_num(x_rec, nan=0.0, posinf=0.0, neginf=0.0)
            x_rec[observed] = y[observed]

            scale = np.nanstd(y)
            if not np.isfinite(scale) or scale <= 0:
                scale = 1.0
            x_rec = np.clip(x_rec, -8.0 * scale, 8.0 * scale)
            reconstructed[i] = x_rec
        except Exception:
            y_fallback = y.copy()
            y_fallback[~observed] = _nanmean_no_warn(y)
            reconstructed[i] = np.nan_to_num(y_fallback, nan=0.0)

    return reconstructed


def interpolate_gsmooth(signals: np.ndarray, adjacency: np.ndarray, lam: float = 0.5, n_iter: int = 50) -> np.ndarray:
    degree = np.sum(adjacency, axis=1)
    degree_safe = np.where(degree > 0, degree, 1.0)
    p = adjacency / degree_safe[:, None]

    reconstructed = signals.copy()
    for i in range(signals.shape[0]):
        y = signals[i].copy()
        observed = ~np.isnan(y)
        if np.all(observed):
            continue
        y[~observed] = np.nanmean(y)

        x = y.copy()
        for _ in range(n_iter):
            x = (1.0 - lam) * y + lam * (p @ x)
            x[observed] = y[observed]
        reconstructed[i] = x

    return reconstructed


def interpolate_graph_time_tikhonov(
    signals: np.ndarray,
    adjacency: np.ndarray,
    alpha: float = 1.0,
    beta: float = 0.1,
) -> np.ndarray:
    # Primera etapa: Tikhonov en grafo por instante.
    x = interpolate_tikhonov(signals, adjacency=adjacency, alpha=alpha)

    # Segunda etapa: suavizado temporal en cada canal.
    smoothed = x.copy()
    for ch in range(x.shape[1]):
        series = x[:, ch]
        out = series.copy()
        for t in range(1, len(series) - 1):
            out[t] = (series[t] + beta * (series[t - 1] + series[t + 1])) / (1.0 + 2.0 * beta)
        smoothed[:, ch] = out
    return smoothed


def interpolate_trss(
    signals: np.ndarray,
    adjacency: np.ndarray,
    alpha: float = 0.8,
    beta: float = 0.15,
    n_iter: int = 120,
    lr: float = 0.05,
) -> np.ndarray:
    """
    GraphTRSS paper-faithful (Giraldo et al. 2022, aproximacion por gradiente):
    min_X ||M o (X-Y)||_F^2 + alpha * tr(X L_g X^T) + beta * tr((D X) L_g (D X)^T)
    con restricciones duras en observaciones M.
    """
    from scipy.sparse import csgraph

    y = signals.astype(float)
    mask = ~np.isnan(y)
    x = y.copy()

    # Inicializacion para faltantes.
    col_mean = _nanmean_no_warn(x, axis=0)
    miss = ~mask
    x[miss] = np.take(col_mean, np.where(miss)[1])

    lap_g = csgraph.laplacian(adjacency, normed=False)
    t = x.shape[0]
    d = np.zeros((max(t - 1, 1), t), dtype=float)
    if t > 1:
        idx = np.arange(t - 1)
        d[idx, idx] = -1.0
        d[idx, idx + 1] = 1.0
    lap_t = d.T @ d

    # Paso adaptativo basado en cota de Lipschitz aproximada para
    # grad(X) = 2 M o (X-Y) + 2 alpha X L_g + 2 beta L_t X L_g.
    norm_lg = np.linalg.norm(lap_g, ord=2)
    norm_lt = np.linalg.norm(lap_t, ord=2)
    lipschitz = 2.0 * (1.0 + alpha * norm_lg + beta * norm_lt * norm_lg)
    step = min(lr, 1.0 / max(lipschitz, 1e-8))

    scale = np.nanstd(y)
    if not np.isfinite(scale) or scale <= 0:
        scale = 1.0
    clip_bound = 8.0 * scale

    for _ in range(n_iter):
        grad_data = (x - np.nan_to_num(y, nan=0.0)) * mask
        grad_graph = x @ lap_g
        # Termino Sobolev temporal en grafo: D^T D X L_g = L_t X L_g.
        grad_sobolev = (lap_t @ x) @ lap_g
        grad = 2.0 * grad_data + 2.0 * alpha * grad_graph + 2.0 * beta * grad_sobolev

        x = x - step * grad
        x = np.clip(x, -clip_bound, clip_bound)
        x[mask] = y[mask]

    return x


# Backwards compatibility alias (legacy name)
# (moved to end of file after function definition to avoid forward-reference)


def interpolate_graph_tv(
    signals: np.ndarray,
    adjacency: np.ndarray,
    lam: float = 0.2,
    n_iter: int = 30,
    eps: float = 1e-5,
) -> np.ndarray:
    """
    TV en grafo via IRLS: aproxima ||grad_G x||_1 con pesos reponderados.
    """
    from scipy.sparse import csgraph

    y = signals.astype(float)
    mask = ~np.isnan(y)
    x = y.copy()
    col_mean = _nanmean_no_warn(x, axis=0)
    miss = ~mask
    x[miss] = np.take(col_mean, np.where(miss)[1])

    # Lista de aristas ponderadas.
    a = np.asarray(adjacency, dtype=float)
    n = a.shape[0]
    edges = np.argwhere(np.triu(a, k=1) > 0)
    w_edge = a[edges[:, 0], edges[:, 1]]

    for _ in range(n_iter):
        # Laplaciano reponderado para TV (IRLS).
        l_tv = np.zeros((n, n), dtype=float)
        for e_idx, (i, j) in enumerate(edges):
            diff = x[:, i] - x[:, j]
            avg_scale = np.mean(1.0 / np.sqrt(diff**2 + eps))
            wij = w_edge[e_idx] * avg_scale
            l_tv[i, i] += wij
            l_tv[j, j] += wij
            l_tv[i, j] -= wij
            l_tv[j, i] -= wij

        for t_idx in range(x.shape[0]):
            obs = mask[t_idx]
            m = np.diag(obs.astype(float))
            b = np.nan_to_num(y[t_idx], nan=0.0)
            a_sys = m + lam * l_tv
            try:
                x[t_idx] = np.linalg.solve(a_sys, m @ b)
            except np.linalg.LinAlgError:
                x[t_idx, ~obs] = np.nanmean(y[t_idx])

        x[mask] = y[mask]

    return x


def interpolate_puy(signals: np.ndarray, adjacency: np.ndarray, alpha: float = 0.5) -> np.ndarray:
    # Aproximacion armonica regularizada sobre el grafo.
    from scipy.sparse import csgraph

    laplacian = csgraph.laplacian(adjacency, normed=False)
    reconstructed = signals.copy()
    for i in range(signals.shape[0]):
        y = signals[i]
        observed = ~np.isnan(y)
        if np.all(observed):
            continue
        m = np.diag(observed.astype(float))
        b = np.nan_to_num(y, nan=0.0)
        a = m + alpha * (laplacian.T @ laplacian)
        try:
            reconstructed[i] = np.linalg.solve(a, m @ b)
        except np.linalg.LinAlgError:
            reconstructed[i, ~observed] = np.nanmean(y)
    return reconstructed


def interpolate_sobolev(
    signals: np.ndarray,
    adjacency: np.ndarray,
    alpha: float = 1.0,
    order: int = 2,
) -> np.ndarray:
    from scipy.sparse import csgraph

    laplacian = csgraph.laplacian(adjacency, normed=False)
    reg = np.eye(laplacian.shape[0]) + laplacian
    reg_power = np.linalg.matrix_power(reg, max(1, order))

    reconstructed = signals.copy()
    for i in range(signals.shape[0]):
        y = signals[i]
        observed = ~np.isnan(y)
        m = np.diag(observed.astype(float))
        b = np.nan_to_num(y, nan=0.0)
        a = m + alpha * reg_power
        try:
            reconstructed[i] = np.linalg.solve(a, m @ b)
        except np.linalg.LinAlgError:
            reconstructed[i, ~observed] = np.nanmean(y)
    return reconstructed


def _rbf_per_row(signals: np.ndarray, positions: np.ndarray, function: str, smooth: float = 0.0) -> np.ndarray:
    x = positions[:, 0]
    y = positions[:, 1]
    z = positions[:, 2] if positions.shape[1] > 2 else np.zeros_like(x)

    reconstructed = signals.copy()
    for i in range(signals.shape[0]):
        row = signals[i]
        observed = ~np.isnan(row)
        if np.sum(observed) < 3:
            reconstructed[i, ~observed] = np.nanmean(row)
            continue
        try:
            rbf = Rbf(x[observed], y[observed], z[observed], row[observed], function=function, smooth=smooth)
            reconstructed[i, ~observed] = rbf(x[~observed], y[~observed], z[~observed])
        except Exception:
            reconstructed[i, ~observed] = np.nanmean(row)
    return reconstructed


def interpolate_spherical_spline(signals: np.ndarray, positions: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    # Implementacion tipo Perrin et al. para spherical splines EEG.
    pos = positions.copy().astype(float)
    norm = np.linalg.norm(pos, axis=1, keepdims=True)
    norm = np.where(norm == 0, 1.0, norm)
    pos = pos / norm

    n_channels = pos.shape[0]
    cos_matrix = np.clip(pos @ pos.T, -1.0, 1.0)

    m_order = 4
    n_terms = 50

    g_matrix = _perrin_g(cos_matrix, m=m_order, n_terms=n_terms)
    a = np.zeros((n_channels + 4, n_channels + 4), dtype=float)
    a[:n_channels, :n_channels] = g_matrix + eps * np.eye(n_channels)
    a[:n_channels, n_channels] = 1.0
    a[:n_channels, n_channels + 1 : n_channels + 4] = pos
    a[n_channels, :n_channels] = 1.0
    a[n_channels + 1 : n_channels + 4, :n_channels] = pos.T

    reconstructed = signals.copy().astype(float)

    for i in range(signals.shape[0]):
        row = signals[i].astype(float)
        observed = ~np.isnan(row)
        missing = ~observed
        if np.sum(missing) == 0:
            continue
        if np.sum(observed) < 4:
            reconstructed[i, missing] = np.nanmean(row)
            continue

        obs_idx = np.where(observed)[0]
        miss_idx = np.where(missing)[0]

        a_obs = np.zeros((obs_idx.size + 4, obs_idx.size + 4), dtype=float)
        g_obs = g_matrix[np.ix_(obs_idx, obs_idx)]
        pos_obs = pos[obs_idx]

        a_obs[: obs_idx.size, : obs_idx.size] = g_obs + eps * np.eye(obs_idx.size)
        a_obs[: obs_idx.size, obs_idx.size] = 1.0
        a_obs[: obs_idx.size, obs_idx.size + 1 : obs_idx.size + 4] = pos_obs
        a_obs[obs_idx.size, : obs_idx.size] = 1.0
        a_obs[obs_idx.size + 1 : obs_idx.size + 4, : obs_idx.size] = pos_obs.T

        b = np.zeros(obs_idx.size + 4, dtype=float)
        b[: obs_idx.size] = row[obs_idx]

        try:
            coeff = np.linalg.solve(a_obs, b)
        except np.linalg.LinAlgError:
            reconstructed[i, missing] = np.nanmean(row)
            continue

        lam = coeff[: obs_idx.size]
        c0 = coeff[obs_idx.size]
        c_xyz = coeff[obs_idx.size + 1 : obs_idx.size + 4]

        cos_mo = np.clip(pos[miss_idx] @ pos_obs.T, -1.0, 1.0)
        g_mo = _perrin_g(cos_mo, m=m_order, n_terms=n_terms)
        pred = g_mo @ lam + c0 + pos[miss_idx] @ c_xyz
        reconstructed[i, miss_idx] = pred

    return reconstructed


def _perrin_g(cos_theta: np.ndarray, m: int = 4, n_terms: int = 50) -> np.ndarray:
    """
    Función de Green para spherical spline EEG (Perrin).
    """
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    g = np.zeros_like(cos_theta, dtype=float)
    for n in range(1, n_terms + 1):
        coeff = (2 * n + 1) / ((n**m) * ((n + 1) ** m))
        p_n = lpmv(0, n, cos_theta)
        g += coeff * p_n
    return g / (4.0 * np.pi)


def interpolate_sobolev_temporal(
    signals: np.ndarray,
    adjacency: np.ndarray,
    alpha: float = 0.5,
    beta: float = 0.2,
    n_iter: int = 100,
    lr: float = 0.05,
) -> np.ndarray:
    """
    Alias de GraphTRSS (misma formulacion que interpolate_trss).
    """
    return interpolate_trss(
        signals,
        adjacency=adjacency,
        alpha=alpha,
        beta=beta,
        n_iter=n_iter,
        lr=lr,
    )


def interpolate_temporal_laplacian(
    signals: np.ndarray,
    adjacency: np.ndarray,
    alpha: float = 0.7,
    beta: float = 0.25,
    n_iter: int = 120,
    lr: float = 0.05,
    clip_factor: float = 8.0,
) -> np.ndarray:
    """
    Product graph: combined spatial-temporal Laplacian.
    Interpola resolviendo min ||x - y||_M + alpha * x'Lx + beta * x'L_t x
    donde L_t es el Laplaciano temporal.
    """
    from scipy.sparse import csgraph

    y = signals.astype(float)
    mask = ~np.isnan(y)
    n_t, n_ch = y.shape

    a = np.asarray(adjacency, dtype=float)
    a = np.nan_to_num(a, nan=0.0, posinf=0.0, neginf=0.0)
    a = np.maximum(a, a.T)
    np.fill_diagonal(a, 0.0)
    lap_g = csgraph.laplacian(a, normed=False)

    # Laplaciano temporal (primeras diferencias)
    l_temp = np.zeros((n_t, n_t), dtype=float)
    if n_t > 1:
        idx = np.arange(n_t - 1)
        l_temp[idx, idx] += 1.0
        l_temp[idx, idx + 1] -= 1.0
        l_temp[idx + 1, idx] -= 1.0
        l_temp[idx + 1, idx + 1] += 1.0

    reconstructed = y.copy()
    col_mean = _nanmean_no_warn(y, axis=0)
    miss = ~mask
    reconstructed[miss] = np.take(col_mean, np.where(miss)[1])

    norm_lg = np.linalg.norm(lap_g, ord=2)
    norm_lt = np.linalg.norm(l_temp, ord=2)
    lipschitz = 2.0 * (1.0 + alpha * norm_lg + beta * norm_lt)
    step = min(lr, 1.0 / max(lipschitz, 1e-8))

    scale = np.nanstd(y)
    if not np.isfinite(scale) or scale <= 0:
        scale = 1.0
    bound = float(clip_factor) * scale

    y_safe = np.nan_to_num(y, nan=0.0)
    for _ in range(max(1, int(n_iter))):
        grad_data = (reconstructed - y_safe) * mask
        grad_spatial = reconstructed @ lap_g
        grad_temporal = l_temp @ reconstructed
        grad = 2.0 * grad_data + 2.0 * alpha * grad_spatial + 2.0 * beta * grad_temporal
        reconstructed = reconstructed - step * grad
        reconstructed = np.clip(reconstructed, -bound, bound)
        reconstructed[mask] = y[mask]

    return reconstructed


def interpolate_heat_diffusion_temporal(
    signals: np.ndarray,
    adjacency: np.ndarray,
    alpha: float = 0.5,
    beta: float = 0.3,
    n_iter: int = 80,
) -> np.ndarray:
    """
    Heat kernel diffusion: combina difusión espacial y temporal.
    x(t+1) = x(t) - step*(grad spatial + grad temporal).
    """
    from scipy.sparse import csgraph

    y = signals.astype(float)
    mask = ~np.isnan(y)
    x = y.copy()
    col_mean = np.nanmean(x, axis=0)
    col_mean = np.where(np.isnan(col_mean), 0.0, col_mean)
    miss = ~mask
    x[miss] = np.take(col_mean, np.where(miss)[1])

    lap_g = csgraph.laplacian(adjacency, normed=False)
    
    # Operador de difusión temporal: kernel de calor discreto
    t = x.shape[0]
    heat_t = np.zeros((t, t), dtype=float)
    for i in range(t):
        for j in range(t):
            heat_t[i, j] = np.exp(-0.1 * (i - j) ** 2)
    
    scale = np.nanstd(y)
    if not np.isfinite(scale) or scale <= 0:
        scale = 1.0

    step = 0.03
    
    for _ in range(n_iter):
        # Gradiente espacial
        grad_spatial = x @ lap_g
        
        # Gradiente temporal vía kernel de calor
        grad_temporal = (heat_t @ x - x)
        
        # Gradiente de datos
        grad_data = 2.0 * (x - np.nan_to_num(y, nan=0.0)) * mask
        
        grad = grad_data + alpha * grad_spatial + beta * grad_temporal
        
        x = x - step * grad
        x = np.clip(x, -8.0 * scale, 8.0 * scale)
        x[mask] = y[mask]

    return x


def interpolate_spline_temporal(
    signals: np.ndarray,
    adjacency: np.ndarray,
    alpha: float = 0.6,
    s_temporal: float = 0.1,
) -> np.ndarray:
    """
    Spline-based temporal smoothing con regularizacion espacial.
    Para cada canal: ajusta spline temporal con peso de Tikhonov espacial.
    """
    from scipy.sparse import csgraph
    from scipy.interpolate import UnivariateSpline

    y = signals.astype(float)
    mask = ~np.isnan(y)
    lap_g = csgraph.laplacian(adjacency, normed=False)
    
    n_t, n_ch = y.shape
    x = np.zeros_like(y)

    for ch in range(n_ch):
        series = y[:, ch]
        obs = mask[:, ch]
        
        if np.sum(obs) < 3:
            x[obs, ch] = series[obs]
            x[~obs, ch] = np.nanmean(series)
            continue
        
        t_obs = np.where(obs)[0]
        t_all = np.arange(n_t)
        
        try:
            # Spline univariado suavizado
            spl = UnivariateSpline(t_obs, series[obs], k=min(3, np.sum(obs) - 1), s=s_temporal * np.sum(obs))
            x[:, ch] = spl(t_all)
        except Exception:
            x[obs, ch] = series[obs]
            x[~obs, ch] = np.nanmean(series)

    # Regulariacion espacial post-spline
    for t_idx in range(n_t):
        obs = mask[t_idx]
        m = np.diag(obs.astype(float))
        b = np.nan_to_num(y[t_idx], nan=0.0)
        a = m + alpha * lap_g
        try:
            x[t_idx] = np.linalg.solve(a, m @ b + alpha * lap_g @ x[t_idx])
        except np.linalg.LinAlgError:
            x[t_idx, ~obs] = np.nanmean(y[t_idx])

    return x


def interpolate_wavelet_temporal(
    signals: np.ndarray,
    adjacency: np.ndarray,
    alpha: float = 0.65,
    wavelet_level: int = 2,
) -> np.ndarray:
    """
    Wavelet filtering en dimension temporal + regulariacion espacial.
    Usa transformada wavelet discreta (Haar) en cada canal.
    """
    from scipy.sparse import csgraph

    y = signals.astype(float)
    mask = ~np.isnan(y)
    lap_g = csgraph.laplacian(adjacency, normed=False)
    
    n_t, n_ch = y.shape
    x = y.copy()
    col_mean = np.nanmean(x, axis=0)
    col_mean = np.where(np.isnan(col_mean), 0.0, col_mean)
    miss = ~mask
    x[miss] = np.take(col_mean, np.where(miss)[1])

    # Simple Haar wavelet-like filtering: pasa-altos y pasa-bajos
    for ch in range(n_ch):
        series = x[:, ch].copy()
        
        for level in range(wavelet_level):
            if len(series) < 2:
                break
            # Decomposición Haar simple
            approx = series.copy()
            for i in range(0, len(series) - 1, 2):
                if i + 1 < len(series):
                    approx[i] = 0.5 * (series[i] + series[i + 1])
            approx = approx[: len(series) // 2 + len(series) % 2]
            series = approx

        # Reconstrucción suavizada
        for i in range(min(len(series), n_t)):
            x[i, ch] = series[i] if i < len(series) else x[i, ch]

    # Regulariacion espacial
    for t_idx in range(n_t):
        obs = mask[t_idx]
        m = np.diag(obs.astype(float))
        b = np.nan_to_num(y[t_idx], nan=0.0)
        a = m + alpha * lap_g
        try:
            x[t_idx] = np.linalg.solve(a, m @ b + alpha * lap_g @ x[t_idx])
        except np.linalg.LinAlgError:
            x[t_idx, ~obs] = np.nanmean(y[t_idx])

    return x


def interpolate_directed_tv(
    signals: np.ndarray,
    adjacency: np.ndarray,
    alpha: float = 0.5,
    beta: float = 0.15,
    n_iter: int = 50,
    eps: float = 1e-5,
) -> np.ndarray:
    """
    Directed Total Variation (Schultz & Villafane-Delgado 2020):
    Extiende TV a grafos dirigidos usando variación direccional.
    """
    from scipy.sparse import csgraph

    y = signals.astype(float)
    mask = ~np.isnan(y)
    x = y.copy()
    col_mean = np.nanmean(x, axis=0)
    col_mean = np.where(np.isnan(col_mean), 0.0, col_mean)
    miss = ~mask
    x[miss] = np.take(col_mean, np.where(miss)[1])

    # Versión simétrica del Laplaciano para dirigida
    a_sym = np.asarray(adjacency, dtype=float)
    a_asym = a_sym + 0.1 * a_sym.T  # Añade pequeña asimetría
    
    lap_g = csgraph.laplacian(a_asym, normed=False)
    
    # Laplaciano temporal
    t = x.shape[0]
    d = np.zeros((max(t - 1, 1), t), dtype=float)
    if t > 1:
        idx = np.arange(t - 1)
        d[idx, idx] = -1.0
        d[idx, idx + 1] = 1.0
    lap_t = d.T @ d

    for _ in range(n_iter):
        # IRLS para TV dirigida
        edges = np.argwhere(a_asym > 0)
        weights = a_asym[edges[:, 0], edges[:, 1]]
        
        l_tv = np.zeros_like(lap_g)
        for (i, j), w in zip(edges, weights):
            diff = np.linalg.norm(x[:, i] - x[:, j], axis=0)
            w_ij = w / (np.sqrt(diff**2 + eps) + 1e-12)
            l_tv[i, i] += w_ij
            l_tv[j, j] += w_ij
            l_tv[i, j] -= w_ij
            l_tv[j, i] -= w_ij

        for t_idx in range(x.shape[0]):
            obs = mask[t_idx]
            m = np.diag(obs.astype(float))
            b = np.nan_to_num(y[t_idx], nan=0.0)
            a = m + alpha * l_tv + beta * lap_t[t_idx, t_idx]
            try:
                x[t_idx] = np.linalg.solve(a + 1e-8 * np.eye(a.shape[0]), m @ b)
            except np.linalg.LinAlgError:
                x[t_idx, ~obs] = np.nanmean(y[t_idx])

        x[mask] = y[mask]

    return x


def interpolate_visibility_graphs(
    signals: np.ndarray,
    adjacency: np.ndarray = None,
    alpha: float = 0.55,
    beta: float = 0.2,
    gamma: float = 0.05,
    n_iter: int = 100,
) -> np.ndarray:
    """
    Visibility graphs + NNK reconstruction (Bozkurt & Ortega 2022).

    Procedimiento (alto nivel):
    1) Construir visibility graphs (NVG/HVG) por timesteps / ventanas.
    2) Extraer características por nodo (grado, clustering) y construir matriz
       de similitud temporal/entre-instantes.
    3) Usar NNK (non-negative kernel) sobre la matriz de similitud para
       construir pesos adaptativos y aplicar suavizado espacio-temporal.

    Nota: esta implementación mantiene la interfaz y parámetros previos para
    compatibilidad, y devuelve el resultado con el método canonical `visibility_graphs`.
    """
    # Parámetros adicionales (compatibilidad hacia atrás: se pueden pasar via kwargs)
    # k: número de vecinos candidatos para NNK
    # use_hvg: si True usa Horizontal Visibility Graph (más estable y simple)
    # nnk_reg: regularización para el solver NNK
    # trss_lr: learning rate para TRSS (si se usa como reconstructor)
    k = int(getattr(interpolate_visibility_graphs, "_default_k", 4))
    use_hvg = True
    nnk_reg = 1e-6
    trss_lr = 0.05

    # If caller didn't provide an adjacency, try using the graph constructor
    # `build_graph('visibility_nnk')` implemented in src.graph_construction.
    if adjacency is None:
        try:
            from src.graph_construction.graph_constructors import build_graph

            bg = build_graph("visibility_nnk", positions=None, signals=signals, k=k, use_hvg=use_hvg, reg=nnk_reg)
            adjacency_bg = bg.get("adjacency") if isinstance(bg, dict) else None
            if adjacency_bg is not None:
                try:
                    return interpolate_trss(signals.astype(float), adjacency=adjacency_bg, alpha=alpha, beta=beta, n_iter=n_iter, lr=trss_lr)
                except Exception:
                    # If TRSS fails on the constructed adjacency, fall back to internal routine
                    pass
        except Exception as exc:
            try:
                record_warning("visibility_graphs", "build_graph_failed", str(exc), severity="warning", decision="fallback")
            except Exception:
                pass

    from pathlib import Path
    import importlib.util
    from scipy.spatial.distance import cdist
    from scipy.sparse import csgraph

    y = signals.astype(float)
    n_t, n_ch = y.shape

    # Trivial fallback si dimensiones demasiado pequeñas
    if n_ch < 2 or n_t < 3:
        recon = y.copy()
        col_mean = _nanmean_no_warn(recon, axis=0)
        miss = np.isnan(recon)
        recon[miss] = np.take(col_mean, np.where(miss)[1])
        return recon

    def _hvg_adjacency(series: np.ndarray) -> np.ndarray:
        # Horizontal Visibility Graph (HVG): conectividad simple y robusta
        s = series.astype(float)
        n = s.size
        adj = np.zeros((n, n), dtype=bool)
        for i in range(n):
            si = s[i]
            for j in range(i + 1, n):
                sj = s[j]
                mid = s[i + 1 : j]
                # HVG condition: all intermediate values < min(si, sj)
                if mid.size == 0 or np.all(mid < min(si, sj)):
                    adj[i, j] = True
        adj = adj | adj.T
        return adj.astype(int)

    try:
        # 1) Extraer características por canal a partir de visibility graphs
        F = np.zeros((n_ch, 4), dtype=float)  # mean_deg, std_deg, mean_clust, std_clust
        for ch in range(n_ch):
            s = y[:, ch].copy()
            if np.isnan(s).all():
                s[:] = 0.0
            else:
                m = np.nanmean(s)
                s[np.isnan(s)] = m

            if use_hvg:
                adj_t = _hvg_adjacency(s)
            else:
                adj_t = _hvg_adjacency(s)  # placeholder for NVG if needed

            deg = adj_t.sum(axis=0).astype(float)

            # clustering coefficient por nodo (unweighted)
            clust = np.zeros(n_t, dtype=float)
            for ti in range(n_t):
                nbr = np.where(adj_t[ti] > 0)[0]
                k_i = nbr.size
                if k_i < 2:
                    clust[ti] = 0.0
                else:
                    sub = adj_t[np.ix_(nbr, nbr)].astype(float)
                    E = sub.sum() / 2.0
                    clust[ti] = (2.0 * E) / (k_i * (k_i - 1))

            F[ch, 0] = float(np.mean(deg))
            F[ch, 1] = float(np.std(deg))
            F[ch, 2] = float(np.nanmean(clust))
            F[ch, 3] = float(np.nanstd(clust))

        # 2) Matriz de similitud (kernel RBF sobre features)
        dmat = cdist(F, F, metric="euclidean")
        vals = dmat[np.triu_indices(n_ch, k=1)]
        vals = vals[vals > 0]
        sigma = float(np.median(vals)) if vals.size > 0 else 1.0
        if not np.isfinite(sigma) or sigma <= 0:
            sigma = 1.0
        G = np.exp(-(dmat ** 2) / (2.0 * sigma ** 2))
        np.fill_diagonal(G, np.max(G))

        # 3) Construir máscara de candidatos para NNK (por similitud)
        knn_param = int(max(1, min(k, n_ch - 1)))
        mask_rows = np.zeros((n_ch, knn_param), dtype=int)
        for i in range(n_ch):
            order = np.argsort(-G[i])
            order = order[order != i]
            if order.size < knn_param:
                pad = np.arange(n_ch)[np.arange(n_ch) != i]
                needed = knn_param - order.size
                order = np.concatenate([order, pad[:needed]])
            mask_rows[i] = order[:knn_param]

        # 4) Invocar implementación NNK (PyNNK) desde Code1201 si está disponible
        repo_root = Path(__file__).resolve().parents[1]
        pynnk_file = repo_root / "Code1201" / "PyNNK_graph_construction" / "graph_construction.py"
        if not pynnk_file.exists():
            raise FileNotFoundError(f"PyNNK implementation not found: {pynnk_file}")

        # Ensure PyNNK module directory is importable so internal imports (e.g., non_neg_qpsolver)
        # work when executing the file as a module.
        import sys
        spec = importlib.util.spec_from_file_location("pynnk_gc", str(pynnk_file))
        pynnk_gc = importlib.util.module_from_spec(spec)
        sys.path.insert(0, str(pynnk_file.parent))
        try:
            spec.loader.exec_module(pynnk_gc)
        finally:
            try:
                # remove the inserted path to avoid side-effects
                if sys.path[0] == str(pynnk_file.parent):
                    sys.path.pop(0)
            except Exception:
                pass

        adjacency_sparse = pynnk_gc.nnk_graph(G, mask_rows, knn_param, reg=nnk_reg)
        try:
            adjacency_nnk = adjacency_sparse.toarray()
        except Exception:
            adjacency_nnk = np.asarray(adjacency_sparse)

        adjacency_nnk = np.maximum(adjacency_nnk, adjacency_nnk.T)
        np.fill_diagonal(adjacency_nnk, 0.0)

        # 5) Reconstruir usando TRSS (paper-faithful spatial-temporal) con la adyacencia NNK
        lr = float(trss_lr)
        reconstructed = interpolate_trss(y, adjacency=adjacency_nnk, alpha=alpha, beta=beta, n_iter=n_iter, lr=lr)
        return reconstructed

    except Exception as exc:
        # Fallback: registrar y ejecutar la antigua implementación basada en coherencia
        try:
            record_warning("visibility_graphs", "fallback", str(exc), severity="warning", decision="fallback")
        except Exception:
            pass

        # --- Código legacy (coherencia temporal adaptativa) ---
        y2 = y.copy()
        mask2 = ~np.isnan(y2)
        x = y2.copy()
        col_mean = np.nanmean(x, axis=0)
        col_mean = np.where(np.isnan(col_mean), 0.0, col_mean)
        miss = ~mask2
        x[miss] = np.take(col_mean, np.where(miss)[1])

        lap_g = csgraph.laplacian(adjacency if adjacency is not None else np.eye(n_ch), normed=False)
        t = x.shape[0]
        coherence = np.ones((t, t), dtype=float)

        for i in range(t):
            for j in range(min(i + 1, t)):
                if i == j:
                    continue
                corr_val = 0.0
                count = 0
                for ch1 in range(n_ch):
                    for ch2 in range(n_ch):
                        if not np.isnan(x[i, ch1]) and not np.isnan(x[j, ch2]):
                            corr_val += x[i, ch1] * x[j, ch2]
                            count += 1
                if count > 0:
                    coherence[i, j] = np.clip(corr_val / (count + 1e-12), 0.0, 1.0)
                    coherence[j, i] = coherence[i, j]

        adaptive_temp = coherence.copy()
        np.fill_diagonal(adaptive_temp, -np.sum(coherence, axis=1) + np.diag(coherence))

        scale = np.nanstd(y2)
        if not np.isfinite(scale) or scale <= 0:
            scale = 1.0

        step = 0.03
        for iter_no in range(n_iter):
            step_adaptive = step / (1.0 + 0.005 * iter_no)
            grad_data = (x - np.nan_to_num(y2, nan=0.0)) * mask2
            grad_graph = np.zeros_like(x)
            for t_idx in range(x.shape[0]):
                grad_graph[t_idx, :] = lap_g @ x[t_idx, :]
            grad_temporal = adaptive_temp @ x
            grad = 2.0 * grad_data + 2.0 * alpha * grad_graph + 2.0 * beta * grad_temporal
            grad += 2.0 * gamma * (x - np.nan_to_num(y2, nan=0.0))
            x = x - step_adaptive * grad
            x = np.clip(x, -8.0 * scale, 8.0 * scale)
            x[mask2] = y2[mask2]

        return x


def interpolate_rbfi(signals: np.ndarray, positions: np.ndarray, function: str = "thin_plate", smooth: float = 0.0) -> np.ndarray:
    return _rbf_per_row(signals, positions, function=function, smooth=smooth)


def interpolate_spline_surface(signals: np.ndarray, positions: np.ndarray) -> np.ndarray:
    x = positions[:, 0]
    y = positions[:, 1]
    reconstructed = signals.copy()

    for i in range(signals.shape[0]):
        row = signals[i]
        observed = ~np.isnan(row)
        if np.sum(observed) < 6:
            reconstructed[i, ~observed] = np.nanmean(row)
            continue

        filled = False
        try:
            import warnings

            # Escala de suavizado creciente para robustecer el ajuste de FITPACK.
            base_s = max(0.5, 0.05 * np.sum(observed))
            for factor in (1.0, 5.0, 20.0):
                with warnings.catch_warnings(record=True) as w:
                    warnings.simplefilter("always")
                    spline = SmoothBivariateSpline(
                        x[observed],
                        y[observed],
                        row[observed],
                        s=base_s * factor,
                    )

                fitpack_warn = False
                for warn in w:
                    msg = str(warn.message)
                    if "required storage space exceeds" in msg.lower() or "nxest" in msg.lower() or "nyest" in msg.lower():
                        fitpack_warn = True
                        record_warning(
                            method="spline_surface",
                            warning_code="FITPACK_CAPACITY",
                            message=msg,
                            severity="medium",
                            decision="fixed",
                            context={"row": int(i), "s_factor": float(factor)},
                        )
                        break

                if not fitpack_warn:
                    reconstructed[i, ~observed] = spline.ev(x[~observed], y[~observed])
                    filled = True
                    break
        except Exception:
            filled = False

        if filled:
            continue

        # Fallback controlado: RBF geométrico, y si falla, media de canales observados.
        try:
            rbf = Rbf(x[observed], y[observed], row[observed], function="thin_plate")
            reconstructed[i, ~observed] = rbf(x[~observed], y[~observed])
            record_warning(
                method="spline_surface",
                warning_code="FITPACK_FALLBACK_RBF",
                message="FITPACK fallback applied; RBF interpolation used",
                severity="low",
                decision="accepted",
                context={"row": int(i)},
            )
        except Exception:
            reconstructed[i, ~observed] = np.nanmean(row)
            record_warning(
                method="spline_surface",
                warning_code="FITPACK_FALLBACK_MEAN",
                message="FITPACK and RBF failed; mean fallback used",
                severity="high",
                decision="deferred",
                context={"row": int(i)},
            )

    return reconstructed


# Backwards compatibility alias (legacy name)
try:
    interpolate_adaptive_temporal = interpolate_visibility_graphs
except NameError:
    # If function is not defined for some reason, delay assignment.
    pass
