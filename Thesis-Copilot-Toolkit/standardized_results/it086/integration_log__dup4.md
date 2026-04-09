# Integration Log: it86_cross_dataset_generalization_high_mr
Started: 2026-04-06T17:04:44.929754
Description: Cross-dataset generalization at high missing ratios

## Dataset: synthetic_16ch | shape=(300, 16)
  Graph: knn__k3 built OK
    mean | MR=0.3 | seed=0 | MAE=5.6150e-01
    nearest | MR=0.3 | seed=0 | MAE=7.1823e-01
    tikhonov | MR=0.3 | seed=0 | MAE=6.1046e-01
    temporal_laplacian | MR=0.3 | seed=0 | MAE=5.2137e-01
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=4.9656e-01
    tv | MR=0.3 | seed=0 | MAE=4.8751e-01
    trss | MR=0.3 | seed=0 | MAE=4.7945e-01
    mean | MR=0.3 | seed=1 | MAE=5.4602e-01
    nearest | MR=0.3 | seed=1 | MAE=6.8775e-01
    tikhonov | MR=0.3 | seed=1 | MAE=6.1318e-01
    temporal_laplacian | MR=0.3 | seed=1 | MAE=5.2485e-01
    graph_time_tikhonov | MR=0.3 | seed=1 | MAE=4.8652e-01
    tv | MR=0.3 | seed=1 | MAE=4.6972e-01
    trss | MR=0.3 | seed=1 | MAE=4.8474e-01
    mean | MR=0.3 | seed=2 | MAE=5.4011e-01
    nearest | MR=0.3 | seed=2 | MAE=7.1442e-01
    tikhonov | MR=0.3 | seed=2 | MAE=6.0568e-01
    temporal_laplacian | MR=0.3 | seed=2 | MAE=5.2523e-01
  Graph: gaussian built OK
    mean | MR=0.3 | seed=0 | MAE=6.0811e-01
    nearest | MR=0.3 | seed=0 | MAE=7.2785e-01
    tikhonov | MR=0.3 | seed=0 | MAE=6.4841e-01
    temporal_laplacian | MR=0.3 | seed=0 | MAE=5.6168e-01
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=4.9834e-01
    tv | MR=0.3 | seed=0 | MAE=4.9427e-01
    trss | MR=0.3 | seed=0 | MAE=5.0175e-01
    mean | MR=0.3 | seed=1 | MAE=6.0253e-01
    nearest | MR=0.3 | seed=1 | MAE=7.3853e-01
    tikhonov | MR=0.3 | seed=1 | MAE=6.4923e-01
    temporal_laplacian | MR=0.3 | seed=1 | MAE=5.4027e-01
    graph_time_tikhonov | MR=0.3 | seed=1 | MAE=5.0928e-01
    tv | MR=0.3 | seed=1 | MAE=4.8673e-01
    trss | MR=0.3 | seed=1 | MAE=4.9433e-01
    mean | MR=0.3 | seed=2 | MAE=5.9263e-01
    nearest | MR=0.3 | seed=2 | MAE=7.3362e-01
    tikhonov | MR=0.3 | seed=2 | MAE=6.5087e-01
    temporal_laplacian | MR=0.3 | seed=2 | MAE=5.3712e-01

## Dataset: mne_sample_proxy | shape=(300, 60)
  Graph: knn__k3 built OK
    mean | MR=0.3 | seed=0 | MAE=2.1102e-06
    nearest | MR=0.3 | seed=0 | MAE=2.6368e-06
    tikhonov | MR=0.3 | seed=0 | MAE=2.2571e-06
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.9725e-06
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.8968e-06
    tv | MR=0.3 | seed=0 | MAE=1.8433e-06
    trss | MR=0.3 | seed=0 | MAE=1.7697e-06
    mean | MR=0.3 | seed=1 | MAE=2.0554e-06
    nearest | MR=0.3 | seed=1 | MAE=2.6627e-06
    tikhonov | MR=0.3 | seed=1 | MAE=2.2968e-06
    temporal_laplacian | MR=0.3 | seed=1 | MAE=2.0362e-06
    graph_time_tikhonov | MR=0.3 | seed=1 | MAE=1.8841e-06
    tv | MR=0.3 | seed=1 | MAE=1.8106e-06
    trss | MR=0.3 | seed=1 | MAE=1.7475e-06
    mean | MR=0.3 | seed=2 | MAE=2.0176e-06
    nearest | MR=0.3 | seed=2 | MAE=2.6305e-06
    tikhonov | MR=0.3 | seed=2 | MAE=2.3264e-06
    temporal_laplacian | MR=0.3 | seed=2 | MAE=1.9716e-06
  Graph: gaussian built OK
    mean | MR=0.3 | seed=0 | MAE=2.1579e-06
    nearest | MR=0.3 | seed=0 | MAE=2.7616e-06
    tikhonov | MR=0.3 | seed=0 | MAE=2.3705e-06
    temporal_laplacian | MR=0.3 | seed=0 | MAE=2.0476e-06
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.9178e-06
    tv | MR=0.3 | seed=0 | MAE=2.0124e-06
    trss | MR=0.3 | seed=0 | MAE=1.8124e-06
    mean | MR=0.3 | seed=1 | MAE=2.2045e-06
    nearest | MR=0.3 | seed=1 | MAE=2.6760e-06
    tikhonov | MR=0.3 | seed=1 | MAE=2.4501e-06
    temporal_laplacian | MR=0.3 | seed=1 | MAE=1.8653e-06
    graph_time_tikhonov | MR=0.3 | seed=1 | MAE=1.9292e-06
    tv | MR=0.3 | seed=1 | MAE=1.8527e-06
    trss | MR=0.3 | seed=1 | MAE=1.8984e-06
    mean | MR=0.3 | seed=2 | MAE=2.2967e-06
    nearest | MR=0.3 | seed=2 | MAE=2.7324e-06
    tikhonov | MR=0.3 | seed=2 | MAE=2.3835e-06
    temporal_laplacian | MR=0.3 | seed=2 | MAE=2.0309e-06

## Dataset: bci_competition_proxy | shape=(300, 22)
  Graph: knn__k3 built OK
    mean | MR=0.3 | seed=0 | MAE=8.4372e-06
    nearest | MR=0.3 | seed=0 | MAE=1.0369e-05
    tikhonov | MR=0.3 | seed=0 | MAE=9.1476e-06
    temporal_laplacian | MR=0.3 | seed=0 | MAE=7.9668e-06
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=7.5341e-06
    tv | MR=0.3 | seed=0 | MAE=7.1110e-06
    trss | MR=0.3 | seed=0 | MAE=7.2132e-06
    mean | MR=0.3 | seed=1 | MAE=8.4876e-06
    nearest | MR=0.3 | seed=1 | MAE=1.0582e-05
    tikhonov | MR=0.3 | seed=1 | MAE=9.1410e-06
    temporal_laplacian | MR=0.3 | seed=1 | MAE=7.8196e-06
    graph_time_tikhonov | MR=0.3 | seed=1 | MAE=7.2881e-06
    tv | MR=0.3 | seed=1 | MAE=7.1444e-06
    trss | MR=0.3 | seed=1 | MAE=7.0368e-06
    mean | MR=0.3 | seed=2 | MAE=7.9980e-06
    nearest | MR=0.3 | seed=2 | MAE=1.0272e-05
    tikhonov | MR=0.3 | seed=2 | MAE=9.3139e-06
    temporal_laplacian | MR=0.3 | seed=2 | MAE=8.0247e-06
  Graph: gaussian built OK
    mean | MR=0.3 | seed=0 | MAE=8.7006e-06
    nearest | MR=0.3 | seed=0 | MAE=1.1080e-05
    tikhonov | MR=0.3 | seed=0 | MAE=9.3549e-06
    temporal_laplacian | MR=0.3 | seed=0 | MAE=8.1607e-06
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=7.7230e-06
    tv | MR=0.3 | seed=0 | MAE=7.3393e-06
    trss | MR=0.3 | seed=0 | MAE=7.2634e-06
    mean | MR=0.3 | seed=1 | MAE=8.9025e-06
    nearest | MR=0.3 | seed=1 | MAE=1.1129e-05
    tikhonov | MR=0.3 | seed=1 | MAE=9.4622e-06
    temporal_laplacian | MR=0.3 | seed=1 | MAE=8.1215e-06
    graph_time_tikhonov | MR=0.3 | seed=1 | MAE=7.6378e-06
    tv | MR=0.3 | seed=1 | MAE=7.2970e-06
    trss | MR=0.3 | seed=1 | MAE=7.6781e-06
    mean | MR=0.3 | seed=2 | MAE=8.6108e-06
    nearest | MR=0.3 | seed=2 | MAE=1.0567e-05
    tikhonov | MR=0.3 | seed=2 | MAE=9.9017e-06
    temporal_laplacian | MR=0.3 | seed=2 | MAE=7.9375e-06

Completed: 2026-04-06T17:04:46.637269
Total rows: 252