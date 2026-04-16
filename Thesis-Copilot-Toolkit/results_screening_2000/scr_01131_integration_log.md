# Integration Log: scr_01131
Started: 2026-04-16T14:08:57.045623+00:00
Description: Screening scr_01131 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.2344s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.3255e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=7.0652e-07 | t=0.0203s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3921e-05 | t=17.8837s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.2173s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3856e-06 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=8.2877e-07 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3940e-05 | t=2.7501s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.1973s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1082e-05 | t=0.0088s
    trss | MR=0.2 | seed=0 | MAE=9.6702e-07 | t=0.0218s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6084e-05 | t=23.8110s

Completed: 2026-04-16T14:08:57.046344+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.