import numpy as np
from src.interpolation_methods import interpolate_visibility_graphs

n_t = 60
n_ch = 8
rng = np.random.default_rng(0)
t = np.linspace(0, 1, n_t)
signals = np.stack([
    np.sin(2 * np.pi * (5 + i * 0.5) * t) + 0.01 * rng.normal(size=n_t)
    for i in range(n_ch)
], axis=1)
# Introduce some missing blocks
masked = signals.copy()
masked[10:20, 2] = np.nan
masked[30:40, 5] = np.nan

try:
    recon = interpolate_visibility_graphs(masked, adjacency=np.eye(n_ch), n_iter=5)
    print("recon shape:", recon.shape)
    print("finite:", bool(np.isfinite(recon).all()))
    print("nan count:", int(np.isnan(recon).sum()))
except Exception as e:
    import traceback
    traceback.print_exc()
    print("ERROR:", e)
