# Integration Log: it84_cross_dataset_generalization_gaussian
Started: 2026-04-06T17:04:41.588326
Description: Cross-dataset generalization on Gaussian graph

## Dataset: synthetic_16ch | shape=(300, 16)
  Graph: gaussian built OK
    mean | MR=0.1 | seed=0 | MAE=5.2521e-01
    nearest | MR=0.1 | seed=0 | MAE=6.6767e-01
    tikhonov | MR=0.1 | seed=0 | MAE=5.9729e-01
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.2075e-01
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.9147e-01
    tv | MR=0.1 | seed=0 | MAE=5.0054e-01
    trss | MR=0.1 | seed=0 | MAE=4.7387e-01
    mean | MR=0.1 | seed=1 | MAE=5.2411e-01
    nearest | MR=0.1 | seed=1 | MAE=6.5848e-01
    tikhonov | MR=0.1 | seed=1 | MAE=5.8331e-01
    temporal_laplacian | MR=0.1 | seed=1 | MAE=5.2768e-01
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=4.9027e-01
    tv | MR=0.1 | seed=1 | MAE=4.9985e-01
    trss | MR=0.1 | seed=1 | MAE=4.9506e-01
    mean | MR=0.1 | seed=2 | MAE=5.2362e-01
    nearest | MR=0.1 | seed=2 | MAE=6.7339e-01
    tikhonov | MR=0.1 | seed=2 | MAE=5.8768e-01
    temporal_laplacian | MR=0.1 | seed=2 | MAE=5.2803e-01

## Dataset: mne_sample_proxy | shape=(300, 60)
  Graph: gaussian built OK
    mean | MR=0.1 | seed=0 | MAE=1.9708e-06
    nearest | MR=0.1 | seed=0 | MAE=2.5026e-06
    tikhonov | MR=0.1 | seed=0 | MAE=2.1868e-06
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.9538e-06
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.8255e-06
    tv | MR=0.1 | seed=0 | MAE=1.7934e-06
    trss | MR=0.1 | seed=0 | MAE=1.8169e-06
    mean | MR=0.1 | seed=1 | MAE=1.9782e-06
    nearest | MR=0.1 | seed=1 | MAE=2.4826e-06
    tikhonov | MR=0.1 | seed=1 | MAE=2.1649e-06
    temporal_laplacian | MR=0.1 | seed=1 | MAE=1.9936e-06
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=1.8630e-06
    tv | MR=0.1 | seed=1 | MAE=1.8306e-06
    trss | MR=0.1 | seed=1 | MAE=1.7985e-06
    mean | MR=0.1 | seed=2 | MAE=2.0281e-06
    nearest | MR=0.1 | seed=2 | MAE=2.5866e-06
    tikhonov | MR=0.1 | seed=2 | MAE=2.1996e-06
    temporal_laplacian | MR=0.1 | seed=2 | MAE=1.9406e-06

## Dataset: bci_competition_proxy | shape=(300, 22)
  Graph: gaussian built OK
    mean | MR=0.1 | seed=0 | MAE=7.9228e-06
    nearest | MR=0.1 | seed=0 | MAE=9.8465e-06
    tikhonov | MR=0.1 | seed=0 | MAE=8.6479e-06
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.0376e-06
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=7.2571e-06
    tv | MR=0.1 | seed=0 | MAE=7.5299e-06
    trss | MR=0.1 | seed=0 | MAE=7.1517e-06
    mean | MR=0.1 | seed=1 | MAE=8.0592e-06
    nearest | MR=0.1 | seed=1 | MAE=9.9305e-06
    tikhonov | MR=0.1 | seed=1 | MAE=8.7052e-06
    temporal_laplacian | MR=0.1 | seed=1 | MAE=8.1821e-06
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=7.4008e-06
    tv | MR=0.1 | seed=1 | MAE=7.4127e-06
    trss | MR=0.1 | seed=1 | MAE=7.2452e-06
    mean | MR=0.1 | seed=2 | MAE=8.0502e-06
    nearest | MR=0.1 | seed=2 | MAE=1.0009e-05
    tikhonov | MR=0.1 | seed=2 | MAE=8.6249e-06
    temporal_laplacian | MR=0.1 | seed=2 | MAE=8.2191e-06

Completed: 2026-04-06T17:04:43.208019
Total rows: 189