# Integration Log: scr_00651
Started: 2026-04-16T15:00:58.417168+00:00
Description: Screening scr_00651 ds=bci_iv2a_real_s1 graph=knn miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=0.0036s
    nearest | MR=0.4 | seed=0 | MAE=6.5281e-06 | t=0.0139s
    tikhonov | MR=0.4 | seed=0 | MAE=8.3009e-06 | t=0.0109s
    tv | MR=0.4 | seed=0 | MAE=6.3026e-06 | t=0.4384s
    trss | MR=0.4 | seed=0 | MAE=4.7099e-06 | t=0.6796s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.1545e-05 | t=0.0128s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.6345e-05 | t=20.8423s
    mean | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.0049s
    nearest | MR=0.4 | seed=1 | MAE=6.8607e-06 | t=0.0140s
    tikhonov | MR=0.4 | seed=1 | MAE=8.2347e-06 | t=0.0470s
    tv | MR=0.4 | seed=1 | MAE=6.2500e-06 | t=0.2013s
    trss | MR=0.4 | seed=1 | MAE=4.6991e-06 | t=0.0206s

Completed: 2026-04-16T15:00:58.418064+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.