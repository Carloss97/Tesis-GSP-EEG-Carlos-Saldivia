# Integration Log: it124_missing_pattern_realistic_v2
Started: 2026-04-07T17:41:22.919614+00:00
Description: Realistic missing-pattern stress test v2

## Dataset: bci_iv2a_real_s1 | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=2.4466e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=5.4376e-06 | t=0.0125s
    tv | MR=0.2 | seed=0 | MAE=2.4464e-06 | t=0.3527s
    trss | MR=0.2 | seed=0 | MAE=1.6619e-06 | t=0.0354s
    mean | MR=0.2 | seed=1 | MAE=2.4913e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=1 | MAE=5.4520e-06 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=2.4911e-06 | t=0.2995s
    trss | MR=0.2 | seed=1 | MAE=1.7407e-06 | t=0.0346s

## Dataset: bci_iv2a_real_s2 | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.1855e-07 | t=0.0038s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6739e-06 | t=0.0124s
    tv | MR=0.2 | seed=0 | MAE=7.1857e-07 | t=0.2986s
    trss | MR=0.2 | seed=0 | MAE=6.1411e-07 | t=0.0338s
    mean | MR=0.2 | seed=1 | MAE=7.0041e-07 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=1.6581e-06 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=7.0041e-07 | t=0.2982s
    trss | MR=0.2 | seed=1 | MAE=5.9749e-07 | t=0.0327s

## Dataset: physionet_eegmmidb_real | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1027e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=5.5530e-06 | t=0.0127s
    tv | MR=0.2 | seed=0 | MAE=4.0081e-06 | t=0.2918s
    trss | MR=0.2 | seed=0 | MAE=1.9701e-06 | t=0.0327s
    mean | MR=0.2 | seed=1 | MAE=4.0539e-06 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=5.5283e-06 | t=0.0125s
    tv | MR=0.2 | seed=1 | MAE=3.9560e-06 | t=0.3353s
    trss | MR=0.2 | seed=1 | MAE=1.9551e-06 | t=0.0324s

Completed: 2026-04-07T17:41:22.924084+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.