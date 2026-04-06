# Integration Log: it90_robustness_graph_sensitivity
Started: 2026-04-06T17:04:51.746203
Description: Sensitivity to graph topology changes

## Dataset: synthetic_16ch | shape=(300, 16)
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2889e-01
    nearest | MR=0.2 | seed=0 | MAE=6.5817e-01
    tikhonov | MR=0.2 | seed=0 | MAE=5.9124e-01
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.1204e-01
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8755e-01
    tv | MR=0.2 | seed=0 | MAE=4.6656e-01
    trss | MR=0.2 | seed=0 | MAE=4.6169e-01
    mean | MR=0.2 | seed=1 | MAE=5.2933e-01
    nearest | MR=0.2 | seed=1 | MAE=6.6617e-01
    tikhonov | MR=0.2 | seed=1 | MAE=5.9766e-01
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.0705e-01
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.8662e-01
    tv | MR=0.2 | seed=1 | MAE=4.6384e-01
    trss | MR=0.2 | seed=1 | MAE=4.7641e-01
    mean | MR=0.2 | seed=2 | MAE=5.2830e-01
    nearest | MR=0.2 | seed=2 | MAE=6.7465e-01
    tikhonov | MR=0.2 | seed=2 | MAE=6.0864e-01
    temporal_laplacian | MR=0.2 | seed=2 | MAE=5.1827e-01
  Graph: gaussian built OK
    mean | MR=0.2 | seed=0 | MAE=5.6281e-01
    nearest | MR=0.2 | seed=0 | MAE=6.9087e-01
    tikhonov | MR=0.2 | seed=0 | MAE=6.0695e-01
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.3731e-01
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8802e-01
    tv | MR=0.2 | seed=0 | MAE=5.1028e-01
    trss | MR=0.2 | seed=0 | MAE=5.1878e-01
    mean | MR=0.2 | seed=1 | MAE=5.5293e-01
    nearest | MR=0.2 | seed=1 | MAE=6.8517e-01
    tikhonov | MR=0.2 | seed=1 | MAE=6.2416e-01
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.3004e-01
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.7981e-01
    tv | MR=0.2 | seed=1 | MAE=4.8846e-01
    trss | MR=0.2 | seed=1 | MAE=4.8914e-01
    mean | MR=0.2 | seed=2 | MAE=5.5793e-01
    nearest | MR=0.2 | seed=2 | MAE=6.9135e-01
    tikhonov | MR=0.2 | seed=2 | MAE=6.2817e-01
    temporal_laplacian | MR=0.2 | seed=2 | MAE=5.3932e-01
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=5.7553e-01
    nearest | MR=0.2 | seed=0 | MAE=7.2844e-01
    tikhonov | MR=0.2 | seed=0 | MAE=6.4075e-01
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.5814e-01
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.1507e-01
    tv | MR=0.2 | seed=0 | MAE=5.0320e-01
    trss | MR=0.2 | seed=0 | MAE=5.1371e-01
    mean | MR=0.2 | seed=1 | MAE=5.5646e-01
    nearest | MR=0.2 | seed=1 | MAE=7.2570e-01
    tikhonov | MR=0.2 | seed=1 | MAE=6.2833e-01
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.6066e-01
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.1433e-01
    tv | MR=0.2 | seed=1 | MAE=5.0952e-01
    trss | MR=0.2 | seed=1 | MAE=5.1264e-01
    mean | MR=0.2 | seed=2 | MAE=5.7046e-01
    nearest | MR=0.2 | seed=2 | MAE=7.2499e-01
    tikhonov | MR=0.2 | seed=2 | MAE=6.3560e-01
    temporal_laplacian | MR=0.2 | seed=2 | MAE=5.4894e-01

## Dataset: mne_sample_proxy | shape=(300, 60)
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.9540e-06
    nearest | MR=0.2 | seed=0 | MAE=2.4805e-06
    tikhonov | MR=0.2 | seed=0 | MAE=2.2808e-06
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.8899e-06
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8097e-06
    tv | MR=0.2 | seed=0 | MAE=1.7914e-06
    trss | MR=0.2 | seed=0 | MAE=1.7471e-06
    mean | MR=0.2 | seed=1 | MAE=1.9624e-06
    nearest | MR=0.2 | seed=1 | MAE=2.4924e-06
    tikhonov | MR=0.2 | seed=1 | MAE=2.1782e-06
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.8496e-06
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7639e-06
    tv | MR=0.2 | seed=1 | MAE=1.7475e-06
    trss | MR=0.2 | seed=1 | MAE=1.7494e-06
    mean | MR=0.2 | seed=2 | MAE=2.0366e-06
    nearest | MR=0.2 | seed=2 | MAE=2.5584e-06
    tikhonov | MR=0.2 | seed=2 | MAE=2.1794e-06
    temporal_laplacian | MR=0.2 | seed=2 | MAE=1.8988e-06
  Graph: gaussian built OK
    mean | MR=0.2 | seed=0 | MAE=2.0792e-06
    nearest | MR=0.2 | seed=0 | MAE=2.5741e-06
    tikhonov | MR=0.2 | seed=0 | MAE=2.3604e-06
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0538e-06
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8618e-06
    tv | MR=0.2 | seed=0 | MAE=1.7742e-06
    trss | MR=0.2 | seed=0 | MAE=1.9340e-06
    mean | MR=0.2 | seed=1 | MAE=2.1025e-06
    nearest | MR=0.2 | seed=1 | MAE=2.6445e-06
    tikhonov | MR=0.2 | seed=1 | MAE=2.2939e-06
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.0101e-06
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7988e-06
    tv | MR=0.2 | seed=1 | MAE=1.8324e-06
    trss | MR=0.2 | seed=1 | MAE=1.9325e-06
    mean | MR=0.2 | seed=2 | MAE=2.0880e-06
    nearest | MR=0.2 | seed=2 | MAE=2.6929e-06
    tikhonov | MR=0.2 | seed=2 | MAE=2.3486e-06
    temporal_laplacian | MR=0.2 | seed=2 | MAE=1.9953e-06
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=2.1899e-06
    nearest | MR=0.2 | seed=0 | MAE=2.7599e-06
    tikhonov | MR=0.2 | seed=0 | MAE=2.3620e-06
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0926e-06
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0234e-06
    tv | MR=0.2 | seed=0 | MAE=1.8686e-06
    trss | MR=0.2 | seed=0 | MAE=1.8435e-06
    mean | MR=0.2 | seed=1 | MAE=2.1756e-06
    nearest | MR=0.2 | seed=1 | MAE=2.7504e-06
    tikhonov | MR=0.2 | seed=1 | MAE=2.3249e-06
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.0134e-06
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.9157e-06
    tv | MR=0.2 | seed=1 | MAE=1.8956e-06
    trss | MR=0.2 | seed=1 | MAE=1.9096e-06
    mean | MR=0.2 | seed=2 | MAE=2.1237e-06
    nearest | MR=0.2 | seed=2 | MAE=2.6753e-06
    tikhonov | MR=0.2 | seed=2 | MAE=2.3970e-06
    temporal_laplacian | MR=0.2 | seed=2 | MAE=2.0732e-06

## Dataset: bci_competition_proxy | shape=(300, 22)
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8586e-06
    nearest | MR=0.2 | seed=0 | MAE=9.7822e-06
    tikhonov | MR=0.2 | seed=0 | MAE=8.8147e-06
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.5941e-06
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.8304e-06
    tv | MR=0.2 | seed=0 | MAE=6.9013e-06
    trss | MR=0.2 | seed=0 | MAE=7.1001e-06
    mean | MR=0.2 | seed=1 | MAE=7.7928e-06
    nearest | MR=0.2 | seed=1 | MAE=9.6518e-06
    tikhonov | MR=0.2 | seed=1 | MAE=8.8063e-06
    temporal_laplacian | MR=0.2 | seed=1 | MAE=7.4903e-06
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=7.4415e-06
    tv | MR=0.2 | seed=1 | MAE=7.0443e-06
    trss | MR=0.2 | seed=1 | MAE=7.3180e-06
    mean | MR=0.2 | seed=2 | MAE=7.9238e-06
    nearest | MR=0.2 | seed=2 | MAE=9.7220e-06
    tikhonov | MR=0.2 | seed=2 | MAE=8.8082e-06
    temporal_laplacian | MR=0.2 | seed=2 | MAE=7.7522e-06
  Graph: gaussian built OK
    mean | MR=0.2 | seed=0 | MAE=8.5139e-06
    nearest | MR=0.2 | seed=0 | MAE=1.0710e-05
    tikhonov | MR=0.2 | seed=0 | MAE=9.1755e-06
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.0142e-06
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.5337e-06
    tv | MR=0.2 | seed=0 | MAE=7.3710e-06
    trss | MR=0.2 | seed=0 | MAE=7.0781e-06
    mean | MR=0.2 | seed=1 | MAE=8.2563e-06
    nearest | MR=0.2 | seed=1 | MAE=1.0329e-05
    tikhonov | MR=0.2 | seed=1 | MAE=9.1277e-06
    temporal_laplacian | MR=0.2 | seed=1 | MAE=8.1417e-06
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=7.3481e-06
    tv | MR=0.2 | seed=1 | MAE=7.2009e-06
    trss | MR=0.2 | seed=1 | MAE=7.3408e-06
    mean | MR=0.2 | seed=2 | MAE=8.5381e-06
    nearest | MR=0.2 | seed=2 | MAE=1.0524e-05
    tikhonov | MR=0.2 | seed=2 | MAE=9.2162e-06
    temporal_laplacian | MR=0.2 | seed=2 | MAE=8.3426e-06
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=8.8223e-06
    nearest | MR=0.2 | seed=0 | MAE=1.0707e-05
    tikhonov | MR=0.2 | seed=0 | MAE=9.5176e-06
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.2577e-06
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.6702e-06
    tv | MR=0.2 | seed=0 | MAE=7.9282e-06
    trss | MR=0.2 | seed=0 | MAE=7.3664e-06
    mean | MR=0.2 | seed=1 | MAE=8.6817e-06
    nearest | MR=0.2 | seed=1 | MAE=1.0718e-05
    tikhonov | MR=0.2 | seed=1 | MAE=9.6369e-06
    temporal_laplacian | MR=0.2 | seed=1 | MAE=8.4016e-06
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=7.8496e-06
    tv | MR=0.2 | seed=1 | MAE=7.7631e-06
    trss | MR=0.2 | seed=1 | MAE=7.5149e-06
    mean | MR=0.2 | seed=2 | MAE=8.7149e-06
    nearest | MR=0.2 | seed=2 | MAE=1.0756e-05
    tikhonov | MR=0.2 | seed=2 | MAE=9.6185e-06
    temporal_laplacian | MR=0.2 | seed=2 | MAE=8.3996e-06

Completed: 2026-04-06T17:04:53.389036
Total rows: 378