# Integration Log: scr_00428
Started: 2026-04-16T13:28:04.515083+00:00
Description: Screening scr_00428 ds=movielens_graph_signal graph=aew miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0040s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0045s
    tikhonov | MR=0.1 | seed=0 | MAE=2.2943e-02 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=1.4559e-02 | t=0.1882s
    trss | MR=0.1 | seed=0 | MAE=1.7240e-02 | t=0.0167s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=7.8101e-02 | t=0.0081s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.0919e-01 | t=19.7364s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0127s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0044s
    tikhonov | MR=0.1 | seed=1 | MAE=3.0653e-02 | t=0.0126s
    tv | MR=0.1 | seed=1 | MAE=1.9397e-02 | t=0.3690s
    trss | MR=0.1 | seed=1 | MAE=2.5813e-02 | t=0.1490s

Completed: 2026-04-16T13:28:04.515902+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.