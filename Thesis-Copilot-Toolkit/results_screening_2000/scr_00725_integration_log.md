# Integration Log: scr_00725
Started: 2026-04-16T11:50:58.689496+00:00
Description: Screening scr_00725 ds=bci_iv2a_real_s3 graph=knng miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knng built OK
    mean | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.0021s
    nearest | MR=0.4 | seed=0 | MAE=1.3679e-06 | t=0.0087s
    tikhonov | MR=0.4 | seed=0 | MAE=2.1862e-06 | t=0.0058s
    tv | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.1508s
    trss | MR=0.4 | seed=0 | MAE=1.3626e-06 | t=0.0197s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.9356e-06 | t=0.0084s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=5.9279e-06 | t=1.2911s
    mean | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.0021s
    nearest | MR=0.4 | seed=1 | MAE=1.3378e-06 | t=0.0086s
    tikhonov | MR=0.4 | seed=1 | MAE=2.1933e-06 | t=0.0058s
    tv | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.1507s
    trss | MR=0.4 | seed=1 | MAE=1.3654e-06 | t=0.0202s

Completed: 2026-04-16T11:50:58.690350+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.