"""Interpolation methods for EEG reconstruction with missing channels."""

import warnings
from typing import Any, Dict

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
        reconstructed = interpolate_temporal_laplacian(signals, adjacency=adjacency, alpha=alpha, beta=beta)
        return {
            "reconstructed": reconstructed,
            "info": {"method": "temporal_laplacian", "alpha": alpha, "beta": beta},
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

    if method == "adaptive_temporal":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para adaptive_temporal.")
        alpha = float(kwargs.get("alpha", 0.55))
        beta = float(kwargs.get("beta", 0.2))
        gamma = float(kwargs.get("gamma", 0.05))
        n_iter = int(kwargs.get("n_iter", 100))
        reconstructed = interpolate_adaptive_temporal(signals, adjacency=adjacency, alpha=alpha, beta=beta, gamma=gamma, n_iter=n_iter)
        return {
            "reconstructed": reconstructed,
            "info": {"method": "adaptive_temporal", "alpha": alpha, "beta": beta, "gamma": gamma, "n_iter": n_iter},
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
            reconstructed = interpolate_spherical_spline(signals, positions=positions)
        elif method == "rbfi_tps":
            reconstructed = interpolate_rbfi(signals, positions=positions, function="thin_plate")
        elif method == "rbfi_mq":
            reconstructed = interpolate_rbfi(signals, positions=positions, function="multiquadric")
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

    laplacian = csgraph.laplacian(adjacency, normed=False)
    evals, evecs = np.linalg.eigh(laplacian)

    # RKHS BGSRP usa base bandlimited excluyendo componente DC.
    n_nodes = evecs.shape[0]
    n = int(np.clip(bandwidth, 2, n_nodes - 1))
    u_n = evecs[:, 1:n]
    mu_n = evals[1:n]
    if not strict_matlab:
        mu_n = np.maximum(mu_n, reg)
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
            reconstructed[i] = x_rec
        except np.linalg.LinAlgError:
            reconstructed[i, ~observed] = np.nanmean(y)

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


def _rbf_per_row(signals: np.ndarray, positions: np.ndarray, function: str) -> np.ndarray:
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
            rbf = Rbf(x[observed], y[observed], z[observed], row[observed], function=function)
            reconstructed[i, ~observed] = rbf(x[~observed], y[~observed], z[~observed])
        except Exception:
            reconstructed[i, ~observed] = np.nanmean(row)
    return reconstructed


def interpolate_spherical_spline(signals: np.ndarray, positions: np.ndarray) -> np.ndarray:
    # Implementacion tipo Perrin et al. para spherical splines EEG.
    pos = positions.copy().astype(float)
    norm = np.linalg.norm(pos, axis=1, keepdims=True)
    norm = np.where(norm == 0, 1.0, norm)
    pos = pos / norm

    n_channels = pos.shape[0]
    cos_matrix = np.clip(pos @ pos.T, -1.0, 1.0)

    m_order = 4
    n_terms = 50
    eps = 1e-6

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
) -> np.ndarray:
    """
    Product graph: combined spatial-temporal Laplacian.
    Interpola resolviendo min ||x - y||_M + alpha * x'Lx + beta * x'L_t x
    donde L_t es el Laplaciano temporal.
    """
    from scipy.sparse import csgraph, eye, kron

    y = signals.astype(float)
    mask = ~np.isnan(y)
    n_t, n_ch = y.shape

    # Laplacianos espacial y temporal
    lap_g = csgraph.laplacian(adjacency, normed=False)
    
    # Laplaciano temporal simple (primeras diferencias)
    l_temp = np.zeros((n_t, n_t), dtype=float)
    for i in range(n_t - 1):
        l_temp[i, i] += 1.0
        l_temp[i, i + 1] -= 1.0
        l_temp[i + 1, i] -= 1.0
        l_temp[i + 1, i + 1] += 1.0

    # Producto Kronecker: L_space ⊗ I_t + I_space ⊗ L_t
    eye_t = eye(n_t, dtype=float)
    eye_g = eye(n_ch, dtype=float)
    
    l_spatial = kron(lap_g, eye_t)
    l_temporal = kron(eye_g, l_temp)
    l_combined = alpha * l_spatial + beta * l_temporal

    x_flat = y.ravel()
    mask_flat = mask.ravel()
    m = np.diag(mask_flat.astype(float))
    b = np.nan_to_num(x_flat, nan=0.0)

    a = m + l_combined
    try:
        x_flat = np.linalg.solve(a, m @ b)
        return x_flat.reshape(n_t, n_ch)
    except np.linalg.LinAlgError:
        reconstructed = y.copy()
        col_mean = np.nanmean(y, axis=0)
        col_mean = np.where(np.isnan(col_mean), 0.0, col_mean)
        miss = ~mask
        reconstructed[miss] = np.take(col_mean, np.where(miss)[1])
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


def interpolate_adaptive_temporal(
    signals: np.ndarray,
    adjacency: np.ndarray,
    alpha: float = 0.55,
    beta: float = 0.2,
    gamma: float = 0.05,
    n_iter: int = 100,
) -> np.ndarray:
    """
    Adaptive temporal smoothing: combina suavizado temporo-espacial con 
    adaptacion local basada en coherencia de señal (Bozkurt & Ortega 2022).
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
    
    # Matriz de pesos adaptativos basada en coherencia temporal
    t = x.shape[0]
    n_ch = x.shape[1]
    coherence = np.ones((t, t), dtype=float)
    
    for i in range(t):
        for j in range(min(i + 1, t)):
            if i == j:
                continue
            # Correlacion simple entre todos los canales en dos instantes
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

    # Laplaciano temporal adaptativo
    adaptive_temp = coherence.copy()
    np.fill_diagonal(adaptive_temp, -np.sum(coherence, axis=1) + np.diag(coherence))

    scale = np.nanstd(y)
    if not np.isfinite(scale) or scale <= 0:
        scale = 1.0

    step = 0.03

    for iter_no in range(n_iter):
        step_adaptive = step / (1.0 + 0.005 * iter_no)

        grad_data = (x - np.nan_to_num(y, nan=0.0)) * mask
        
        # Gradiente espacial: aplicar por timestep
        grad_graph = np.zeros_like(x)
        for t in range(x.shape[0]):  # Para cada timestep
            grad_graph[t, :] = lap_g @ x[t, :]  # Apply spatial Laplacian to each time point
        
        grad_temporal = adaptive_temp @ x  # (t, t) @ (t, n_ch) = (t, n_ch) ✓
        
        grad = 2.0 * grad_data + 2.0 * alpha * grad_graph + 2.0 * beta * grad_temporal
        grad += 2.0 * gamma * (x - np.nan_to_num(y, nan=0.0))  # Término de fidelidad adicional

        x = x - step_adaptive * grad
        x = np.clip(x, -8.0 * scale, 8.0 * scale)
        x[mask] = y[mask]

    return x


def interpolate_rbfi(signals: np.ndarray, positions: np.ndarray, function: str = "thin_plate") -> np.ndarray:
    return _rbf_per_row(signals, positions, function=function)


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
