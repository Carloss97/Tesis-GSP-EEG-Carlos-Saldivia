**Aviso de artefacto histórico:** Este archivo contiene selecciones históricas que incluyen métodos ahora excluidos de ejecuciones activas. Ver [Thesis-Copilot-Toolkit/docs/HISTORICAL_ARTIFACTS_NOTICE.md](Thesis-Copilot-Toolkit/docs/HISTORICAL_ARTIFACTS_NOTICE.md).

# SELECTIONS — cutoff 0.05 (no physionet)

- Median filter matches: 0
- Mean filter matches: 0

## B1 — Mean-based (top 3)
- aew__k4_sigma_corr0_5_sigma_dist1 | heat_diffusion_temporal: mean_mae=0.1641371543200398
- aew__k4_sigma_corr0_5_sigma_dist1 | trss: mean_mae=0.1645469214538009
- kalofolias | directed_tv: mean_mae=0.1647039064027324

## B2 — Real-only mean (top 3)
- aew__k4_sigma_corr0_5_sigma_dist1 | heat_diffusion_temporal: mean_mae=0.1641371543200398
- aew__k4_sigma_corr0_5_sigma_dist1 | trss: mean_mae=0.1645469214538009
- kalofolias | directed_tv: mean_mae=0.1647039064027324

## B3 — Median-based (top 3)
- aew__k4_sigma_corr0_5_sigma_dist1 | gsmooth: median_mae=0.1610362106875651
- aew__k4_sigma_corr0_5_sigma_dist1 | trss: median_mae=0.1638271694529104
- aew__k4_sigma_corr0_5_sigma_dist1 | heat_diffusion_temporal: median_mae=0.1658630307899041

## B4 — Stability-first (top 3 by std_mae then mean_mae)
- aew__k4_sigma_corr0_5_sigma_dist1 | spline_temporal: std_mae=0.0 mean_mae=nan
- gaussian__sigma1 | spline_temporal: std_mae=0.0 mean_mae=nan
- kalofolias | spline_temporal: std_mae=0.0 mean_mae=nan
