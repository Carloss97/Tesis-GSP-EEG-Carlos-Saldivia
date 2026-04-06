# Integration Log: it107_mat100hz_baseline
Started: 2026-04-06T19:04:27.687700+00:00
Description: 100Hz MAT baseline validation

## Dataset: iv100hz_mat | rows=420
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0036s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0051s
    tikhonov | MR=0.1 | seed=0 | MAE=1.3433e+02 | t=0.0128s
    tv | MR=0.1 | seed=0 | MAE=1.1963e+01 | t=0.3778s
    trss | MR=0.1 | seed=0 | MAE=1.3969e+01 | t=0.0332s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.0474e+02 | t=0.0164s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.6591e+02 | t=7.3021s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0037s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0051s
    tikhonov | MR=0.1 | seed=1 | MAE=1.3439e+02 | t=0.0128s
    tv | MR=0.1 | seed=1 | MAE=1.2576e+01 | t=0.3771s
    trss | MR=0.1 | seed=1 | MAE=1.4213e+01 | t=0.0330s
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0037s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0051s
    tikhonov | MR=0.1 | seed=0 | MAE=8.2813e+01 | t=0.0129s
    tv | MR=0.1 | seed=0 | MAE=1.6144e+01 | t=0.2915s
    trss | MR=0.1 | seed=0 | MAE=1.5723e+01 | t=0.0336s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.5864e+02 | t=0.0164s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.9459e+02 | t=7.3423s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0036s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0051s
    tikhonov | MR=0.1 | seed=1 | MAE=8.3408e+01 | t=0.0130s
    tv | MR=0.1 | seed=1 | MAE=1.8592e+01 | t=0.2921s
    trss | MR=0.1 | seed=1 | MAE=1.6440e+01 | t=0.0328s

Completed: 2026-04-06T19:04:27.690483+00:00
Total rows: 420
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.