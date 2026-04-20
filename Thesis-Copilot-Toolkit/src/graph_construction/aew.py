"""Adaptive Edge Weighting (AEW) port from MATLAB to Python.

Port of Papers/MSALP_AEW/AEW.m and generate_nngraph.m adapted for
graph-construction pipelines. The functions expect `X` with shape
`(d, n)` where columns correspond to objects/nodes and rows to features.
"""
from typing import Tuple, Union

import numpy as np
from scipy.spatial.distance import pdist, squareform


def generate_nngraph(X: np.ndarray, k: int, sigma: str = "median") -> Tuple[np.ndarray, Union[float, np.ndarray]]:
    """Create a nearest-neighbour affinity matrix W and sigma heuristics.

    X: array (d, n) where columns are points
    k: number of nearest neighbors
    sigma: 'median' or 'local-scaling'
    Returns (W, sigma0) where sigma0 may be scalar (median) or array (local-scaling).
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError("X must be 2D array with shape (d, n)")
    d, n = X.shape

    # pairwise squared distances between columns (n x n)
    D = squareform(pdist(X.T, metric="sqeuclidean"))

    # sort distances per column (each column includes 0 on diagonal first)
    sort_idx = np.argsort(D, axis=0)
    sort_D = np.sort(D, axis=0)

    # nearest neighbors indices and distances (exclude self at row 0)
    k_eff = max(1, min(int(k), n - 1))
    knn_idx = sort_idx[1 : k_eff + 1, :]
    kD = sort_D[1 : k_eff + 1, :]

    W = np.zeros((n, n), dtype=float)
    if sigma == "median":
        sigma_val = float(np.mean(np.sqrt(kD[np.isfinite(kD)])))
        if sigma_val == 0 or not np.isfinite(sigma_val):
            sigma_val = 1.0
        for i in range(n):
            W[i, knn_idx[:, i]] = np.exp(-kD[:, i] / (2.0 * sigma_val ** 2))
        sigma_out = sigma_val
    elif sigma == "local-scaling":
        # MATLAB: use sqrt(kD(end,:)) if k<7 else sqrt(kD(7,:))
        if k_eff < 7:
            sigma_arr = np.sqrt(kD[-1, :])
        else:
            sigma_arr = np.sqrt(kD[6, :])
        sigma_arr = np.asarray(sigma_arr)
        sigma_arr[sigma_arr == 0] = 1.0
        for i in range(n):
            idxs = knn_idx[:, i]
            denom = sigma_arr[i] * sigma_arr[idxs]
            W[i, idxs] = np.exp(-kD[:, i] / denom)
        sigma_out = sigma_arr
    else:
        raise ValueError("Unknown option for sigma: %r" % sigma)

    # symmetrize
    W = np.maximum(W, W.T)
    return W, sigma_out


def AEW(X: np.ndarray, param: dict) -> Tuple[np.ndarray, np.ndarray]:
    """Port of the MATLAB AEW implementation.

    Inputs
    - X: array (d, n) where columns are node feature vectors
    - param: dict with keys `max_iter`, `k`, `sigma` ('median'|'local-scaling'), and optional
      `tol`, `beta`, `rho`, `max_beta_p`.

    Returns (W, W0): optimized adjacency and initial adjacency.
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError("X must be 2D array with shape (d, n)")
    d, n = X.shape

    max_iter = int(param.get("max_iter", 50))
    k = int(param.get("k", 5))
    sigma_opt = param.get("sigma", "median")
    tol = float(param.get("tol", 1e-4))
    beta = float(param.get("beta", 0.1))
    max_beta_p = int(param.get("max_beta_p", 8))
    rho = float(param.get("rho", 1e-3))

    # initial nearest-neighbour affinity + sigma heuristic
    W0, sigma0 = generate_nngraph(X, k, sigma_opt)

    L = np.eye(d, dtype=float)
    Xori = X.copy()

    # distances are computed between columns of X (points)
    if np.ndim(sigma0) > 0 and np.shape(sigma0)[0] > 1:
        sigma_arr = np.asarray(sigma0).reshape(n, 1)
        dist = squareform(pdist(X.T, metric="sqeuclidean"))
        dist = dist / (sigma_arr @ sigma_arr.T)
    else:
        sigma_scalar = float(np.asarray(sigma0).item())
        Xs = X / (np.sqrt(2.0) * sigma_scalar)
        dist = squareform(pdist(Xs.T, metric="sqeuclidean"))

    # initialize W only on edges present in W0
    edge_mask = W0 > 0
    W = np.zeros((n, n), dtype=float)
    W[edge_mask] = np.exp(-dist[edge_mask])

    # prepare derivatives
    W_idx = [np.where(W[i, :] != 0)[0] for i in range(n)]

    Gd = np.zeros((n, n, d), dtype=float)
    for i in range(n):
        xi = X[:, i]
        for j in W_idx[i]:
            diff = xi - X[:, j]
            Gd[i, j, :] = -(diff * diff)
            if np.ndim(sigma0) > 0 and np.shape(sigma0)[0] > 1:
                Gd[i, j, :] = Gd[i, j, :] / (sigma_arr[i, 0] * sigma_arr[j, 0])

    d_W = np.zeros((n, n, d), dtype=float)
    d_WDi = np.zeros_like(d_W)

    ex = False
    beta_p = 0

    for it in range(max_iter):
        D = np.sum(W, axis=1)
        D_safe = np.where(D == 0, 1e-12, D)

        # compute d_W
        for i in range(n):
            idx = W_idx[i]
            if idx.size == 0:
                continue
            A = Gd[i, idx, :]  # (len_idx, d)
            L_diag = np.diag(L)
            B = A * L_diag[None, :]
            d_W[i, idx, :] = 2.0 * (W[i, idx][:, None] * B)

        sum_d_W = np.zeros((n, d), dtype=float)
        for i in range(n):
            idx = W_idx[i]
            if idx.size == 0:
                continue
            sum_d_W[i, :] = d_W[i, idx, :].sum(axis=0)
            D_i = D_safe[i]
            term1 = d_W[i, idx, :] / D_i
            term2 = (W[i, idx] / (D_i ** 2))[:, None] * sum_d_W[i, :][None, :]
            d_WDi[i, idx, :] = term1 - term2

        Xest = (np.diag(1.0 / D_safe) @ W @ Xori.T).T
        err = Xori - Xest
        sqerr = np.sum(err ** 2)

        # gradient assembly (MATLAB uses column-major reshapes)
        M = np.reshape(d_WDi, (n * n, d), order="F")
        T = err.T @ Xori
        vec_T = np.reshape(T, (n * n,), order="F")
        grad_raw = - (M.T @ vec_T)
        normg = np.linalg.norm(grad_raw)
        grad = grad_raw / (normg + 1e-16)

        print(f"AEW iter={it+1}, MSE={sqerr/(d*n):.6e}")

        # line search
        step = (beta ** beta_p) * 1.0
        sqerr_prev = sqerr
        L_prev = L.copy()

        accepted = False
        while True:
            L = L_prev - step * np.diag(grad)
            LX = L @ X
            dist_new = squareform(pdist(LX.T, metric="sqeuclidean"))
            if np.ndim(sigma0) > 0 and np.shape(sigma0)[0] > 1:
                dist_new = dist_new / (sigma_arr @ sigma_arr.T)
            W[edge_mask] = np.exp(-dist_new[edge_mask])

            D = np.sum(W, axis=1)
            D_safe = np.where(D == 0, 1e-12, D)
            Xest = (np.diag(1.0 / D_safe) @ W @ Xori.T).T
            err = Xori - Xest
            sqerr_temp = np.sum(err ** 2)

            if sqerr_temp - sqerr_prev <= -rho * step * (grad @ grad):
                accepted = True
                break

            beta_p += 1
            if beta_p > max_beta_p:
                ex = True
                break
            step = step * beta

        if ex:
            break

        if ((sqerr_prev - sqerr_temp) / (sqerr_prev + 1e-16)) < tol:
            break

    return W, W0
