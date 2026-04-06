# Integration Log: it114_eeg_vs_iris_transfer
Started: 2026-04-06T19:46:08.341861+00:00
Description: EEG vs Iris transfer comparison

## Dataset: bci_iv2a_real_s1 | rows=126
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0037s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0051s
    tikhonov | MR=0.1 | seed=0 | MAE=4.5749e-06 | t=0.0128s
    tv | MR=0.1 | seed=0 | MAE=1.3024e-06 | t=0.2934s
    trss | MR=0.1 | seed=0 | MAE=9.1525e-07 | t=0.0349s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=9.3331e-06 | t=0.0163s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4248e-05 | t=7.3009s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0036s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0051s
    tikhonov | MR=0.1 | seed=1 | MAE=4.5276e-06 | t=0.0127s
    tv | MR=0.1 | seed=1 | MAE=1.2371e-06 | t=0.2953s
    trss | MR=0.1 | seed=1 | MAE=8.4390e-07 | t=0.0334s

## Dataset: iris_graph_signal | rows=126
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0018s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0018s
    tikhonov | MR=0.1 | seed=0 | MAE=2.6471e-01 | t=0.0050s
    tv | MR=0.1 | seed=0 | MAE=1.2578e-01 | t=0.1033s
    trss | MR=0.1 | seed=0 | MAE=1.0362e-01 | t=0.0073s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1982e-01 | t=0.0075s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.3675e-01 | t=0.0150s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0027s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0018s
    tikhonov | MR=0.1 | seed=1 | MAE=2.6943e-01 | t=0.0051s
    tv | MR=0.1 | seed=1 | MAE=1.3774e-01 | t=0.1033s
    trss | MR=0.1 | seed=1 | MAE=1.1253e-01 | t=0.0074s

## Dataset: physionet_eegmmidb_real | rows=126
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0037s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0051s
    tikhonov | MR=0.1 | seed=0 | MAE=4.5685e-06 | t=0.0128s
    tv | MR=0.1 | seed=0 | MAE=2.0331e-06 | t=0.2847s
    trss | MR=0.1 | seed=0 | MAE=9.7034e-07 | t=0.0331s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.0050e-05 | t=0.0164s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.7778e-05 | t=7.2988s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0037s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0051s
    tikhonov | MR=0.1 | seed=1 | MAE=4.5474e-06 | t=0.0131s
    tv | MR=0.1 | seed=1 | MAE=1.9934e-06 | t=0.2847s
    trss | MR=0.1 | seed=1 | MAE=9.4228e-07 | t=0.0336s

Completed: 2026-04-06T19:46:08.348146+00:00
Total rows: 378
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.