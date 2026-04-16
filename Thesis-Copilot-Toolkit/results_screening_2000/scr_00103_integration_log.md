# Integration Log: scr_00103
Started: 2026-04-16T15:04:27.261061+00:00
Description: Screening scr_00103 ds=iris_graph_signal graph=aew miss=1ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=1ch | seed=0 | MAE=1.2881e-01 | t=0.0015s
    nearest | MR=1ch | seed=0 | MAE=1.6484e-01 | t=0.0015s
    tikhonov | MR=1ch | seed=0 | MAE=1.3169e-01 | t=0.0965s
    tv | MR=1ch | seed=0 | MAE=1.0497e-01 | t=0.1838s
    trss | MR=1ch | seed=0 | MAE=8.0596e-02 | t=0.0037s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.2150e-01 | t=0.0051s
    temporal_laplacian | MR=1ch | seed=0 | MAE=4.6663e-01 | t=15.4806s
    mean | MR=1ch | seed=1 | MAE=1.3930e-01 | t=0.0311s
    nearest | MR=1ch | seed=1 | MAE=1.5346e-01 | t=0.0030s
    tikhonov | MR=1ch | seed=1 | MAE=1.4471e-01 | t=0.0036s
    tv | MR=1ch | seed=1 | MAE=1.2292e-01 | t=0.1693s
    trss | MR=1ch | seed=1 | MAE=9.4878e-02 | t=0.0142s

Completed: 2026-04-16T15:04:27.261888+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.