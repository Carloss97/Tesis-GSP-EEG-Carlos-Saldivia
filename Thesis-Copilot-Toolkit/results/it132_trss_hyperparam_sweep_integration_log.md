# Integration Log: it132_trss_hyperparam_sweep
Started: 2026-04-13T17:56:58.759603+00:00
Description: TRSS hyperparameter sweep (lambda/alpha) on real data

## Dataset: bci_iv2a_real_s1 | rows=64
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=2.4458e-06 | t=0.1495s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5798e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=5.9418e-07 | t=0.0184s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.8236e-06 | t=1.3866s
    tv | MR=0.2 | seed=1 | MAE=2.4905e-06 | t=0.1506s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.6074e-06 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=6.4783e-07 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=8.8755e-06 | t=1.3508s
    tv | MR=0.2 | seed=2 | MAE=2.3799e-06 | t=0.1497s
    graph_time_tikhonov | MR=0.2 | seed=2 | MAE=4.5280e-06 | t=0.0081s
    trss | MR=0.2 | seed=2 | MAE=5.8681e-07 | t=0.0181s
    temporal_laplacian | MR=0.2 | seed=2 | MAE=8.7696e-06 | t=1.3854s

## Dataset: iv100hz_mat | rows=64
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.8283e+01 | t=0.1440s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.0492e+01 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=9.7384e+00 | t=0.0163s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5415e+02 | t=1.3455s
    tv | MR=0.2 | seed=1 | MAE=4.1835e+01 | t=0.1453s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=8.1022e+01 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=9.8279e+00 | t=0.0178s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5412e+02 | t=1.3875s
    tv | MR=0.2 | seed=2 | MAE=4.4676e+01 | t=0.1462s
    graph_time_tikhonov | MR=0.2 | seed=2 | MAE=8.1769e+01 | t=0.0077s
    trss | MR=0.2 | seed=2 | MAE=9.8081e+00 | t=0.0174s
    temporal_laplacian | MR=0.2 | seed=2 | MAE=1.5400e+02 | t=1.3739s

## Dataset: physionet_eegmmidb_real | rows=64
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.7968e-06 | t=0.1527s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.2051e-06 | t=0.0092s
    trss | MR=0.2 | seed=0 | MAE=1.4599e-06 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4402e-05 | t=1.4777s
    tv | MR=0.2 | seed=1 | MAE=3.7331e-06 | t=0.1570s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.1876e-06 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=1.4159e-06 | t=0.0176s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.4426e-05 | t=1.5825s
    tv | MR=0.2 | seed=2 | MAE=3.7350e-06 | t=0.1517s
    graph_time_tikhonov | MR=0.2 | seed=2 | MAE=5.1674e-06 | t=0.0084s
    trss | MR=0.2 | seed=2 | MAE=1.3160e-06 | t=0.0171s
    temporal_laplacian | MR=0.2 | seed=2 | MAE=1.4375e-05 | t=1.5705s

Completed: 2026-04-13T17:56:58.765317+00:00
Total rows: 192
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.