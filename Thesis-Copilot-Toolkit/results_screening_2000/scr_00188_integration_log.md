# Integration Log: scr_00188
Started: 2026-04-16T14:22:57.116741+00:00
Description: Screening scr_00188 ds=movielens_graph_signal graph=knng miss=2ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.0031s
    nearest | MR=2ch | seed=0 | MAE=1.3191e-02 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=6.3960e-02 | t=0.0091s
    tv | MR=2ch | seed=0 | MAE=1.4572e-02 | t=0.7004s
    trss | MR=2ch | seed=0 | MAE=1.8736e-02 | t=0.4873s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.4176e-01 | t=0.0125s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.4232e-01 | t=18.7471s
    mean | MR=2ch | seed=1 | MAE=1.9048e-02 | t=0.0021s
    nearest | MR=2ch | seed=1 | MAE=2.1272e-02 | t=0.0052s
    tikhonov | MR=2ch | seed=1 | MAE=6.8756e-02 | t=0.0069s
    tv | MR=2ch | seed=1 | MAE=1.9106e-02 | t=0.1787s
    trss | MR=2ch | seed=1 | MAE=2.7825e-02 | t=0.2743s

Completed: 2026-04-16T14:22:57.117623+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.