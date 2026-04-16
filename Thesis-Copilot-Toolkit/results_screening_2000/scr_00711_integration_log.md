# Integration Log: scr_00711
Started: 2026-04-16T15:34:13.751684+00:00
Description: Screening scr_00711 ds=bci_iv2a_real_s1 graph=kalofolias miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=0.0196s
    nearest | MR=0.4 | seed=0 | MAE=6.5281e-06 | t=0.0181s
    tikhonov | MR=0.4 | seed=0 | MAE=9.8811e-06 | t=0.0152s
    tv | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=1.2675s
    trss | MR=0.4 | seed=0 | MAE=4.9195e-06 | t=0.2663s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.2963e-05 | t=0.0363s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.7936e-05 | t=20.8733s
    mean | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.0031s
    nearest | MR=0.4 | seed=1 | MAE=6.8607e-06 | t=0.0356s
    tikhonov | MR=0.4 | seed=1 | MAE=9.8158e-06 | t=0.0138s
    tv | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.7629s
    trss | MR=0.4 | seed=1 | MAE=4.8792e-06 | t=0.1815s

Completed: 2026-04-16T15:34:13.753489+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.