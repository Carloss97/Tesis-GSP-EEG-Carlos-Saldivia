# Integration Log: it150_142
Started: 2026-04-15T00:57:33.970082+00:00
Description: Bulk normalized run it150_142 dataset=synthetic_beta graph=gaussian miss=[0.2] mode=base

## Dataset: synthetic_beta | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2957e-01 | t=0.0032s
    nearest | MR=0.2 | seed=0 | MAE=1.6337e-01 | t=0.0040s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6935e-01 | t=0.0098s
    tv | MR=0.2 | seed=0 | MAE=1.3100e-01 | t=0.2026s
    trss | MR=0.2 | seed=0 | MAE=1.0100e-01 | t=0.0164s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5184e-01 | t=0.0099s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.6799e-01 | t=1.0878s
    mean | MR=0.2 | seed=1 | MAE=1.2838e-01 | t=0.0030s
    nearest | MR=0.2 | seed=1 | MAE=1.7359e-01 | t=0.0045s
    tikhonov | MR=0.2 | seed=1 | MAE=2.6984e-01 | t=0.0070s
    tv | MR=0.2 | seed=1 | MAE=1.3045e-01 | t=0.1878s
    trss | MR=0.2 | seed=1 | MAE=1.0373e-01 | t=0.0165s

Completed: 2026-04-15T00:57:33.971239+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.