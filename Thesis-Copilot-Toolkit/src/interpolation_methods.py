"""Interpolation methods for EEG reconstruction with missing channels."""

from typing import Any, Dict
import warnings

import numpy as np
from scipy.interpolate import LinearNDInterpolator, Rbf, SmoothBivariateSpline
from scipy.special import lpmv


_NNI_FALLBACK_WARNED = False


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
        reconstructed = interpolate_bgsrp(signals, adjacency=adjacency, bandwidth=bandwidth)
        return {"reconstructed": reconstructed, "info": {"method": "bgsrp", "bandwidth": bandwidth}}

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

    if method == "qiu_batch":
        if adjacency is None:
            raise ValueError("Se requiere 'adjacency' para Qiu batch.")
        alpha = float(kwargs.get("alpha", 1.0))
        reconstructed = interpolate_qiu_batch(signals, adjacency=adjacency, alpha=alpha)
        return {"reconstructed": reconstructed, "info": {"method": "qiu_batch", "alpha": alpha}}

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

    if method in {"nni", "natural_neighbor"}:
        positions = kwargs.get("positions")
        k_neighbors = int(kwargs.get("k_neighbors", 6))
        reconstructed = interpolate_nni(signals, positions=positions, k_neighbors=k_neighbors)
        return {
            "reconstructed": reconstructed,
            "info": {"method": "nni", "k_neighbors": k_neighbors, "note": "approx"},
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


def interpolate_bgsrp(signals: np.ndarray, adjacency: np.ndarray, bandwidth: int = 8) -> np.ndarray:
    from scipy.sparse import csgraph

    laplacian = csgraph.laplacian(adjacency, normed=False)
    evals, evecs = np.linalg.eigh(laplacian)
    k = int(np.clip(bandwidth, 1, evecs.shape[1]))
    u_k = evecs[:, :k]

    reconstructed = signals.copy()
    for i in range(signals.shape[0]):
        y = signals[i]
        observed = ~np.isnan(y)
        if np.all(observed):
            continue
        if np.sum(observed) < 1:
            reconstructed[i] = np.zeros_like(y)
            continue

        a = u_k[observed, :]
        b = y[observed]
        try:
            coeffs, *_ = np.linalg.lstsq(a, b, rcond=None)
            reconstructed[i] = u_k @ coeffs
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
    TRSS (aprox): regularizacion espacio-temporal con restricciones duras en observaciones.
    """
    from scipy.sparse import csgraph

    y = signals.astype(float)
    mask = ~np.isnan(y)
    x = y.copy()

    # Inicializacion para faltantes.
    col_mean = np.nanmean(x, axis=0)
    col_mean = np.where(np.isnan(col_mean), 0.0, col_mean)
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

    # Paso adaptativo basado en cota de Lipschitz aproximada.
    norm_lg = np.linalg.norm(lap_g, ord=2)
    norm_lt = np.linalg.norm(lap_t, ord=2)
    lipschitz = 2.0 * (1.0 + alpha * norm_lg + beta * norm_lt)
    step = min(lr, 1.0 / max(lipschitz, 1e-8))

    scale = np.nanstd(y)
    if not np.isfinite(scale) or scale <= 0:
        scale = 1.0
    clip_bound = 8.0 * scale

    for _ in range(n_iter):
        grad_data = (x - np.nan_to_num(y, nan=0.0)) * mask
        grad_graph = x @ lap_g
        grad_time = lap_t @ x
        grad = 2.0 * grad_data + 2.0 * alpha * grad_graph + 2.0 * beta * grad_time

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
    col_mean = np.nanmean(x, axis=0)
    col_mean = np.where(np.isnan(col_mean), 0.0, col_mean)
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


def interpolate_qiu_batch(signals: np.ndarray, adjacency: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    from scipy.sparse import csgraph

    laplacian = csgraph.laplacian(adjacency, normed=False)
    n_channels = signals.shape[1]
    eye = np.eye(n_channels)

    reconstructed = signals.copy()
    for i in range(signals.shape[0]):
        y = signals[i]
        observed = ~np.isnan(y)
        m = np.diag(observed.astype(float))
        rhs = np.nan_to_num(y, nan=0.0)
        a = m + alpha * (eye + laplacian)
        try:
            reconstructed[i] = np.linalg.solve(a, m @ rhs)
        except np.linalg.LinAlgError:
            reconstructed[i, ~observed] = np.nanmean(y)
    return reconstructed


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


def interpolate_nni(signals: np.ndarray, positions: np.ndarray = None, k_neighbors: int = 6) -> np.ndarray:
    if positions is None:
        raise ValueError("Se requieren 'positions' para NNI.")

    reconstructed = signals.copy()
    xy = positions[:, :2]
    dists = np.linalg.norm(positions[:, None, :] - positions[None, :, :], axis=2)
    np.fill_diagonal(dists, np.inf)

    use_exact_backend = False
    naturalneighbor_backend = None
    try:
        import naturalneighbor as naturalneighbor_backend  # type: ignore

        use_exact_backend = True
    except Exception:
        global _NNI_FALLBACK_WARNED
        if not _NNI_FALLBACK_WARNED:
            warnings.warn(
                "Paquete 'naturalneighbor' no disponible. NNI usara fallback lineal local.",
                RuntimeWarning,
            )
            _NNI_FALLBACK_WARNED = True

    for i in range(signals.shape[0]):
        y = signals[i].copy()
        observed = ~np.isnan(y)
        obs_idx = np.where(observed)[0]
        miss_idx = np.where(~observed)[0]
        if obs_idx.size == 0 or miss_idx.size == 0:
            continue

        if use_exact_backend:
            try:
                pts = xy[obs_idx]
                vals = y[obs_idx]
                xi = xy[miss_idx]
                pred = naturalneighbor_backend.griddata(pts, vals, xi)  # type: ignore[attr-defined]
                pred = np.asarray(pred).reshape(-1)
                y[miss_idx] = pred
                reconstructed[i] = y
                continue
            except Exception:
                # Si falla backend externo, continuar con fallback local.
                pass

        # Fallback estable: interpolación lineal en triangulación + IDW local para NaN residuales.
        interp = LinearNDInterpolator(xy[obs_idx], y[obs_idx], fill_value=np.nan)
        pred = interp(xy[miss_idx])
        y[miss_idx] = pred

        # Reemplazo de NaN residuales con IDW local.
        rem = np.where(np.isnan(y))[0]
        for m in rem:
            local = obs_idx[np.argsort(dists[m, obs_idx])[: min(k_neighbors, obs_idx.size)]]
            local_d = np.maximum(dists[m, local], 1e-12)
            w = 1.0 / local_d
            y[m] = np.dot(w, y[local]) / np.sum(w)

        reconstructed[i] = y

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
        try:
            # Smoothing adaptativo para evitar sobreajuste y warnings numéricos.
            s_val = max(0.5, 0.05 * np.sum(observed))
            spline = SmoothBivariateSpline(x[observed], y[observed], row[observed], s=s_val)
            reconstructed[i, ~observed] = spline.ev(x[~observed], y[~observed])
        except Exception:
            reconstructed[i, ~observed] = np.nanmean(row)

    return reconstructed
