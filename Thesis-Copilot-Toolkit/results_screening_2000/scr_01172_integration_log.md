# Integration Log: scr_01172
Started: 2026-04-16T15:02:39.356508+00:00
Description: Screening scr_01172 ds=movielens_graph_signal graph=vknng miss=[0.1] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=4.3493e-02 | t=0.5119s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.9555e-02 | t=0.0345s
    trss | MR=0.2 | seed=0 | MAE=7.7917e-02 | t=0.2390s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1777e-01 | t=19.7335s
    tv | MR=0.2 | seed=1 | MAE=4.3134e-02 | t=0.5134s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.5310e-02 | t=0.0660s
    trss | MR=0.2 | seed=1 | MAE=8.3490e-02 | t=0.1772s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2208e-01 | t=12.4891s
    tv | MR=0.2 | seed=0 | MAE=4.3775e-02 | t=0.1567s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0373e-01 | t=0.0087s
    trss | MR=0.2 | seed=0 | MAE=7.3225e-02 | t=0.0206s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2534e-01 | t=29.5143s

Completed: 2026-04-16T15:02:39.357426+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.