# Integration Log: scr_00280
Started: 2026-04-16T15:08:45.270351+00:00
Description: Screening scr_00280 ds=bci_iv2a_real_s2 graph=kalofolias miss=3ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: kalofolias built OK
    mean | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.0031s
    nearest | MR=3ch | seed=0 | MAE=5.1829e-07 | t=0.0576s
    tikhonov | MR=3ch | seed=0 | MAE=1.9762e-06 | t=0.0086s
    tv | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.6710s
    trss | MR=3ch | seed=0 | MAE=3.8275e-07 | t=0.0182s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=4.9577e-06 | t=0.0087s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.4886e-05 | t=18.2930s
    mean | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.0032s
    nearest | MR=3ch | seed=1 | MAE=4.9473e-07 | t=0.1046s
    tikhonov | MR=3ch | seed=1 | MAE=1.9751e-06 | t=0.0087s
    tv | MR=3ch | seed=1 | MAE=5.2909e-07 | t=1.2856s
    trss | MR=3ch | seed=1 | MAE=3.8330e-07 | t=0.0634s

Completed: 2026-04-16T15:08:45.271631+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.