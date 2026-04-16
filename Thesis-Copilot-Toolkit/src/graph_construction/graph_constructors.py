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


def build_graph(method: str, positions: np.ndarray, signals: np.ndarray = None, **kwargs) -> Dict[str, Any]:
    """
    Construye un grafo según el método especificado.

    Entradas:
    - method: método de construcción.
    - positions: matriz (n_electrodos, 2|3).
    - signals: opcional, matriz (n_instantes, n_electrodos) para métodos data-driven.
    """
    method = method.lower()
    n_nodes = positions.shape[0]

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
        # Adaptive Edge Weighting: mezcla cercanía espacial y similitud en señal.
        if signals is None:
            raise ValueError("El método 'aew' requiere 'signals'.")
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
