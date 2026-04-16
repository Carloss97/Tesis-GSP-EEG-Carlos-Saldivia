# Integration Log: scr_00543
Started: 2026-04-16T14:07:40.701409+00:00
Description: Screening scr_00543 ds=bci_iv2a_real_s1 graph=knn miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.3 | seed=0 | MAE=4.4732e-06 | t=0.0029s
    nearest | MR=0.3 | seed=0 | MAE=4.7753e-06 | t=0.0075s
    tikhonov | MR=0.3 | seed=0 | MAE=6.9436e-06 | t=0.0063s
    tv | MR=0.3 | seed=0 | MAE=4.4728e-06 | t=0.1528s
    trss | MR=0.3 | seed=0 | MAE=3.2594e-06 | t=0.0182s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.0683e-05 | t=0.0156s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.5601e-05 | t=23.6177s
    mean | MR=0.3 | seed=1 | MAE=4.4548e-06 | t=0.0020s
    nearest | MR=0.3 | seed=1 | MAE=4.6851e-06 | t=0.0084s
    tikhonov | MR=0.3 | seed=1 | MAE=6.9196e-06 | t=0.0062s
    tv | MR=0.3 | seed=1 | MAE=4.4545e-06 | t=0.1492s
    trss | MR=0.3 | seed=1 | MAE=3.2717e-06 | t=0.0196s

Completed: 2026-04-16T14:07:40.702345+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.