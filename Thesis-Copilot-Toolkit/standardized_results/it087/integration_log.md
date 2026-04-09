# Integration Log: it87_cross_dataset_generalization_few_missing
Started: 2026-04-06T17:04:46.646838
Description: Cross-dataset generalization with 1ch/2ch/3ch scenarios

## Dataset: synthetic_16ch | shape=(300, 16)
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=5.2541e-01
    nearest | MR=1ch | seed=0 | MAE=6.5616e-01
    tikhonov | MR=1ch | seed=0 | MAE=5.5051e-01
    temporal_laplacian | MR=1ch | seed=0 | MAE=5.1826e-01
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=4.7660e-01
    tv | MR=1ch | seed=0 | MAE=4.8596e-01
    trss | MR=1ch | seed=0 | MAE=4.7018e-01
    mean | MR=1ch | seed=1 | MAE=5.2617e-01
    nearest | MR=1ch | seed=1 | MAE=6.3743e-01
    tikhonov | MR=1ch | seed=1 | MAE=5.6072e-01
    temporal_laplacian | MR=1ch | seed=1 | MAE=5.1347e-01
    graph_time_tikhonov | MR=1ch | seed=1 | MAE=4.8561e-01
    tv | MR=1ch | seed=1 | MAE=4.8064e-01
    trss | MR=1ch | seed=1 | MAE=4.8206e-01
    mean | MR=1ch | seed=2 | MAE=5.3361e-01
    nearest | MR=1ch | seed=2 | MAE=6.5718e-01
    tikhonov | MR=1ch | seed=2 | MAE=5.9281e-01
    temporal_laplacian | MR=1ch | seed=2 | MAE=5.0010e-01

## Dataset: mne_sample_proxy | shape=(300, 60)
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=1.9344e-06
    nearest | MR=1ch | seed=0 | MAE=2.4242e-06
    tikhonov | MR=1ch | seed=0 | MAE=2.0790e-06
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.9638e-06
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.8214e-06
    tv | MR=1ch | seed=0 | MAE=1.8352e-06
    trss | MR=1ch | seed=0 | MAE=1.8167e-06
    mean | MR=1ch | seed=1 | MAE=1.9411e-06
    nearest | MR=1ch | seed=1 | MAE=2.4032e-06
    tikhonov | MR=1ch | seed=1 | MAE=2.1119e-06
    temporal_laplacian | MR=1ch | seed=1 | MAE=1.9528e-06
    graph_time_tikhonov | MR=1ch | seed=1 | MAE=1.7601e-06
    tv | MR=1ch | seed=1 | MAE=1.7269e-06
    trss | MR=1ch | seed=1 | MAE=1.8017e-06
    mean | MR=1ch | seed=2 | MAE=1.9661e-06
    nearest | MR=1ch | seed=2 | MAE=2.4056e-06
    tikhonov | MR=1ch | seed=2 | MAE=2.1422e-06
    temporal_laplacian | MR=1ch | seed=2 | MAE=1.9549e-06

## Dataset: bci_competition_proxy | shape=(300, 22)
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=7.7695e-06
    nearest | MR=1ch | seed=0 | MAE=9.7595e-06
    tikhonov | MR=1ch | seed=0 | MAE=8.4299e-06
    temporal_laplacian | MR=1ch | seed=0 | MAE=7.7791e-06
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=7.2507e-06
    tv | MR=1ch | seed=0 | MAE=7.2747e-06
    trss | MR=1ch | seed=0 | MAE=7.0411e-06
    mean | MR=1ch | seed=1 | MAE=7.7991e-06
    nearest | MR=1ch | seed=1 | MAE=9.6059e-06
    tikhonov | MR=1ch | seed=1 | MAE=8.5188e-06
    temporal_laplacian | MR=1ch | seed=1 | MAE=8.0224e-06
    graph_time_tikhonov | MR=1ch | seed=1 | MAE=7.2385e-06
    tv | MR=1ch | seed=1 | MAE=7.2283e-06
    trss | MR=1ch | seed=1 | MAE=7.2008e-06
    mean | MR=1ch | seed=2 | MAE=7.9578e-06
    nearest | MR=1ch | seed=2 | MAE=9.5177e-06
    tikhonov | MR=1ch | seed=2 | MAE=8.5079e-06
    temporal_laplacian | MR=1ch | seed=2 | MAE=7.6598e-06

Completed: 2026-04-06T17:04:48.261821
Total rows: 189