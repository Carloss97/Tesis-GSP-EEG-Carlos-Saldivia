# Integration Log: it119_noise_trend_multidomain
Started: 2026-04-07T06:15:47.616415+00:00
Description: Noise trend multidomain

## Dataset: iris_graph_signal | rows=112
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.3128e-01 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=1.6856e-01 | t=0.0018s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6737e-01 | t=0.0049s
    tv | MR=0.2 | seed=0 | MAE=1.3087e-01 | t=0.1020s
    trss | MR=0.2 | seed=0 | MAE=1.0745e-01 | t=0.0072s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2317e-01 | t=0.0074s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.3800e-01 | t=0.0124s
    mean | MR=0.2 | seed=1 | MAE=1.3992e-01 | t=0.0027s
    nearest | MR=0.2 | seed=1 | MAE=1.5380e-01 | t=0.0018s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7209e-01 | t=0.0050s
    tv | MR=0.2 | seed=1 | MAE=1.3910e-01 | t=0.1019s
    trss | MR=0.2 | seed=1 | MAE=1.1388e-01 | t=0.0072s

## Dataset: iv100hz_mat | rows=112
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.2161e+01 | t=0.0037s
    nearest | MR=0.2 | seed=0 | MAE=6.5284e+01 | t=0.0077s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0115e+02 | t=0.0126s
    tv | MR=0.2 | seed=0 | MAE=4.3129e+01 | t=0.2893s
    trss | MR=0.2 | seed=0 | MAE=3.4461e+01 | t=0.0353s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6809e+02 | t=0.0160s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0378e+02 | t=7.2862s
    mean | MR=0.2 | seed=1 | MAE=4.1947e+01 | t=0.0036s
    nearest | MR=0.2 | seed=1 | MAE=6.5604e+01 | t=0.0077s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0156e+02 | t=0.0125s
    tv | MR=0.2 | seed=1 | MAE=4.1885e+01 | t=0.2836s
    trss | MR=0.2 | seed=1 | MAE=3.4520e+01 | t=0.0343s

## Dataset: physionet_eegmmidb_real | rows=112
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1646e-06 | t=0.0038s
    nearest | MR=0.2 | seed=0 | MAE=4.8008e-06 | t=0.0077s
    tikhonov | MR=0.2 | seed=0 | MAE=5.8552e-06 | t=0.0130s
    tv | MR=0.2 | seed=0 | MAE=4.0713e-06 | t=0.3712s
    trss | MR=0.2 | seed=0 | MAE=2.1621e-06 | t=0.0343s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1144e-05 | t=0.0163s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9022e-05 | t=7.6823s
    mean | MR=0.2 | seed=1 | MAE=4.1469e-06 | t=0.0037s
    nearest | MR=0.2 | seed=1 | MAE=4.7521e-06 | t=0.0077s
    tikhonov | MR=0.2 | seed=1 | MAE=5.8432e-06 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=4.0510e-06 | t=0.2857s
    trss | MR=0.2 | seed=1 | MAE=2.1607e-06 | t=0.0333s

Completed: 2026-04-07T06:15:47.622283+00:00
Total rows: 336
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.