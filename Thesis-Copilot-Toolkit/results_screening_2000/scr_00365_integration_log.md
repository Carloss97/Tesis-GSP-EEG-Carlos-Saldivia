# Integration Log: scr_00365
Started: 2026-04-16T13:09:18.634092+00:00
Description: Screening scr_00365 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=2.4876e-07 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=2.4703e-06 | t=0.0058s
    tv | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.2355s
    trss | MR=0.1 | seed=0 | MAE=2.1652e-07 | t=0.0721s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.2163e-06 | t=0.0141s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.4614e-06 | t=4.6834s
    mean | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=2.5230e-07 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=2.4663e-06 | t=0.0057s
    tv | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.2387s
    trss | MR=0.1 | seed=1 | MAE=2.0313e-07 | t=0.0954s

Completed: 2026-04-16T13:09:18.634898+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.