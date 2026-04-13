# Integration Log: it142_confidence_bootstrap_real
Started: 2026-04-13T18:34:16.702813+00:00
Description: Bootstrap CI for key combos on real datasets

## Dataset: bci_iv2a_real_s1 | rows=70
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=2.4466e-06 | t=0.0025s
    nearest | MR=0.2 | seed=0 | MAE=2.5305e-06 | t=0.0046s
    tikhonov | MR=0.2 | seed=0 | MAE=5.4376e-06 | t=0.0064s
    tv | MR=0.2 | seed=0 | MAE=2.4464e-06 | t=0.1651s
    trss | MR=0.2 | seed=0 | MAE=1.6619e-06 | t=0.0186s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.8596e-06 | t=0.0085s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4752e-05 | t=1.7432s
    mean | MR=0.2 | seed=1 | MAE=2.4913e-06 | t=0.0028s
    nearest | MR=0.2 | seed=1 | MAE=2.5788e-06 | t=0.0043s
    tikhonov | MR=0.2 | seed=1 | MAE=5.4520e-06 | t=0.0079s
    tv | MR=0.2 | seed=1 | MAE=2.4911e-06 | t=0.1837s
    trss | MR=0.2 | seed=1 | MAE=1.7407e-06 | t=0.0203s

## Dataset: iv100hz_mat | rows=70
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1733e+01 | t=0.0028s
    nearest | MR=0.2 | seed=0 | MAE=6.4929e+01 | t=0.0053s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0048e+02 | t=0.0065s
    tv | MR=0.2 | seed=0 | MAE=4.0719e+01 | t=0.1633s
    trss | MR=0.2 | seed=0 | MAE=3.3793e+01 | t=0.0191s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6687e+02 | t=0.0098s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0205e+02 | t=1.4527s
    mean | MR=0.2 | seed=1 | MAE=4.1650e+01 | t=0.0026s
    nearest | MR=0.2 | seed=1 | MAE=6.5250e+01 | t=0.0046s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0097e+02 | t=0.0063s
    tv | MR=0.2 | seed=1 | MAE=4.0392e+01 | t=0.1576s
    trss | MR=0.2 | seed=1 | MAE=3.4227e+01 | t=0.0194s

## Dataset: physionet_eegmmidb_real | rows=70
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1027e-06 | t=0.0022s
    nearest | MR=0.2 | seed=0 | MAE=4.7139e-06 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=5.5530e-06 | t=0.0066s
    tv | MR=0.2 | seed=0 | MAE=4.0081e-06 | t=0.1517s
    trss | MR=0.2 | seed=0 | MAE=1.9701e-06 | t=0.0171s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0695e-05 | t=0.0077s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8840e-05 | t=1.4050s
    mean | MR=0.2 | seed=1 | MAE=4.0539e-06 | t=0.0024s
    nearest | MR=0.2 | seed=1 | MAE=4.6000e-06 | t=0.0045s
    tikhonov | MR=0.2 | seed=1 | MAE=5.5283e-06 | t=0.0063s
    tv | MR=0.2 | seed=1 | MAE=3.9560e-06 | t=0.1435s
    trss | MR=0.2 | seed=1 | MAE=1.9551e-06 | t=0.0177s

Completed: 2026-04-13T18:34:16.705126+00:00
Total rows: 210
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.