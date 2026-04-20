"""Graph construction utilities for EEG pipelines."""

from typing import Any, Dict

import numpy as np
from scipy.spatial.distance import cdist
from scipy.optimize import nnls
from sklearn.neighbors import kneighbors_graph


def _as_dense(matrix: Any) -> np.ndarray:
    if hasattr(matrix, "toarray"):
        return matrix.toarray()
    return np.asarray(matrix)


def _symmetrize(adjacency: np.ndarray, mode: str = "max") -> np.ndarray:
    if mode == "mean":
        return 0.5 * (adjacency + adjacency.T)
    return np.maximum(adjacency, adjacency.T)


def _estimate_kernel_sigma(positions: np.ndarray) -> float:
    d = cdist(positions, positions)
    vals = d[np.triu_indices_from(d, k=1)]
    vals = vals[vals > 0]
    if vals.size == 0:
        return 1.0
    return float(np.median(vals))


def _build_nnk_adjacency(
    positions: np.ndarray,
    k: int,
    sigma: float,
    reg: float = 1e-6,
    weight_threshold: float = 1e-8,
) -> np.ndarray:
    """
    Implementacion propia de NNK via regresion de kernel no-negativa local.
    """
    n = positions.shape[0]
    dists = cdist(positions, positions)
    kernel = np.exp(-(dists**2) / (2.0 * sigma**2))
    np.fill_diagonal(kernel, 1.0)

    # Vecinos candidatos por distancia geometrica.
    d_local = dists.copy()
    np.fill_diagonal(d_local, np.inf)
    adjacency = np.zeros((n, n), dtype=float)

    k_eff = min(max(1, k), max(1, n - 1))
    for i in range(n):
        nbr = np.argpartition(d_local[i], k_eff)[:k_eff]
        k_nn = kernel[np.ix_(nbr, nbr)] + reg * np.eye(k_eff)
        k_in = kernel[nbr, i]

        # NNLS sobre kernel local: min ||K_nn x - k_in||^2 s.t. x >= 0
        try:
            x, _ = nnls(k_nn, k_in)
        except Exception:
            x = np.zeros(k_eff, dtype=float)

        x[x < weight_threshold] = 0.0
        adjacency[i, nbr] = x

    adjacency = _symmetrize(adjacency, mode="max")
    np.fill_diagonal(adjacency, 0.0)
    return adjacency


def hvg_adjacency(series: np.ndarray) -> np.ndarray:
    """Horizontal Visibility Graph (HVG) adjacency (unweighted).

    Condition: two nodes i<j are connected if all intermediate values
    are strictly less than min(s[i], s[j]).
    """
    s = np.asarray(series, dtype=float)
    n = s.size
    adj = np.zeros((n, n), dtype=bool)
    for i in range(n):
        si = s[i]
        for j in range(i + 1, n):
            sj = s[j]
            mid = s[i + 1 : j]
            if mid.size == 0 or np.all(mid < min(si, sj)):
                adj[i, j] = True
    adj = adj | adj.T
    return adj.astype(int)


def nvg_adjacency(series: np.ndarray) -> np.ndarray:
    """Natural Visibility Graph (NVG) adjacency (unweighted).

    Condition: two nodes i<j are connected if every intermediate
    point k satisfies s[k] < s[i] + (s[j]-s[i])*(k-i)/(j-i).
    """
    s = np.asarray(series, dtype=float)
    n = s.size
    adj = np.zeros((n, n), dtype=int)
    for i in range(n):
        si = s[i]
        for j in range(i + 1, n):
            sj = s[j]
            k_idx = np.arange(i + 1, j)
            if k_idx.size == 0:
                adj[i, j] = 1
                continue
            # linearly interpolate between si and sj
            numer = (sj - si) * (k_idx - i)
            denom = (j - i)
            line = si + numer / float(denom)
            if np.all(s[k_idx] < line):
                adj[i, j] = 1
    adj = adj | adj.T
    return adj.astype(int)


def prune_delay(adjacency: np.ndarray, max_delay: int) -> np.ndarray:
    """Prune edges in `adjacency` whose temporal lag exceeds `max_delay`.

    This is a lightweight port of the common `pruneDelay` idea: remove
    visibility edges that connect timestamps farther apart than allowed.
    """
    a = np.asarray(adjacency).copy()
    if a.ndim != 2 or a.shape[0] != a.shape[1]:
        raise ValueError("adjacency must be a square matrix")
    n = a.shape[0]
    if max_delay is None or max_delay < 0:
        return a
    for i in range(n):
        for j in range(n):
            if a[i, j] != 0 and abs(j - i) > int(max_delay):
                a[i, j] = 0
    return a


def _learn_kalofolias_weights(
    z: np.ndarray,
    a: float = 1.0,
    b: float = 1.0,
    max_iter: int = 400,
    lr: float = 5e-2,
    tol: float = 1e-6,
) -> np.ndarray:
    """
    Aproximacion numerica al modelo de Kalofolias (log-degrees + norma Frobenius):
    min_W <Z,W> - a*sum(log(d)) + b/2 ||W||_F^2
    s.a. W simetrica, no-negativa, diagonal cero.
    """
    n = z.shape[0]
    w = np.zeros((n, n), dtype=float)
    eps = 1e-8

    z = np.maximum(z, 0.0)
    z = 0.5 * (z + z.T)
    np.fill_diagonal(z, 0.0)

    for _ in range(max_iter):
        deg = np.sum(w, axis=1) + eps
        inv_deg = 1.0 / deg

        grad = z + b * w
        deg_term = a * (inv_deg[:, None] + inv_deg[None, :])
        grad = grad - deg_term
        np.fill_diagonal(grad, 0.0)

        w_new = w - lr * grad
        w_new = np.maximum(w_new, 0.0)
        w_new = 0.5 * (w_new + w_new.T)
        np.fill_diagonal(w_new, 0.0)

        rel = np.linalg.norm(w_new - w) / (np.linalg.norm(w) + 1e-12)
        w = w_new
        if rel < tol:
            break

    return w


def build_graph(method: str, positions: np.ndarray = None, signals: np.ndarray = None, **kwargs) -> Dict[str, Any]:
    """
    Construye un grafo según el método especificado.

    Entradas:
    - method: método de construcción.
    - positions: matriz (n_electrodos, 2|3).
    - signals: opcional, matriz (n_instantes, n_electrodos) para métodos data-driven.
    """
    method = method.lower()
    if positions is not None:
        n_nodes = positions.shape[0]
    elif signals is not None:
        if np.asarray(signals).ndim != 2:
            raise ValueError("'signals' debe tener forma (n_t, n_ch)")
        n_nodes = np.asarray(signals).shape[1]
    else:
        raise ValueError("Se requiere 'positions' o 'signals' para construir el grafo.")

    if method == "knn":
        k = min(int(kwargs.get("k", 5)), max(1, n_nodes - 1))
        adjacency = kneighbors_graph(
            positions,
            n_neighbors=k,
            mode="connectivity",
            include_self=False,
        )
        adjacency = _symmetrize(_as_dense(adjacency), mode="max")
        return {"adjacency": adjacency, "info": {"method": "knn", "k": k}}

    if method == "knng":
        # kNN Graph ponderado con kernel gaussiano sobre aristas kNN.
        k = min(int(kwargs.get("k", 5)), max(1, n_nodes - 1))
        sigma = float(kwargs.get("sigma", 1.0))
        dists = cdist(positions, positions)
        conn = kneighbors_graph(
            positions,
            n_neighbors=k,
            mode="connectivity",
            include_self=False,
        )
        conn = _symmetrize(_as_dense(conn), mode="max")
        adjacency = np.exp(-(dists**2) / (2.0 * sigma**2)) * conn
        np.fill_diagonal(adjacency, 0.0)
        return {"adjacency": adjacency, "info": {"method": "knng", "k": k, "sigma": sigma}}

    if method == "vknng":
        # Variable kNN Graph: k_i adaptativo según densidad local.
        # Ensure base_k does not exceed n_nodes-1 to avoid selecting the
        # diagonal (inf) when computing the k-th nearest neighbor distance
        # for very small graphs.
        base_k = min(int(kwargs.get("k", 5)), max(1, n_nodes - 1))
        alpha = float(kwargs.get("alpha", 1.0))
        k_min = int(kwargs.get("k_min", 2))
        k_max = int(kwargs.get("k_max", max(3, base_k * 2)))
        dists = cdist(positions, positions)
        np.fill_diagonal(dists, np.inf)

        local_scale = np.partition(dists, base_k - 1, axis=1)[:, base_k - 1]
        median_scale = np.median(local_scale[~np.isinf(local_scale)])
        adjacency = np.zeros((n_nodes, n_nodes), dtype=float)

        for i in range(n_nodes):
            ratio = (median_scale / max(local_scale[i], 1e-12)) ** alpha
            k_i = int(np.clip(round(base_k * ratio), k_min, min(k_max, n_nodes - 1)))
            nbr_idx = np.argpartition(dists[i], k_i)[:k_i]
            adjacency[i, nbr_idx] = 1.0

        adjacency = _symmetrize(adjacency, mode="max")
        np.fill_diagonal(adjacency, 0.0)
        return {
            "adjacency": adjacency,
            "info": {"method": "vknng", "k": base_k, "alpha": alpha, "k_min": k_min, "k_max": k_max},
        }

    if method == "gaussian":
        sigma = float(kwargs.get("sigma", 1.0))
        dists = cdist(positions, positions)
        adjacency = np.exp(-(dists**2) / (2.0 * sigma**2))
        np.fill_diagonal(adjacency, 0.0)
        return {"adjacency": adjacency, "info": {"method": "gaussian", "sigma": sigma}}

    if method == "epsilon_ball":
        epsilon = float(kwargs.get("epsilon", 0.5))
        dists = cdist(positions, positions)
        adjacency = (dists < epsilon).astype(float)
        np.fill_diagonal(adjacency, 0.0)
        return {"adjacency": adjacency, "info": {"method": "epsilon_ball", "epsilon": epsilon}}

    if method == "mst":
        from scipy.sparse.csgraph import minimum_spanning_tree

        dists = cdist(positions, positions)
        mst = minimum_spanning_tree(dists)
        adjacency = _symmetrize(mst.toarray(), mode="max")
        np.fill_diagonal(adjacency, 0.0)
        return {"adjacency": adjacency, "info": {"method": "mst"}}

    if method == "fully_connected_inverse_distance":
        dists = cdist(positions, positions)
        with np.errstate(divide="ignore", invalid="ignore"):
            adjacency = 1.0 / dists
            adjacency[dists == 0] = 0.0
        return {"adjacency": adjacency, "info": {"method": "fully_connected_inverse_distance"}}

    if method == "aew":
        # Adaptive Edge Weighting (paper-aligned): run AEW optimizer.
        # AEW expects `signals` as (n_t, n_ch) => columns are nodes/features.
        if signals is None:
            raise ValueError("El método 'aew' requiere 'signals'.")

        # Map kwargs to AEW parameters
        param = {
            "max_iter": int(kwargs.get("max_iter", 50)),
            "k": int(kwargs.get("k", 5)),
            "sigma": kwargs.get("sigma", "median"),
            "tol": float(kwargs.get("tol", 1e-4)),
            "beta": float(kwargs.get("beta", 0.1)),
            "rho": float(kwargs.get("rho", 1e-3)),
            "max_beta_p": int(kwargs.get("max_beta_p", 8)),
        }

        # prepare X as (d, n) where columns are nodes (features per node)
        y = np.asarray(signals, dtype=float)
        if y.ndim != 2:
            raise ValueError("'signals' debe tener forma (n_t, n_ch)")
        X = y  # shape (n_t, n_ch) => (d, n)

        # local import to avoid top-level dependency
        try:
            from .aew import AEW

            W_opt, W0 = AEW(X, param)
            adjacency = np.maximum(W_opt, W_opt.T)
            np.fill_diagonal(adjacency, 0.0)
            return {
                "adjacency": adjacency,
                "info": {"method": "aew", "k": param["k"], "max_iter": param["max_iter"], "backend": "aew_python"},
            }
        except Exception:
            # Fallback: keep lightweight mixture heuristic from earlier implementation
            k = min(int(kwargs.get("k", 5)), max(1, n_nodes - 1))
            sigma_dist = float(kwargs.get("sigma_dist", 1.0))
            sigma_corr = float(kwargs.get("sigma_corr", 0.5))

            dists = cdist(positions, positions)
            conn = kneighbors_graph(
                positions,
                n_neighbors=k,
                mode="connectivity",
                include_self=False,
            )
            conn = _symmetrize(_as_dense(conn), mode="max")

            spatial_w = np.exp(-(dists**2) / (2.0 * sigma_dist**2))
            corr = np.corrcoef(signals.T)
            corr = np.nan_to_num(corr, nan=0.0)
            signal_w = np.exp(-(1.0 - np.abs(corr)) / max(sigma_corr, 1e-12))
            adjacency = conn * spatial_w * signal_w
            np.fill_diagonal(adjacency, 0.0)
            return {
                "adjacency": adjacency,
                "info": {
                    "method": "aew",
                    "k": k,
                    "sigma_dist": sigma_dist,
                    "sigma_corr": sigma_corr,
                    "backend": "aew_fallback",
                },
            }

    if method == "kalofolias":
        # Implementacion interna del modelo con prior log-degree (sin dependencia MATLAB).
        if signals is None:
            raise ValueError("El método 'kalofolias' requiere 'signals'.")

        x = signals.T  # nodos x muestras
        z = cdist(x, x, metric="sqeuclidean")
        scale = float(kwargs.get("distance_scale", 1.0))
        z = z * scale

        a = float(kwargs.get("a", 1.0))
        b = float(kwargs.get("b", 1.0))
        max_iter = int(kwargs.get("max_iter", 400))
        lr = float(kwargs.get("lr", 5e-2))
        tol = float(kwargs.get("tol", 1e-6))

        adjacency = _learn_kalofolias_weights(z=z, a=a, b=b, max_iter=max_iter, lr=lr, tol=tol)
        return {
            "adjacency": adjacency,
            "info": {
                "method": "kalofolias",
                "backend": "internal_log_degree_opt",
                "a": a,
                "b": b,
            },
        }

    if method in {"visibility", "visibility_nnk", "visibility_graph"}:
        # Build visibility-graph features per channel and run NNK over feature-kernel.
        if signals is None:
            raise ValueError("El método 'visibility_nnk' requiere 'signals' (n_t, n_ch).")

        from scipy.spatial.distance import cdist
        from pathlib import Path
        import importlib.util
        import sys

        use_hvg = bool(kwargs.get("use_hvg", True))
        k = int(kwargs.get("k", 4))
        nnk_reg = float(kwargs.get("reg", 1e-6))

        y = np.asarray(signals, dtype=float)
        if y.ndim != 2:
            raise ValueError("'signals' debe tener forma (n_t, n_ch)")
        n_t, n_ch = y.shape

        def _hvg_adjacency(series: np.ndarray) -> np.ndarray:
            # delegate to module-level implementation
            return hvg_adjacency(series)

        # 1) Features per channel from visibility graphs
        F = np.zeros((n_ch, 4), dtype=float)
        for ch in range(n_ch):
            s = y[:, ch].copy()
            if np.isnan(s).all():
                s[:] = 0.0
            else:
                m = np.nanmean(s)
                s[np.isnan(s)] = m

            if use_hvg:
                adj_t = hvg_adjacency(s)
            else:
                adj_t = nvg_adjacency(s)

            deg = adj_t.sum(axis=0).astype(float)

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

        # 2) Kernel similarity over features (RBF)
        dmat = cdist(F, F, metric="euclidean")
        vals = dmat[np.triu_indices(n_ch, k=1)]
        vals = vals[vals > 0]
        sigma = float(np.median(vals)) if vals.size > 0 else 1.0
        if not np.isfinite(sigma) or sigma <= 0:
            sigma = 1.0
        G = np.exp(-(dmat ** 2) / (2.0 * sigma ** 2))
        np.fill_diagonal(G, np.max(G))

        # 3) Candidate mask for NNK
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

        # 4) Try Code1201 PyNNK nnk_graph if available
        repo_root = Path(__file__).resolve().parents[2]
        pynnk_file = repo_root / "Code1201" / "PyNNK_graph_construction" / "graph_construction.py"
        adjacency = None
        backend = "internal"
        if pynnk_file.exists():
            try:
                spec = importlib.util.spec_from_file_location("pynnk_gc", str(pynnk_file))
                pynnk_gc = importlib.util.module_from_spec(spec)
                sys.path.insert(0, str(pynnk_file.parent))
                spec.loader.exec_module(pynnk_gc)
                adjacency_sparse = pynnk_gc.nnk_graph(G, mask_rows, knn_param, reg=nnk_reg)
                try:
                    adjacency = adjacency_sparse.toarray()
                except Exception:
                    adjacency = np.asarray(adjacency_sparse)
                adjacency = np.maximum(adjacency, adjacency.T)
                np.fill_diagonal(adjacency, 0.0)
                backend = "pynnk"
            except Exception:
                adjacency = None
            finally:
                try:
                    if sys.path[0] == str(pynnk_file.parent):
                        sys.path.pop(0)
                except Exception:
                    pass

        if adjacency is None:
            # Fallback: use internal NNLS-based local NNK on feature positions
            sigma_feat = _estimate_kernel_sigma(F)
            adjacency = _build_nnk_adjacency(positions=F, k=k, sigma=sigma_feat, reg=nnk_reg, weight_threshold=float(kwargs.get("weight_threshold", 1e-8)))

        return {"adjacency": adjacency, "info": {"method": "visibility_nnk", "k": k, "backend": backend, "use_hvg": use_hvg}}

    if method == "nnk":
        k = min(int(kwargs.get("k", 5)), max(1, n_nodes - 1))
        sigma = float(kwargs.get("sigma", _estimate_kernel_sigma(positions)))
        reg = float(kwargs.get("reg", 1e-6))
        thr = float(kwargs.get("weight_threshold", 1e-8))

        backend = kwargs.get("backend", "auto")
        if backend in {"auto", "pynnk"}:
            try:
                from PyNNK_graph_construction.faiss_nnk_neighbors import nnk_graph

                adjacency = _as_dense(nnk_graph(positions, k=k))
                adjacency = _symmetrize(adjacency, mode="max")
                np.fill_diagonal(adjacency, 0.0)
                return {
                    "adjacency": adjacency,
                    "info": {"method": "nnk", "k": k, "backend": "pynnk"},
                }
            except Exception:
                # Fallback automatico a implementacion interna.
                pass

        adjacency = _build_nnk_adjacency(positions=positions, k=k, sigma=sigma, reg=reg, weight_threshold=thr)
        return {
            "adjacency": adjacency,
            "info": {"method": "nnk", "k": k, "sigma": sigma, "backend": "internal_nnls"},
        }

    raise NotImplementedError(f"Metodo de grafo no implementado: {method}")
