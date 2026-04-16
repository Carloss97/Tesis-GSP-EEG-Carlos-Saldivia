# Integration Log: scr_00603
Started: 2026-04-16T14:36:33.376306+00:00
Description: Screening scr_00603 ds=bci_iv2a_real_s1 graph=kalofolias miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.3 | seed=0 | MAE=4.4732e-06 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=4.7753e-06 | t=0.0335s
    tikhonov | MR=0.3 | seed=0 | MAE=8.6330e-06 | t=0.0116s
    tv | MR=0.3 | seed=0 | MAE=4.4732e-06 | t=0.3653s
    trss | MR=0.3 | seed=0 | MAE=3.3338e-06 | t=0.0767s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.2283e-05 | t=0.0172s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.7494e-05 | t=23.1408s
    mean | MR=0.3 | seed=1 | MAE=4.4548e-06 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=4.6851e-06 | t=0.0134s
    tikhonov | MR=0.3 | seed=1 | MAE=8.5770e-06 | t=0.0085s
    tv | MR=0.3 | seed=1 | MAE=4.4548e-06 | t=0.2091s
    trss | MR=0.3 | seed=1 | MAE=3.3023e-06 | t=0.0203s

Completed: 2026-04-16T14:36:33.377196+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.