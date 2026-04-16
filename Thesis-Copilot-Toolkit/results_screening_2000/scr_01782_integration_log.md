# Integration Log: scr_01782
Started: 2026-04-16T09:36:26.981996+00:00
Description: Screening scr_01782 ds=iv100hz_mat graph=gaussian miss=3ch mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0023s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=4.7261e-02 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=1.2611e-02 | t=0.1858s
    trss | MR=0.2 | seed=0 | MAE=1.2743e-02 | t=0.0202s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.6587e-02 | t=0.0088s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.3303e-02 | t=1.2508s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=4.7318e-02 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=1.0753e-02 | t=0.1854s
    trss | MR=0.2 | seed=1 | MAE=1.2807e-02 | t=0.0208s

Completed: 2026-04-16T09:36:26.982872+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.