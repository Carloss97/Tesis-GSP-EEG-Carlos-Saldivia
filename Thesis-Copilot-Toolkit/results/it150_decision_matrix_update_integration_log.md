# Integration Log: it150_decision_matrix_update
Started: 2026-04-13T19:08:24.605812+00:00
Description: Update decision matrix after focused experiments

## Dataset: bci_iv2a_real_s1 | rows=28
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=2.4466e-06 | t=0.0019s
    nearest | MR=0.2 | seed=0 | MAE=2.5305e-06 | t=0.0065s
    tikhonov | MR=0.2 | seed=0 | MAE=5.4376e-06 | t=0.0105s
    tv | MR=0.2 | seed=0 | MAE=2.4464e-06 | t=0.2019s
    trss | MR=0.2 | seed=0 | MAE=1.6619e-06 | t=0.0201s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.8596e-06 | t=0.0115s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4752e-05 | t=1.7787s
    mean | MR=0.2 | seed=1 | MAE=2.4913e-06 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=2.5788e-06 | t=0.0062s
    tikhonov | MR=0.2 | seed=1 | MAE=5.4520e-06 | t=0.0074s
    tv | MR=0.2 | seed=1 | MAE=2.4911e-06 | t=0.2039s
    trss | MR=0.2 | seed=1 | MAE=1.7407e-06 | t=0.0224s

## Dataset: bci_iv2a_real_s2 | rows=28
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.1855e-07 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=6.6601e-07 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6739e-06 | t=0.0072s
    tv | MR=0.2 | seed=0 | MAE=7.1857e-07 | t=0.2151s
    trss | MR=0.2 | seed=0 | MAE=6.1411e-07 | t=0.0217s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.6485e-06 | t=0.0108s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2965e-05 | t=1.7997s
    mean | MR=0.2 | seed=1 | MAE=7.0041e-07 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=6.9296e-07 | t=0.0070s
    tikhonov | MR=0.2 | seed=1 | MAE=1.6581e-06 | t=0.0074s
    tv | MR=0.2 | seed=1 | MAE=7.0041e-07 | t=0.2097s
    trss | MR=0.2 | seed=1 | MAE=5.9749e-07 | t=0.0202s

## Dataset: physionet_eegmmidb_real | rows=28
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1027e-06 | t=0.0036s
    nearest | MR=0.2 | seed=0 | MAE=4.7139e-06 | t=0.0064s
    tikhonov | MR=0.2 | seed=0 | MAE=5.5530e-06 | t=0.0094s
    tv | MR=0.2 | seed=0 | MAE=4.0081e-06 | t=0.2154s
    trss | MR=0.2 | seed=0 | MAE=1.9701e-06 | t=0.0260s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0695e-05 | t=0.0131s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8840e-05 | t=1.9076s
    mean | MR=0.2 | seed=1 | MAE=4.0539e-06 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=4.6000e-06 | t=0.0064s
    tikhonov | MR=0.2 | seed=1 | MAE=5.5283e-06 | t=0.0099s
    tv | MR=0.2 | seed=1 | MAE=3.9560e-06 | t=0.2120s
    trss | MR=0.2 | seed=1 | MAE=1.9551e-06 | t=0.0214s

Completed: 2026-04-13T19:08:24.608109+00:00
Total rows: 84
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.