# Integration Log: it83_cross_dataset_generalization_knn
Started: 2026-04-06T17:04:39.800835
Description: Cross-dataset generalization on KNN graph

## Dataset: synthetic_16ch | shape=(300, 16)
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=4.9961e-01
    nearest | MR=0.1 | seed=0 | MAE=6.2613e-01
    tikhonov | MR=0.1 | seed=0 | MAE=5.5846e-01
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.0705e-01
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.6766e-01
    tv | MR=0.1 | seed=0 | MAE=4.6846e-01
    trss | MR=0.1 | seed=0 | MAE=4.4386e-01
    mean | MR=0.1 | seed=1 | MAE=5.1739e-01
    nearest | MR=0.1 | seed=1 | MAE=6.3687e-01
    tikhonov | MR=0.1 | seed=1 | MAE=5.5199e-01
    temporal_laplacian | MR=0.1 | seed=1 | MAE=4.9302e-01
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=4.5685e-01
    tv | MR=0.1 | seed=1 | MAE=4.5091e-01
    trss | MR=0.1 | seed=1 | MAE=4.4402e-01
    mean | MR=0.1 | seed=2 | MAE=5.1185e-01
    nearest | MR=0.1 | seed=2 | MAE=6.3019e-01
    tikhonov | MR=0.1 | seed=2 | MAE=5.7582e-01
    temporal_laplacian | MR=0.1 | seed=2 | MAE=4.7884e-01

## Dataset: mne_sample_proxy | shape=(300, 60)
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.9200e-06
    nearest | MR=0.1 | seed=0 | MAE=2.3880e-06
    tikhonov | MR=0.1 | seed=0 | MAE=2.1149e-06
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.8243e-06
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.6942e-06
    tv | MR=0.1 | seed=0 | MAE=1.7626e-06
    trss | MR=0.1 | seed=0 | MAE=1.7150e-06
    mean | MR=0.1 | seed=1 | MAE=1.9145e-06
    nearest | MR=0.1 | seed=1 | MAE=2.3449e-06
    tikhonov | MR=0.1 | seed=1 | MAE=2.0822e-06
    temporal_laplacian | MR=0.1 | seed=1 | MAE=1.8338e-06
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=1.6836e-06
    tv | MR=0.1 | seed=1 | MAE=1.7023e-06
    trss | MR=0.1 | seed=1 | MAE=1.7049e-06
    mean | MR=0.1 | seed=2 | MAE=1.9273e-06
    nearest | MR=0.1 | seed=2 | MAE=2.3555e-06
    tikhonov | MR=0.1 | seed=2 | MAE=2.0879e-06
    temporal_laplacian | MR=0.1 | seed=2 | MAE=1.7670e-06

## Dataset: bci_competition_proxy | shape=(300, 22)
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=7.6405e-06
    nearest | MR=0.1 | seed=0 | MAE=9.3523e-06
    tikhonov | MR=0.1 | seed=0 | MAE=8.0791e-06
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.1485e-06
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.8383e-06
    tv | MR=0.1 | seed=0 | MAE=6.6941e-06
    trss | MR=0.1 | seed=0 | MAE=6.8005e-06
    mean | MR=0.1 | seed=1 | MAE=7.5033e-06
    nearest | MR=0.1 | seed=1 | MAE=9.6106e-06
    tikhonov | MR=0.1 | seed=1 | MAE=8.2878e-06
    temporal_laplacian | MR=0.1 | seed=1 | MAE=7.2919e-06
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=6.7215e-06
    tv | MR=0.1 | seed=1 | MAE=6.8591e-06
    trss | MR=0.1 | seed=1 | MAE=6.8111e-06
    mean | MR=0.1 | seed=2 | MAE=7.5273e-06
    nearest | MR=0.1 | seed=2 | MAE=9.3245e-06
    tikhonov | MR=0.1 | seed=2 | MAE=8.4045e-06
    temporal_laplacian | MR=0.1 | seed=2 | MAE=7.6271e-06

Completed: 2026-04-06T17:04:41.582615
Total rows: 189