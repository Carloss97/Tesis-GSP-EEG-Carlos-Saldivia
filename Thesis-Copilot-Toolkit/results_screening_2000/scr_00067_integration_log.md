# Integration Log: scr_00067
Started: 2026-04-16T14:46:54.238517+00:00
Description: Screening scr_00067 ds=iris_graph_signal graph=kalofolias miss=1ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=1ch | seed=0 | MAE=1.2881e-01 | t=0.0014s
    nearest | MR=1ch | seed=0 | MAE=1.6484e-01 | t=0.0014s
    tikhonov | MR=1ch | seed=0 | MAE=5.3900e-01 | t=0.0049s
    tv | MR=1ch | seed=0 | MAE=1.2881e-01 | t=0.0883s
    trss | MR=1ch | seed=0 | MAE=9.3339e-02 | t=0.0035s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=5.3343e-01 | t=0.0953s
    temporal_laplacian | MR=1ch | seed=0 | MAE=8.2372e-01 | t=3.6983s
    mean | MR=1ch | seed=1 | MAE=1.3930e-01 | t=0.0018s
    nearest | MR=1ch | seed=1 | MAE=1.5346e-01 | t=0.0010s
    tikhonov | MR=1ch | seed=1 | MAE=5.3246e-01 | t=0.0042s
    tv | MR=1ch | seed=1 | MAE=1.3930e-01 | t=0.0550s
    trss | MR=1ch | seed=1 | MAE=1.0295e-01 | t=0.0027s

Completed: 2026-04-16T14:46:54.239400+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.