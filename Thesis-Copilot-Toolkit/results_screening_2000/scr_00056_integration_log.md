# Integration Log: scr_00056
Started: 2026-04-16T14:42:00.040933+00:00
Description: Screening scr_00056 ds=movielens_graph_signal graph=gaussian miss=1ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.0030s
    nearest | MR=1ch | seed=0 | MAE=1.9262e-02 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=7.6824e-02 | t=0.0091s
    tv | MR=1ch | seed=0 | MAE=1.5665e-02 | t=0.8054s
    trss | MR=1ch | seed=0 | MAE=1.7596e-02 | t=1.0076s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.4912e-01 | t=0.0408s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.4040e-01 | t=14.9621s
    mean | MR=1ch | seed=1 | MAE=1.2778e-02 | t=0.0334s
    nearest | MR=1ch | seed=1 | MAE=1.7187e-02 | t=0.0032s
    tikhonov | MR=1ch | seed=1 | MAE=7.6285e-02 | t=0.0100s
    tv | MR=1ch | seed=1 | MAE=1.2784e-02 | t=1.1407s
    trss | MR=1ch | seed=1 | MAE=1.5684e-02 | t=0.3292s

Completed: 2026-04-16T14:42:00.041790+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.