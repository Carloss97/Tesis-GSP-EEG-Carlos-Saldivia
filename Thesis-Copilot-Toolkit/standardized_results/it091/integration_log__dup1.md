# Integration Log: it91_robustness_method_subset_tv_focus
Started: 2026-04-06T17:04:53.402893
Description: Sensitivity with strong TV/time subset emphasis

## Dataset: synthetic_16ch | shape=(300, 16)
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=4.9429e-01
    tikhonov | MR=0.1 | seed=0 | MAE=5.6146e-01
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.5337e-01
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.2453e-01
    tv | MR=0.1 | seed=0 | MAE=4.4048e-01
    trss | MR=0.1 | seed=0 | MAE=4.2858e-01
    mean | MR=0.1 | seed=1 | MAE=4.9641e-01
    tikhonov | MR=0.1 | seed=1 | MAE=5.5206e-01
    temporal_laplacian | MR=0.1 | seed=1 | MAE=4.6814e-01
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=4.2573e-01
    tv | MR=0.1 | seed=1 | MAE=4.3031e-01
    trss | MR=0.1 | seed=1 | MAE=4.1871e-01
    mean | MR=0.1 | seed=2 | MAE=5.0295e-01
    tikhonov | MR=0.1 | seed=2 | MAE=5.5130e-01
    temporal_laplacian | MR=0.1 | seed=2 | MAE=4.6068e-01
    graph_time_tikhonov | MR=0.1 | seed=2 | MAE=4.4846e-01
    tv | MR=0.1 | seed=2 | MAE=4.4219e-01
    trss | MR=0.1 | seed=2 | MAE=4.2432e-01

## Dataset: mne_sample_proxy | shape=(300, 60)
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.9050e-06
    tikhonov | MR=0.1 | seed=0 | MAE=2.0546e-06
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.7363e-06
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.6462e-06
    tv | MR=0.1 | seed=0 | MAE=1.6609e-06
    trss | MR=0.1 | seed=0 | MAE=1.5735e-06
    mean | MR=0.1 | seed=1 | MAE=1.9292e-06
    tikhonov | MR=0.1 | seed=1 | MAE=2.0527e-06
    temporal_laplacian | MR=0.1 | seed=1 | MAE=1.7590e-06
    graph_time_tikhonov | MR=0.1 | seed=1 | MAE=1.5922e-06
    tv | MR=0.1 | seed=1 | MAE=1.5384e-06
    trss | MR=0.1 | seed=1 | MAE=1.6257e-06
    mean | MR=0.1 | seed=2 | MAE=1.9755e-06
    tikhonov | MR=0.1 | seed=2 | MAE=2.1502e-06
    temporal_laplacian | MR=0.1 | seed=2 | MAE=1.7756e-06
    graph_time_tikhonov | MR=0.1 | seed=2 | MAE=1.6291e-06
    tv | MR=0.1 | seed=2 | MAE=1.5896e-06
    trss | MR=0.1 | seed=2 | MAE=1.6691e-06

Completed: 2026-04-06T17:04:55.119521
Total rows: 180