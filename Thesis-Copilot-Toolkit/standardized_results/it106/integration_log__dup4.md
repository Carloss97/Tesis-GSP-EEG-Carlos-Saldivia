# Integration Log: it106_bci_iv2a_multisubject
Started: 2026-04-06T18:55:25.724639+00:00
Description: BCI IV 2a multisubject validation (S1-S3)

## Dataset: bci_iv2a_real_s1 | rows=126
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0038s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0052s
    tikhonov | MR=0.1 | seed=0 | MAE=4.5749e-06 | t=0.0128s
    tv | MR=0.1 | seed=0 | MAE=1.3024e-06 | t=0.3069s
    trss | MR=0.1 | seed=0 | MAE=9.1525e-07 | t=0.0348s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=9.3331e-06 | t=0.0161s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4248e-05 | t=7.2625s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0037s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0051s
    tikhonov | MR=0.1 | seed=1 | MAE=4.5276e-06 | t=0.0133s
    tv | MR=0.1 | seed=1 | MAE=1.2371e-06 | t=0.3053s
    trss | MR=0.1 | seed=1 | MAE=8.4390e-07 | t=0.0321s

## Dataset: bci_iv2a_real_s2 | rows=126
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.0038s
    nearest | MR=0.1 | seed=0 | MAE=3.2237e-07 | t=0.0052s
    tikhonov | MR=0.1 | seed=0 | MAE=1.3859e-06 | t=0.0128s
    tv | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.3035s
    trss | MR=0.1 | seed=0 | MAE=2.7621e-07 | t=0.0357s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.5658e-06 | t=0.0166s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.2481e-05 | t=7.9042s
    mean | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.0037s
    nearest | MR=0.1 | seed=1 | MAE=3.1417e-07 | t=0.0051s
    tikhonov | MR=0.1 | seed=1 | MAE=1.3896e-06 | t=0.0128s
    tv | MR=0.1 | seed=1 | MAE=3.4820e-07 | t=0.3055s
    trss | MR=0.1 | seed=1 | MAE=2.8718e-07 | t=0.0328s

## Dataset: bci_iv2a_real_s3 | rows=126
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.0043s
    nearest | MR=0.1 | seed=0 | MAE=2.4876e-07 | t=0.0051s
    tikhonov | MR=0.1 | seed=0 | MAE=1.2245e-06 | t=0.0128s
    tv | MR=0.1 | seed=0 | MAE=3.0422e-07 | t=0.3099s
    trss | MR=0.1 | seed=0 | MAE=2.7490e-07 | t=0.0363s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.4018e-06 | t=0.0163s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.7930e-06 | t=7.2381s
    mean | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.0036s
    nearest | MR=0.1 | seed=1 | MAE=2.5230e-07 | t=0.0053s
    tikhonov | MR=0.1 | seed=1 | MAE=1.2060e-06 | t=0.0128s
    tv | MR=0.1 | seed=1 | MAE=2.8474e-07 | t=0.3000s
    trss | MR=0.1 | seed=1 | MAE=2.6659e-07 | t=0.0330s

Completed: 2026-04-06T18:55:25.729568+00:00
Total rows: 378
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.