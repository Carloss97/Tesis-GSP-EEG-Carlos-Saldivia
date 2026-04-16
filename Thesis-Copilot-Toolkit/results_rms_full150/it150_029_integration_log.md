# Integration Log: it150_029
Started: 2026-04-15T00:27:27.716521+00:00
Description: Bulk normalized run it150_029 dataset=bci_iv2a_real_s3 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.0026s
    nearest | MR=0.1 | seed=0 | MAE=2.9251e-02 | t=0.0067s
    tikhonov | MR=0.1 | seed=0 | MAE=2.8972e-01 | t=0.0118s
    tv | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.2671s
    trss | MR=0.1 | seed=0 | MAE=2.5335e-02 | t=0.0189s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.7686e-01 | t=0.0109s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.2996e-01 | t=4.0231s
    mean | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=2.9433e-02 | t=0.0057s
    tikhonov | MR=0.1 | seed=1 | MAE=2.8921e-01 | t=0.0092s
    tv | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.2640s
    trss | MR=0.1 | seed=1 | MAE=2.3608e-02 | t=0.0186s

Completed: 2026-04-15T00:27:27.717519+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.