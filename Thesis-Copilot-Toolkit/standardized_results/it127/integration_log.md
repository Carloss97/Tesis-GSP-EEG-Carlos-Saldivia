# Integration Log: it127_noise_profile_non_gaussian
Started: 2026-04-07T17:41:49.060921+00:00
Description: Non-Gaussian-like noise robustness proxy

## Dataset: iris_graph_signal | rows=24
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2978e-01 | t=0.0018s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6557e-01 | t=0.0050s
    tv | MR=0.2 | seed=0 | MAE=1.2783e-01 | t=0.1055s
    trss | MR=0.2 | seed=0 | MAE=1.0513e-01 | t=0.0072s
    mean | MR=0.2 | seed=1 | MAE=1.3937e-01 | t=0.0026s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7048e-01 | t=0.0050s
    tv | MR=0.2 | seed=1 | MAE=1.3812e-01 | t=0.1050s
    trss | MR=0.2 | seed=1 | MAE=1.1294e-01 | t=0.0074s
    mean | MR=0.2 | seed=0 | MAE=1.3498e-01 | t=0.0026s
    tikhonov | MR=0.2 | seed=0 | MAE=2.7366e-01 | t=0.0050s
    tv | MR=0.2 | seed=0 | MAE=1.3427e-01 | t=0.1047s
    trss | MR=0.2 | seed=0 | MAE=1.1220e-01 | t=0.0072s

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1874e+01 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0067e+02 | t=0.0125s
    tv | MR=0.2 | seed=0 | MAE=4.4883e+01 | t=0.2888s
    trss | MR=0.2 | seed=0 | MAE=3.4060e+01 | t=0.0334s
    mean | MR=0.2 | seed=1 | MAE=4.1744e+01 | t=0.0037s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0112e+02 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=3.8391e+01 | t=0.2893s
    trss | MR=0.2 | seed=1 | MAE=3.4241e+01 | t=0.0340s
    mean | MR=0.2 | seed=0 | MAE=4.3045e+01 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0267e+02 | t=0.0127s
    tv | MR=0.2 | seed=0 | MAE=4.0372e+01 | t=0.2906s
    trss | MR=0.2 | seed=0 | MAE=3.5806e+01 | t=0.0335s

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1216e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=5.6593e-06 | t=0.0127s
    tv | MR=0.2 | seed=0 | MAE=4.0277e-06 | t=0.2905s
    trss | MR=0.2 | seed=0 | MAE=2.0376e-06 | t=0.0338s
    mean | MR=0.2 | seed=1 | MAE=4.0931e-06 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=5.6408e-06 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=3.9966e-06 | t=0.2926s
    trss | MR=0.2 | seed=1 | MAE=2.0268e-06 | t=0.0347s
    mean | MR=0.2 | seed=0 | MAE=4.2979e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=6.4201e-06 | t=0.0125s
    tv | MR=0.2 | seed=0 | MAE=4.2101e-06 | t=0.2917s
    trss | MR=0.2 | seed=0 | MAE=2.4959e-06 | t=0.0373s

Completed: 2026-04-07T17:41:49.066759+00:00
Total rows: 72
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.