# Integration Log: it94_robustness_cross_proxy_shift
Started: 2026-04-06T17:04:58.506735
Description: Cross-proxy domain shift robustness

## Dataset: mne_sample_proxy | shape=(300, 60)
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.9801e-06
    nearest | MR=0.2 | seed=0 | MAE=2.5077e-06
    tikhonov | MR=0.2 | seed=0 | MAE=2.2247e-06
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0618e-06
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9494e-06
    tv | MR=0.2 | seed=0 | MAE=1.9593e-06
    trss | MR=0.2 | seed=0 | MAE=1.9261e-06
    mean | MR=0.2 | seed=1 | MAE=1.9386e-06
    nearest | MR=0.2 | seed=1 | MAE=2.5523e-06
    tikhonov | MR=0.2 | seed=1 | MAE=2.2340e-06
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.1101e-06
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.9802e-06
    tv | MR=0.2 | seed=1 | MAE=1.9267e-06
    trss | MR=0.2 | seed=1 | MAE=1.9414e-06
    mean | MR=0.2 | seed=2 | MAE=2.0193e-06
    nearest | MR=0.2 | seed=2 | MAE=2.4675e-06
    tikhonov | MR=0.2 | seed=2 | MAE=2.1170e-06
    temporal_laplacian | MR=0.2 | seed=2 | MAE=2.0572e-06
  Graph: gaussian built OK
    mean | MR=0.2 | seed=0 | MAE=2.0294e-06
    nearest | MR=0.2 | seed=0 | MAE=2.6712e-06
    tikhonov | MR=0.2 | seed=0 | MAE=2.3330e-06
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.1912e-06
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0405e-06
    tv | MR=0.2 | seed=0 | MAE=2.0422e-06
    trss | MR=0.2 | seed=0 | MAE=2.0976e-06
    mean | MR=0.2 | seed=1 | MAE=2.1758e-06
    nearest | MR=0.2 | seed=1 | MAE=2.6491e-06
    tikhonov | MR=0.2 | seed=1 | MAE=2.3284e-06
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.2638e-06
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.0772e-06
    tv | MR=0.2 | seed=1 | MAE=2.0286e-06
    trss | MR=0.2 | seed=1 | MAE=2.0509e-06
    mean | MR=0.2 | seed=2 | MAE=2.0754e-06
    nearest | MR=0.2 | seed=2 | MAE=2.6001e-06
    tikhonov | MR=0.2 | seed=2 | MAE=2.3038e-06
    temporal_laplacian | MR=0.2 | seed=2 | MAE=2.1500e-06

## Dataset: bci_competition_proxy | shape=(300, 22)
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.9140e-06
    nearest | MR=0.2 | seed=0 | MAE=9.8535e-06
    tikhonov | MR=0.2 | seed=0 | MAE=9.0143e-06
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.1982e-06
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.7193e-06
    tv | MR=0.2 | seed=0 | MAE=7.8929e-06
    trss | MR=0.2 | seed=0 | MAE=7.6974e-06
    mean | MR=0.2 | seed=1 | MAE=8.2961e-06
    nearest | MR=0.2 | seed=1 | MAE=9.9259e-06
    tikhonov | MR=0.2 | seed=1 | MAE=8.7466e-06
    temporal_laplacian | MR=0.2 | seed=1 | MAE=8.3609e-06
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=8.0251e-06
    tv | MR=0.2 | seed=1 | MAE=7.8167e-06
    trss | MR=0.2 | seed=1 | MAE=7.5450e-06
    mean | MR=0.2 | seed=2 | MAE=7.8210e-06
    nearest | MR=0.2 | seed=2 | MAE=9.9919e-06
    tikhonov | MR=0.2 | seed=2 | MAE=9.0560e-06
    temporal_laplacian | MR=0.2 | seed=2 | MAE=8.2507e-06
  Graph: gaussian built OK
    mean | MR=0.2 | seed=0 | MAE=8.2828e-06
    nearest | MR=0.2 | seed=0 | MAE=1.0547e-05
    tikhonov | MR=0.2 | seed=0 | MAE=9.1883e-06
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.7094e-06
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.3122e-06
    tv | MR=0.2 | seed=0 | MAE=8.1483e-06
    trss | MR=0.2 | seed=0 | MAE=8.0667e-06
    mean | MR=0.2 | seed=1 | MAE=8.2181e-06
    nearest | MR=0.2 | seed=1 | MAE=1.0489e-05
    tikhonov | MR=0.2 | seed=1 | MAE=9.1192e-06
    temporal_laplacian | MR=0.2 | seed=1 | MAE=8.7113e-06
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=8.4695e-06
    tv | MR=0.2 | seed=1 | MAE=8.0738e-06
    trss | MR=0.2 | seed=1 | MAE=8.1540e-06
    mean | MR=0.2 | seed=2 | MAE=8.3532e-06
    nearest | MR=0.2 | seed=2 | MAE=1.0306e-05
    tikhonov | MR=0.2 | seed=2 | MAE=9.4684e-06
    temporal_laplacian | MR=0.2 | seed=2 | MAE=8.8173e-06

## Dataset: physionet_eegmmidb | shape=(300, 64)
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=2.6757e-05
    nearest | MR=0.2 | seed=0 | MAE=3.3116e-05
    tikhonov | MR=0.2 | seed=0 | MAE=2.8462e-05
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7823e-05
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.5819e-05
    tv | MR=0.2 | seed=0 | MAE=2.6105e-05
    trss | MR=0.2 | seed=0 | MAE=2.6363e-05
    mean | MR=0.2 | seed=1 | MAE=2.7453e-05
    nearest | MR=0.2 | seed=1 | MAE=3.3144e-05
    tikhonov | MR=0.2 | seed=1 | MAE=2.9451e-05
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7339e-05
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.6458e-05
    tv | MR=0.2 | seed=1 | MAE=2.6117e-05
    trss | MR=0.2 | seed=1 | MAE=2.5670e-05
    mean | MR=0.2 | seed=2 | MAE=2.6864e-05
    nearest | MR=0.2 | seed=2 | MAE=3.3650e-05
    tikhonov | MR=0.2 | seed=2 | MAE=2.9664e-05
    temporal_laplacian | MR=0.2 | seed=2 | MAE=2.7416e-05
  Graph: gaussian built OK
    mean | MR=0.2 | seed=0 | MAE=2.7697e-05
    nearest | MR=0.2 | seed=0 | MAE=3.5486e-05
    tikhonov | MR=0.2 | seed=0 | MAE=3.0305e-05
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8876e-05
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8493e-05
    tv | MR=0.2 | seed=0 | MAE=2.6903e-05
    trss | MR=0.2 | seed=0 | MAE=2.7386e-05
    mean | MR=0.2 | seed=1 | MAE=2.8749e-05
    nearest | MR=0.2 | seed=1 | MAE=3.4429e-05
    tikhonov | MR=0.2 | seed=1 | MAE=3.1932e-05
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.9441e-05
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.7806e-05
    tv | MR=0.2 | seed=1 | MAE=2.7039e-05
    trss | MR=0.2 | seed=1 | MAE=2.6663e-05
    mean | MR=0.2 | seed=2 | MAE=2.8313e-05
    nearest | MR=0.2 | seed=2 | MAE=3.5341e-05
    tikhonov | MR=0.2 | seed=2 | MAE=3.1175e-05
    temporal_laplacian | MR=0.2 | seed=2 | MAE=2.9453e-05

Completed: 2026-04-06T17:05:00.208681
Total rows: 336