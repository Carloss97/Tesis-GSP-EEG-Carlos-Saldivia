# Integration Log: it78_few_missing_1ch_tv_focus
Started: 2026-04-06T06:25:23.789683
Description: 1 electrode missing, 5 datasets, TV methods focus

## Dataset: synthetic_16ch | shape=(300, 16)
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=3.8237e-01
    nearest | MR=1ch | seed=0 | MAE=7.3124e-01
    tikhonov | MR=1ch | seed=0 | MAE=4.2949e-01
    temporal_laplacian | MR=1ch | seed=0 | MAE=6.0097e-01
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.2933e-01
    tv | MR=1ch | seed=0 | MAE=4.1560e-01
    directed_tv | MR=1ch | seed=0 | MAE=3.1685e+00

## Dataset: synthetic_32ch | shape=(300, 32)
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=4.3533e-01
    nearest | MR=1ch | seed=0 | MAE=9.1141e-01
    tikhonov | MR=1ch | seed=0 | MAE=5.3104e-01
    temporal_laplacian | MR=1ch | seed=0 | MAE=6.3864e-01
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=5.3072e-01
    tv | MR=1ch | seed=0 | MAE=5.2266e-01
    directed_tv | MR=1ch | seed=0 | MAE=5.1001e+00

## Dataset: mne_sample_proxy | shape=(300, 60)
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=1.5632e-06
    nearest | MR=1ch | seed=0 | MAE=2.2388e-06
    tikhonov | MR=1ch | seed=0 | MAE=1.4417e-06
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.2467e-06
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.4415e-06
    tv | MR=1ch | seed=0 | MAE=1.5923e-06
    directed_tv | MR=1ch | seed=0 | MAE=1.3002e-06

## Dataset: bci_competition_proxy | shape=(300, 22)
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=6.5961e-06
    nearest | MR=1ch | seed=0 | MAE=8.7290e-06
    tikhonov | MR=1ch | seed=0 | MAE=7.5547e-06
    temporal_laplacian | MR=1ch | seed=0 | MAE=8.2328e-06
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=7.5457e-06
    tv | MR=1ch | seed=0 | MAE=6.6171e-06
    directed_tv | MR=1ch | seed=0 | MAE=7.2893e-06

## Dataset: bci_competition_proxy_s2 | shape=(300, 22)
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=4.4223e-06
    nearest | MR=1ch | seed=0 | MAE=5.5949e-06
    tikhonov | MR=1ch | seed=0 | MAE=4.1384e-06
    temporal_laplacian | MR=1ch | seed=0 | MAE=4.1540e-06
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.1161e-06
    tv | MR=1ch | seed=0 | MAE=4.4074e-06
    directed_tv | MR=1ch | seed=0 | MAE=4.0543e-06

Completed: 2026-04-06T06:27:22.193774
Total rows: 35