# Integration Log: scr_00615
Started: 2026-04-16T14:42:27.179272+00:00
Description: Screening scr_00615 ds=bci_iv2a_real_s1 graph=knng miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knng built OK
    mean | MR=0.3 | seed=0 | MAE=4.4732e-06 | t=0.0041s
    nearest | MR=0.3 | seed=0 | MAE=4.7753e-06 | t=0.0589s
    tikhonov | MR=0.3 | seed=0 | MAE=7.6308e-06 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=4.4730e-06 | t=0.5648s
    trss | MR=0.3 | seed=0 | MAE=3.3929e-06 | t=0.2154s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.1374e-05 | t=0.0127s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.6495e-05 | t=22.9341s
    mean | MR=0.3 | seed=1 | MAE=4.4548e-06 | t=0.0036s
    nearest | MR=0.3 | seed=1 | MAE=4.6851e-06 | t=0.0416s
    tikhonov | MR=0.3 | seed=1 | MAE=7.6086e-06 | t=0.0128s
    tv | MR=0.3 | seed=1 | MAE=4.4546e-06 | t=0.5520s
    trss | MR=0.3 | seed=1 | MAE=3.3806e-06 | t=0.2454s

Completed: 2026-04-16T14:42:27.180154+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.