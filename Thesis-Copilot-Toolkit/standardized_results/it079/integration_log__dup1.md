# Integration Log: it79_few_missing_2ch_tv_focus
Started: 2026-04-06T06:27:28.290904
Description: 2 electrodes missing, 5 datasets, TV methods focus

## Dataset: synthetic_16ch | shape=(300, 16)
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=4.0763e-01
    nearest | MR=2ch | seed=0 | MAE=5.3800e-01
    tikhonov | MR=2ch | seed=0 | MAE=4.4472e-01
    temporal_laplacian | MR=2ch | seed=0 | MAE=6.9487e-01
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.4411e-01
    tv | MR=2ch | seed=0 | MAE=4.0913e-01
    directed_tv | MR=2ch | seed=0 | MAE=2.0622e+00

## Dataset: synthetic_32ch | shape=(300, 32)
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=4.8831e-01
    nearest | MR=2ch | seed=0 | MAE=5.2234e-01
    tikhonov | MR=2ch | seed=0 | MAE=4.7450e-01
    temporal_laplacian | MR=2ch | seed=0 | MAE=5.7567e-01
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.7429e-01
    tv | MR=2ch | seed=0 | MAE=4.8033e-01
    directed_tv | MR=2ch | seed=0 | MAE=3.4364e+00

## Dataset: mne_sample_proxy | shape=(300, 60)
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=1.8635e-06
    nearest | MR=2ch | seed=0 | MAE=2.4946e-06
    tikhonov | MR=2ch | seed=0 | MAE=1.7503e-06
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.7011e-06
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.7502e-06
    tv | MR=2ch | seed=0 | MAE=1.8513e-06
    directed_tv | MR=2ch | seed=0 | MAE=1.6894e-06

## Dataset: bci_competition_proxy | shape=(300, 22)
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=6.5922e-06
    nearest | MR=2ch | seed=0 | MAE=9.2209e-06
    tikhonov | MR=2ch | seed=0 | MAE=6.5288e-06
    temporal_laplacian | MR=2ch | seed=0 | MAE=8.3828e-06
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=6.5270e-06
    tv | MR=2ch | seed=0 | MAE=6.5790e-06
    directed_tv | MR=2ch | seed=0 | MAE=7.3732e-06

## Dataset: bci_competition_proxy_s2 | shape=(300, 22)
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=4.4191e-06
    nearest | MR=2ch | seed=0 | MAE=6.7749e-06
    tikhonov | MR=2ch | seed=0 | MAE=4.3097e-06
    temporal_laplacian | MR=2ch | seed=0 | MAE=4.2443e-06
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.2901e-06
    tv | MR=2ch | seed=0 | MAE=4.4123e-06
    directed_tv | MR=2ch | seed=0 | MAE=4.0722e-06

Completed: 2026-04-06T06:29:26.141557
Total rows: 35