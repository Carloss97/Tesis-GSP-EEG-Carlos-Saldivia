# Integration Log: scr_00698
Started: 2026-04-16T15:26:38.609842+00:00
Description: Screening scr_00698 ds=physionet_real graph=gaussian miss=[0.4] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.0341s
    nearest | MR=0.4 | seed=0 | MAE=1.1571e-05 | t=0.0590s
    tikhonov | MR=0.4 | seed=0 | MAE=1.9831e-05 | t=0.0438s
    tv | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.9225s
    trss | MR=0.4 | seed=0 | MAE=8.5305e-06 | t=0.1066s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.2761e-05 | t=0.0408s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=3.9904e-05 | t=14.6797s
    mean | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.0035s
    nearest | MR=0.4 | seed=1 | MAE=1.1385e-05 | t=0.0211s
    tikhonov | MR=0.4 | seed=1 | MAE=1.9846e-05 | t=0.0825s
    tv | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.9505s
    trss | MR=0.4 | seed=1 | MAE=8.5118e-06 | t=0.1689s

Completed: 2026-04-16T15:26:38.610750+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.