# Integration Log: it105_real_eeg_crossdataset
Started: 2026-04-06T18:47:21.304430+00:00
Description: Cross-dataset real EEG validation (PhysioNet + BCI IV 2a)

## Dataset: bci_iv2a_real_s1 | rows=168
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0038s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0052s
    tikhonov | MR=0.1 | seed=0 | MAE=4.5749e-06 | t=0.0129s
    tv | MR=0.1 | seed=0 | MAE=1.3024e-06 | t=0.3053s
    trss | MR=0.1 | seed=0 | MAE=9.1525e-07 | t=0.0337s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=9.3331e-06 | t=0.0165s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4248e-05 | t=7.2480s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0037s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0054s
    tikhonov | MR=0.1 | seed=1 | MAE=4.5276e-06 | t=0.0126s
    tv | MR=0.1 | seed=1 | MAE=1.2371e-06 | t=0.3005s
    trss | MR=0.1 | seed=1 | MAE=8.4390e-07 | t=0.0325s

## Dataset: physionet_eegmmidb_real | rows=168
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0037s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0051s
    tikhonov | MR=0.1 | seed=0 | MAE=4.5685e-06 | t=0.0134s
    tv | MR=0.1 | seed=0 | MAE=2.0331e-06 | t=0.2905s
    trss | MR=0.1 | seed=0 | MAE=9.7034e-07 | t=0.0339s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.0050e-05 | t=0.0161s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.7778e-05 | t=7.3117s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0036s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0051s
    tikhonov | MR=0.1 | seed=1 | MAE=4.5474e-06 | t=0.0128s
    tv | MR=0.1 | seed=1 | MAE=1.9934e-06 | t=0.2903s
    trss | MR=0.1 | seed=1 | MAE=9.4228e-07 | t=0.0332s

Completed: 2026-04-06T18:47:21.307813+00:00
Total rows: 336
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.