# Integration Log: it130_final_decision_matrix
Started: 2026-04-07T17:44:49.492746+00:00
Description: Final conditional decision matrix

## Dataset: bci_iv2a_real_s1 | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=2.4466e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=5.4376e-06 | t=0.0128s
    tv | MR=0.2 | seed=0 | MAE=2.4464e-06 | t=0.2987s
    trss | MR=0.2 | seed=0 | MAE=1.6619e-06 | t=0.0351s
    mean | MR=0.2 | seed=1 | MAE=2.4913e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=1 | MAE=5.4520e-06 | t=0.0125s
    tv | MR=0.2 | seed=1 | MAE=2.4911e-06 | t=0.2996s
    trss | MR=0.2 | seed=1 | MAE=1.7407e-06 | t=0.0418s

## Dataset: bci_iv2a_real_s2 | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.1855e-07 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6739e-06 | t=0.0125s
    tv | MR=0.2 | seed=0 | MAE=7.1857e-07 | t=0.2986s
    trss | MR=0.2 | seed=0 | MAE=6.1411e-07 | t=0.0332s
    mean | MR=0.2 | seed=1 | MAE=7.0041e-07 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=1.6581e-06 | t=0.0132s
    tv | MR=0.2 | seed=1 | MAE=7.0041e-07 | t=0.2970s
    trss | MR=0.2 | seed=1 | MAE=5.9749e-07 | t=0.0335s

## Dataset: iris_graph_signal | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0017s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6471e-01 | t=0.0053s
    tv | MR=0.2 | seed=0 | MAE=1.2578e-01 | t=0.1025s
    trss | MR=0.2 | seed=0 | MAE=1.0362e-01 | t=0.0072s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0026s
    tikhonov | MR=0.2 | seed=1 | MAE=2.6943e-01 | t=0.0050s
    tv | MR=0.2 | seed=1 | MAE=1.3774e-01 | t=0.1018s
    trss | MR=0.2 | seed=1 | MAE=1.1253e-01 | t=0.0073s

## Dataset: iv100hz_mat | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1733e+01 | t=0.0038s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0048e+02 | t=0.0126s
    tv | MR=0.2 | seed=0 | MAE=3.9792e+01 | t=0.2872s
    trss | MR=0.2 | seed=0 | MAE=3.3793e+01 | t=0.0332s
    mean | MR=0.2 | seed=1 | MAE=4.1650e+01 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0097e+02 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=4.0705e+01 | t=0.2908s
    trss | MR=0.2 | seed=1 | MAE=3.4227e+01 | t=0.0351s

## Dataset: movielens_graph_signal | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=3.2705e-02 | t=0.0056s
    tikhonov | MR=0.2 | seed=0 | MAE=7.0617e-02 | t=0.0125s
    tv | MR=0.2 | seed=0 | MAE=3.2550e-02 | t=0.2869s
    trss | MR=0.2 | seed=0 | MAE=4.0337e-02 | t=0.0329s
    mean | MR=0.2 | seed=1 | MAE=3.6242e-02 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=7.7216e-02 | t=0.0125s
    tv | MR=0.2 | seed=1 | MAE=3.6317e-02 | t=0.2873s
    trss | MR=0.2 | seed=1 | MAE=4.8531e-02 | t=0.0332s

## Dataset: physionet_eegmmidb_real | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1027e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=5.5530e-06 | t=0.0125s
    tv | MR=0.2 | seed=0 | MAE=4.0081e-06 | t=0.2904s
    trss | MR=0.2 | seed=0 | MAE=1.9701e-06 | t=0.0337s
    mean | MR=0.2 | seed=1 | MAE=4.0539e-06 | t=0.0039s
    tikhonov | MR=0.2 | seed=1 | MAE=5.5283e-06 | t=0.0128s
    tv | MR=0.2 | seed=1 | MAE=3.9560e-06 | t=0.2910s
    trss | MR=0.2 | seed=1 | MAE=1.9551e-06 | t=0.0333s

Completed: 2026-04-07T17:44:49.501007+00:00
Total rows: 48
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.