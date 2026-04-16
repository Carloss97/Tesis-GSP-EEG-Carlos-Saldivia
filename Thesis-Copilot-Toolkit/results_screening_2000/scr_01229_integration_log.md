# Integration Log: scr_01229
Started: 2026-04-16T08:22:48.075198+00:00
Description: Screening scr_01229 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.1869s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6180e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=2.8663e-02 | t=0.0183s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.9513e-01 | t=1.2856s
    tv | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.1886s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.6266e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.0563e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.9340e-01 | t=1.3739s
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.1884s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1137e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.0629e-02 | t=0.0185s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.9815e-01 | t=1.5180s

Completed: 2026-04-16T08:22:48.076051+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.