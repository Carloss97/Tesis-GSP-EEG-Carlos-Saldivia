# Integration Log: it129_confidence_interval_stability
Started: 2026-04-07T17:44:34.995581+00:00
Description: Bootstrap stability of GO/NO-GO

## Dataset: bci_iv2a_real_s1 | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=2.4466e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=5.4376e-06 | t=0.0126s
    tv | MR=0.2 | seed=0 | MAE=2.4464e-06 | t=0.2993s
    trss | MR=0.2 | seed=0 | MAE=1.6619e-06 | t=0.0337s
    mean | MR=0.2 | seed=1 | MAE=2.4913e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=1 | MAE=5.4520e-06 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=2.4911e-06 | t=0.2989s
    trss | MR=0.2 | seed=1 | MAE=1.7407e-06 | t=0.0327s

## Dataset: iris_graph_signal | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0017s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6471e-01 | t=0.0049s
    tv | MR=0.2 | seed=0 | MAE=1.2578e-01 | t=0.1038s
    trss | MR=0.2 | seed=0 | MAE=1.0362e-01 | t=0.0072s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0026s
    tikhonov | MR=0.2 | seed=1 | MAE=2.6943e-01 | t=0.0049s
    tv | MR=0.2 | seed=1 | MAE=1.3774e-01 | t=0.1054s
    trss | MR=0.2 | seed=1 | MAE=1.1253e-01 | t=0.0072s

## Dataset: iv100hz_mat | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1733e+01 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0048e+02 | t=0.0129s
    tv | MR=0.2 | seed=0 | MAE=3.9792e+01 | t=0.2905s
    trss | MR=0.2 | seed=0 | MAE=3.3793e+01 | t=0.0334s
    mean | MR=0.2 | seed=1 | MAE=4.1650e+01 | t=0.0037s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0097e+02 | t=0.0127s
    tv | MR=0.2 | seed=1 | MAE=4.0705e+01 | t=0.2902s
    trss | MR=0.2 | seed=1 | MAE=3.4227e+01 | t=0.0330s

## Dataset: physionet_eegmmidb_real | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1027e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=5.5530e-06 | t=0.0126s
    tv | MR=0.2 | seed=0 | MAE=4.0081e-06 | t=0.2928s
    trss | MR=0.2 | seed=0 | MAE=1.9701e-06 | t=0.0328s
    mean | MR=0.2 | seed=1 | MAE=4.0539e-06 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=5.5283e-06 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=3.9560e-06 | t=0.2914s
    trss | MR=0.2 | seed=1 | MAE=1.9551e-06 | t=0.0346s

Completed: 2026-04-07T17:44:35.002779+00:00
Total rows: 32
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.