# Integration Log: it123_graph_density_calibration
Started: 2026-04-07T17:41:13.770599+00:00
Description: Graph density calibration sweep

## Dataset: iv100hz_mat | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1733e+01 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0048e+02 | t=0.0125s
    tv | MR=0.2 | seed=0 | MAE=3.9792e+01 | t=0.2877s
    trss | MR=0.2 | seed=0 | MAE=3.3793e+01 | t=0.0333s
    mean | MR=0.2 | seed=1 | MAE=4.1650e+01 | t=0.0037s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0097e+02 | t=0.0123s
    tv | MR=0.2 | seed=1 | MAE=4.0705e+01 | t=0.2850s
    trss | MR=0.2 | seed=1 | MAE=3.4227e+01 | t=0.0329s

## Dataset: movielens_graph_signal | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=3.2705e-02 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=7.0617e-02 | t=0.0129s
    tv | MR=0.2 | seed=0 | MAE=3.2550e-02 | t=0.2909s
    trss | MR=0.2 | seed=0 | MAE=4.0337e-02 | t=0.0328s
    mean | MR=0.2 | seed=1 | MAE=3.6242e-02 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=7.7216e-02 | t=0.0125s
    tv | MR=0.2 | seed=1 | MAE=3.6317e-02 | t=0.3003s
    trss | MR=0.2 | seed=1 | MAE=4.8531e-02 | t=0.0329s

## Dataset: physionet_eegmmidb_real | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1027e-06 | t=0.0037s
    tikhonov | MR=0.2 | seed=0 | MAE=5.5530e-06 | t=0.0130s
    tv | MR=0.2 | seed=0 | MAE=4.0081e-06 | t=0.3057s
    trss | MR=0.2 | seed=0 | MAE=1.9701e-06 | t=0.0340s
    mean | MR=0.2 | seed=1 | MAE=4.0539e-06 | t=0.0036s
    tikhonov | MR=0.2 | seed=1 | MAE=5.5283e-06 | t=0.0143s
    tv | MR=0.2 | seed=1 | MAE=3.9560e-06 | t=0.2881s
    trss | MR=0.2 | seed=1 | MAE=1.9551e-06 | t=0.0330s

Completed: 2026-04-07T17:41:13.774864+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.