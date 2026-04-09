# Integration Log: it125_temporal_window_sensitivity
Started: 2026-04-07T17:41:31.899645+00:00
Description: Temporal window sensitivity proxy

## Dataset: bci_iv2a_real_s1 | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=2.4466e-06 | t=0.0038s
    tikhonov | MR=0.2 | seed=0 | MAE=5.4376e-06 | t=0.0126s
    tv | MR=0.2 | seed=0 | MAE=2.4464e-06 | t=0.3013s
    trss | MR=0.2 | seed=0 | MAE=1.6619e-06 | t=0.0371s
    mean | MR=0.2 | seed=1 | MAE=2.4913e-06 | t=0.0039s
    tikhonov | MR=0.2 | seed=1 | MAE=5.4520e-06 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=2.4911e-06 | t=0.2988s
    trss | MR=0.2 | seed=1 | MAE=1.7407e-06 | t=0.0337s

## Dataset: iv100hz_mat | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1733e+01 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0048e+02 | t=0.0125s
    tv | MR=0.2 | seed=0 | MAE=3.9792e+01 | t=0.2899s
    trss | MR=0.2 | seed=0 | MAE=3.3793e+01 | t=0.0345s
    mean | MR=0.2 | seed=1 | MAE=4.1650e+01 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0097e+02 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=4.0705e+01 | t=0.2898s
    trss | MR=0.2 | seed=1 | MAE=3.4227e+01 | t=0.0336s

## Dataset: physionet_eegmmidb_real | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1027e-06 | t=0.0038s
    tikhonov | MR=0.2 | seed=0 | MAE=5.5530e-06 | t=0.0125s
    tv | MR=0.2 | seed=0 | MAE=4.0081e-06 | t=0.2902s
    trss | MR=0.2 | seed=0 | MAE=1.9701e-06 | t=0.0334s
    mean | MR=0.2 | seed=1 | MAE=4.0539e-06 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=5.5283e-06 | t=0.0124s
    tv | MR=0.2 | seed=1 | MAE=3.9560e-06 | t=0.2897s
    trss | MR=0.2 | seed=1 | MAE=1.9551e-06 | t=0.0333s

Completed: 2026-04-07T17:41:31.904236+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.