# Integration Log: it104_noise_sensitivity_tv
Started: 2026-04-06T17:50:25.775806+00:00
Description: Noise sensitivity analysis for TV methods

## Dataset: physionet_eegmmidb_real | rows=112
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1646e-06 | t=0.0040s
    nearest | MR=0.2 | seed=0 | MAE=4.8008e-06 | t=0.0079s
    tikhonov | MR=0.2 | seed=0 | MAE=7.7515e-06 | t=0.0129s
    tv | MR=0.2 | seed=0 | MAE=4.0885e-06 | t=0.2928s
    trss | MR=0.2 | seed=0 | MAE=2.7686e-06 | t=0.0351s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3527e-05 | t=0.0162s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5455e-05 | t=7.2842s
    mean | MR=0.2 | seed=1 | MAE=4.1469e-06 | t=0.0037s
    nearest | MR=0.2 | seed=1 | MAE=4.7521e-06 | t=0.0077s
    tikhonov | MR=0.2 | seed=1 | MAE=7.7251e-06 | t=0.0124s
    tv | MR=0.2 | seed=1 | MAE=4.0694e-06 | t=0.2890s
    trss | MR=0.2 | seed=1 | MAE=2.7842e-06 | t=0.0333s

Completed: 2026-04-06T17:50:25.777310+00:00
Total rows: 112
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.