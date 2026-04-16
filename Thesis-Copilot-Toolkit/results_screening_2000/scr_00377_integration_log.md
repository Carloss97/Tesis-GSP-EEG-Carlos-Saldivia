# Integration Log: scr_00377
Started: 2026-04-16T13:11:09.854930+00:00
Description: Screening scr_00377 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=2.4876e-07 | t=0.0034s
    tikhonov | MR=0.1 | seed=0 | MAE=2.4703e-06 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.1866s
    trss | MR=0.1 | seed=0 | MAE=2.1652e-07 | t=0.0173s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.2163e-06 | t=0.0084s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.4614e-06 | t=6.0624s
    mean | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=2.5230e-07 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=2.4663e-06 | t=0.0064s
    tv | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.1936s
    trss | MR=0.1 | seed=1 | MAE=2.0313e-07 | t=0.0163s

Completed: 2026-04-16T13:11:09.855797+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.