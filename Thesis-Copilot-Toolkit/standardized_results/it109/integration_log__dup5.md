# Integration Log: it109_mat100hz_noise_sensitivity
Started: 2026-04-06T19:16:10.498525+00:00
Description: 100Hz MAT noise sensitivity

## Dataset: iv100hz_mat | rows=168
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.2161e+01 | t=0.0036s
    nearest | MR=0.2 | seed=0 | MAE=6.5284e+01 | t=0.0077s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0115e+02 | t=0.0123s
    tv | MR=0.2 | seed=0 | MAE=4.3129e+01 | t=0.2806s
    trss | MR=0.2 | seed=0 | MAE=3.4461e+01 | t=0.0349s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6809e+02 | t=0.0157s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0378e+02 | t=7.2304s
    mean | MR=0.2 | seed=1 | MAE=4.1947e+01 | t=0.0036s
    nearest | MR=0.2 | seed=1 | MAE=6.5604e+01 | t=0.0076s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0156e+02 | t=0.0122s
    tv | MR=0.2 | seed=1 | MAE=4.1885e+01 | t=0.2885s
    trss | MR=0.2 | seed=1 | MAE=3.4520e+01 | t=0.0331s

Completed: 2026-04-06T19:16:10.499939+00:00
Total rows: 168
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.