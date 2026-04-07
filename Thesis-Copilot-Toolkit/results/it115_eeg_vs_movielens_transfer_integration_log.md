# Integration Log: it115_eeg_vs_movielens_transfer
Started: 2026-04-06T20:02:36.085773+00:00
Description: EEG vs MovieLens transfer comparison

## Dataset: bci_iv2a_real_s1 | rows=126
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0039s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0051s
    tikhonov | MR=0.1 | seed=0 | MAE=4.5749e-06 | t=0.0126s
    tv | MR=0.1 | seed=0 | MAE=1.3024e-06 | t=0.2937s
    trss | MR=0.1 | seed=0 | MAE=9.1525e-07 | t=0.0332s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=9.3331e-06 | t=0.0161s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4248e-05 | t=7.2693s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0043s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0052s
    tikhonov | MR=0.1 | seed=1 | MAE=4.5276e-06 | t=0.0125s
    tv | MR=0.1 | seed=1 | MAE=1.2371e-06 | t=0.2938s
    trss | MR=0.1 | seed=1 | MAE=8.4390e-07 | t=0.0329s

## Dataset: movielens_graph_signal | rows=126
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0037s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0052s
    tikhonov | MR=0.1 | seed=0 | MAE=5.9092e-02 | t=0.0126s
    tv | MR=0.1 | seed=0 | MAE=1.4570e-02 | t=0.2855s
    trss | MR=0.1 | seed=0 | MAE=1.7555e-02 | t=0.0337s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.3606e-01 | t=0.0160s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4080e-01 | t=7.2953s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0036s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0051s
    tikhonov | MR=0.1 | seed=1 | MAE=6.4536e-02 | t=0.0125s
    tv | MR=0.1 | seed=1 | MAE=1.9193e-02 | t=0.2824s
    trss | MR=0.1 | seed=1 | MAE=2.7197e-02 | t=0.0331s

## Dataset: physionet_eegmmidb_real | rows=126
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0038s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0052s
    tikhonov | MR=0.1 | seed=0 | MAE=4.5685e-06 | t=0.0130s
    tv | MR=0.1 | seed=0 | MAE=2.0331e-06 | t=0.2880s
    trss | MR=0.1 | seed=0 | MAE=9.7034e-07 | t=0.0329s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.0050e-05 | t=0.0161s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.7778e-05 | t=7.3362s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0037s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0052s
    tikhonov | MR=0.1 | seed=1 | MAE=4.5474e-06 | t=0.0124s
    tv | MR=0.1 | seed=1 | MAE=1.9934e-06 | t=0.2849s
    trss | MR=0.1 | seed=1 | MAE=9.4228e-07 | t=0.0324s

Completed: 2026-04-06T20:02:36.090710+00:00
Total rows: 378
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.