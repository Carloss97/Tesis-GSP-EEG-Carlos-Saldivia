# Integration Log: scr_00496
Started: 2026-04-16T13:50:15.654469+00:00
Description: Screening scr_00496 ds=bci_iv2a_real_s2 graph=kalofolias miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=8.0037e-07 | t=0.0049s
    tikhonov | MR=0.2 | seed=0 | MAE=2.1884e-06 | t=0.0064s
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.1969s
    trss | MR=0.2 | seed=0 | MAE=6.5818e-07 | t=0.0182s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.0165e-06 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5226e-05 | t=20.5847s
    mean | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.0023s
    nearest | MR=0.2 | seed=1 | MAE=8.8678e-07 | t=0.0073s
    tikhonov | MR=0.2 | seed=1 | MAE=2.1997e-06 | t=0.0063s
    tv | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.4104s
    trss | MR=0.2 | seed=1 | MAE=6.9089e-07 | t=0.3109s

Completed: 2026-04-16T13:50:15.655385+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.