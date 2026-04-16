# Integration Log: it150_041
Started: 2026-04-15T00:29:37.324176+00:00
Description: Bulk normalized run it150_041 dataset=bci_iv2a_real_s3 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.0022s
    nearest | MR=0.1 | seed=0 | MAE=2.9251e-02 | t=0.0045s
    tikhonov | MR=0.1 | seed=0 | MAE=2.8972e-01 | t=0.0078s
    tv | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.2302s
    trss | MR=0.1 | seed=0 | MAE=2.5335e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.7686e-01 | t=0.0145s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.2996e-01 | t=2.2884s
    mean | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.0038s
    nearest | MR=0.1 | seed=1 | MAE=2.9433e-02 | t=0.0036s
    tikhonov | MR=0.1 | seed=1 | MAE=2.8921e-01 | t=0.0092s
    tv | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.2497s
    trss | MR=0.1 | seed=1 | MAE=2.3608e-02 | t=0.0178s

Completed: 2026-04-15T00:29:37.325082+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.