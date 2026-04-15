# Integration Log: it150_145
Started: 2026-04-15T00:57:54.209965+00:00
Description: Bulk normalized run it150_145 dataset=mne_sample graph=kalofolias miss=[0.2] mode=base

## Dataset: mne_sample | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=1.5569e-01 | t=0.0032s
    nearest | MR=0.2 | seed=0 | MAE=2.0800e-01 | t=0.0048s
    tikhonov | MR=0.2 | seed=0 | MAE=4.6360e-01 | t=0.0084s
    tv | MR=0.2 | seed=0 | MAE=1.5569e-01 | t=0.2350s
    trss | MR=0.2 | seed=0 | MAE=1.0633e-01 | t=0.0211s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.3423e-01 | t=0.0121s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.6079e-01 | t=1.7979s
    mean | MR=0.2 | seed=1 | MAE=1.5761e-01 | t=0.0029s
    nearest | MR=0.2 | seed=1 | MAE=2.1365e-01 | t=0.0061s
    tikhonov | MR=0.2 | seed=1 | MAE=4.6455e-01 | t=0.0074s
    tv | MR=0.2 | seed=1 | MAE=1.5761e-01 | t=0.2336s
    trss | MR=0.2 | seed=1 | MAE=1.0851e-01 | t=0.0204s

Completed: 2026-04-15T00:57:54.211184+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.