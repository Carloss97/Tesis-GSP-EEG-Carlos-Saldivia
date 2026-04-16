# Integration Log: pilot_0016
Started: 2026-04-16T06:29:12.737405+00:00
Description: Pilot run pilot_0016 dataset=physionet_real graph=knn miss=[0.1]

## Dataset: physionet_eegmmidb_real | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=4.4949e-02 | t=0.0034s
    tv | MR=0.1 | seed=0 | MAE=3.8597e-02 | t=0.1586s
    trss | MR=0.1 | seed=0 | MAE=1.9006e-02 | t=0.0163s
    mean | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=4.3518e-02 | t=0.0027s
    tv | MR=0.1 | seed=1 | MAE=3.7556e-02 | t=0.1468s
    trss | MR=0.1 | seed=1 | MAE=1.8084e-02 | t=0.0165s

Completed: 2026-04-16T06:29:12.738180+00:00
Total rows: 8
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.