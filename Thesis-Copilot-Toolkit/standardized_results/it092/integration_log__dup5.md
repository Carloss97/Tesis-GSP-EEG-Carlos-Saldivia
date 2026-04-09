# Integration Log: it92_robustness_low_missing_stability
Started: 2026-04-06T17:04:55.123976
Description: Stability at low missing ratios

## Dataset: synthetic_32ch | shape=(300, 32)
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=4.5381e-01
    nearest | MR=0.1 | seed=0 | MAE=5.4748e-01
    tikhonov | MR=0.1 | seed=0 | MAE=4.9493e-01
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.1973e-01
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1260e-01
    tv | MR=0.1 | seed=0 | MAE=3.9985e-01
    trss | MR=0.1 | seed=0 | MAE=3.8914e-01
    mean | MR=0.1 | seed=1 | MAE=4.5674e-01
    nearest | MR=0.1 | seed=1 | MAE=5.5100e-01
    tikhonov | MR=0.1 | seed=1 | MAE=4.9843e-01
    temporal_laplacian | MR=0.1 | seed=1 | MAE=4.2200e-01
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=4.1136e-01
    tv | MR=0.1 | seed=1 | MAE=3.7943e-01
    trss | MR=0.1 | seed=1 | MAE=3.8699e-01
    mean | MR=0.1 | seed=2 | MAE=4.5026e-01
    nearest | MR=0.1 | seed=2 | MAE=5.6073e-01
    tikhonov | MR=0.1 | seed=2 | MAE=4.8377e-01
    temporal_laplacian | MR=0.1 | seed=2 | MAE=4.2480e-01
  Graph: gaussian built OK
    mean | MR=0.1 | seed=0 | MAE=4.7831e-01
    nearest | MR=0.1 | seed=0 | MAE=5.6980e-01
    tikhonov | MR=0.1 | seed=0 | MAE=4.9219e-01
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.4781e-01
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1249e-01
    tv | MR=0.1 | seed=0 | MAE=4.2391e-01
    trss | MR=0.1 | seed=0 | MAE=4.1666e-01
    mean | MR=0.1 | seed=1 | MAE=4.4313e-01
    nearest | MR=0.1 | seed=1 | MAE=5.7998e-01
    tikhonov | MR=0.1 | seed=1 | MAE=5.2434e-01
    temporal_laplacian | MR=0.1 | seed=1 | MAE=4.5348e-01
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=4.1581e-01
    tv | MR=0.1 | seed=1 | MAE=4.0657e-01
    trss | MR=0.1 | seed=1 | MAE=4.0075e-01
    mean | MR=0.1 | seed=2 | MAE=4.7069e-01
    nearest | MR=0.1 | seed=2 | MAE=5.8463e-01
    tikhonov | MR=0.1 | seed=2 | MAE=5.1169e-01
    temporal_laplacian | MR=0.1 | seed=2 | MAE=4.5831e-01

## Dataset: mne_sample_proxy | shape=(300, 60)
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.8678e-06
    nearest | MR=0.1 | seed=0 | MAE=2.3661e-06
    tikhonov | MR=0.1 | seed=0 | MAE=2.1095e-06
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.8538e-06
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.7841e-06
    tv | MR=0.1 | seed=0 | MAE=1.7379e-06
    trss | MR=0.1 | seed=0 | MAE=1.7031e-06
    mean | MR=0.1 | seed=1 | MAE=1.9363e-06
    nearest | MR=0.1 | seed=1 | MAE=2.3298e-06
    tikhonov | MR=0.1 | seed=1 | MAE=2.1421e-06
    temporal_laplacian | MR=0.1 | seed=1 | MAE=1.8367e-06
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=1.7784e-06
    tv | MR=0.1 | seed=1 | MAE=1.6687e-06
    trss | MR=0.1 | seed=1 | MAE=1.6822e-06
    mean | MR=0.1 | seed=2 | MAE=1.9039e-06
    nearest | MR=0.1 | seed=2 | MAE=2.3090e-06
    tikhonov | MR=0.1 | seed=2 | MAE=2.1505e-06
    temporal_laplacian | MR=0.1 | seed=2 | MAE=1.8582e-06
  Graph: gaussian built OK
    mean | MR=0.1 | seed=0 | MAE=2.0008e-06
    nearest | MR=0.1 | seed=0 | MAE=2.4952e-06
    tikhonov | MR=0.1 | seed=0 | MAE=2.1546e-06
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.9015e-06
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.8371e-06
    tv | MR=0.1 | seed=0 | MAE=1.8684e-06
    trss | MR=0.1 | seed=0 | MAE=1.6997e-06
    mean | MR=0.1 | seed=1 | MAE=1.9462e-06
    nearest | MR=0.1 | seed=1 | MAE=2.5084e-06
    tikhonov | MR=0.1 | seed=1 | MAE=2.2988e-06
    temporal_laplacian | MR=0.1 | seed=1 | MAE=1.8429e-06
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=1.7852e-06
    tv | MR=0.1 | seed=1 | MAE=1.7719e-06
    trss | MR=0.1 | seed=1 | MAE=1.7205e-06
    mean | MR=0.1 | seed=2 | MAE=1.9987e-06
    nearest | MR=0.1 | seed=2 | MAE=2.5129e-06
    tikhonov | MR=0.1 | seed=2 | MAE=2.1630e-06
    temporal_laplacian | MR=0.1 | seed=2 | MAE=1.9492e-06

## Dataset: bci_competition_proxy | shape=(300, 22)
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=7.8803e-06
    nearest | MR=0.1 | seed=0 | MAE=9.6211e-06
    tikhonov | MR=0.1 | seed=0 | MAE=8.4588e-06
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.0025e-06
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=7.1682e-06
    tv | MR=0.1 | seed=0 | MAE=6.7544e-06
    trss | MR=0.1 | seed=0 | MAE=6.6074e-06
    mean | MR=0.1 | seed=1 | MAE=7.7983e-06
    nearest | MR=0.1 | seed=1 | MAE=9.6901e-06
    tikhonov | MR=0.1 | seed=1 | MAE=8.0747e-06
    temporal_laplacian | MR=0.1 | seed=1 | MAE=7.3881e-06
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=7.1242e-06
    tv | MR=0.1 | seed=1 | MAE=6.9256e-06
    trss | MR=0.1 | seed=1 | MAE=6.7651e-06
    mean | MR=0.1 | seed=2 | MAE=7.7708e-06
    nearest | MR=0.1 | seed=2 | MAE=9.5381e-06
    tikhonov | MR=0.1 | seed=2 | MAE=8.1675e-06
    temporal_laplacian | MR=0.1 | seed=2 | MAE=7.3887e-06
  Graph: gaussian built OK
    mean | MR=0.1 | seed=0 | MAE=8.0331e-06
    nearest | MR=0.1 | seed=0 | MAE=1.0001e-05
    tikhonov | MR=0.1 | seed=0 | MAE=8.6736e-06
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.3240e-06
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=7.5020e-06
    tv | MR=0.1 | seed=0 | MAE=7.3357e-06
    trss | MR=0.1 | seed=0 | MAE=7.2874e-06
    mean | MR=0.1 | seed=1 | MAE=8.1437e-06
    nearest | MR=0.1 | seed=1 | MAE=9.9971e-06
    tikhonov | MR=0.1 | seed=1 | MAE=8.9705e-06
    temporal_laplacian | MR=0.1 | seed=1 | MAE=7.9245e-06
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=7.1951e-06
    tv | MR=0.1 | seed=1 | MAE=7.0671e-06
    trss | MR=0.1 | seed=1 | MAE=7.1367e-06
    mean | MR=0.1 | seed=2 | MAE=7.9825e-06
    nearest | MR=0.1 | seed=2 | MAE=1.0066e-05
    tikhonov | MR=0.1 | seed=2 | MAE=8.7809e-06
    temporal_laplacian | MR=0.1 | seed=2 | MAE=7.6386e-06

Completed: 2026-04-06T17:04:56.767165
Total rows: 336