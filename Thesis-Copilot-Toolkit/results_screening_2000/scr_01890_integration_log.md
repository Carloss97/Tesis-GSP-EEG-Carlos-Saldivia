# Integration Log: scr_01890
Started: 2026-04-16T09:51:42.900368+00:00
Description: Screening scr_01890 ds=iv100hz_mat graph=gaussian miss=[0.1] mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0046s
    tikhonov | MR=0.2 | seed=0 | MAE=4.7261e-02 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=1.2611e-02 | t=0.1841s
    trss | MR=0.2 | seed=0 | MAE=1.2743e-02 | t=0.0202s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.6587e-02 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.3303e-02 | t=1.2410s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0022s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0045s
    tikhonov | MR=0.2 | seed=1 | MAE=4.7318e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=1.0753e-02 | t=0.1875s
    trss | MR=0.2 | seed=1 | MAE=1.2807e-02 | t=0.0200s

Completed: 2026-04-16T09:51:42.901086+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.