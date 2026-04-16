# Integration Log: scr_00104
Started: 2026-04-16T15:05:13.844974+00:00
Description: Screening scr_00104 ds=movielens_graph_signal graph=aew miss=1ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.0037s
    nearest | MR=1ch | seed=0 | MAE=1.9262e-02 | t=0.0032s
    tikhonov | MR=1ch | seed=0 | MAE=2.4688e-02 | t=0.0089s
    tv | MR=1ch | seed=0 | MAE=1.5678e-02 | t=0.4043s
    trss | MR=1ch | seed=0 | MAE=1.7261e-02 | t=0.6998s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=7.6362e-02 | t=0.1332s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.0737e-01 | t=24.9568s
    mean | MR=1ch | seed=1 | MAE=1.2778e-02 | t=0.0034s
    nearest | MR=1ch | seed=1 | MAE=1.7187e-02 | t=0.0033s
    tikhonov | MR=1ch | seed=1 | MAE=2.2367e-02 | t=0.0088s
    tv | MR=1ch | seed=1 | MAE=1.2927e-02 | t=1.0247s
    trss | MR=1ch | seed=1 | MAE=1.5116e-02 | t=0.7593s

Completed: 2026-04-16T15:05:13.845951+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.