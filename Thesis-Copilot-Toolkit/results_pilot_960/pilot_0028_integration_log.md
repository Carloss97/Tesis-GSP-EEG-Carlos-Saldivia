# Integration Log: pilot_0028
Started: 2026-04-16T06:29:47.370441+00:00
Description: Pilot run pilot_0028 dataset=bci_iv2a_real_s1 graph=knn miss=[0.1]

## Dataset: bci_iv2a_real_s1 | rows=8
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.0024s
    nearest | MR=0.1 | seed=0 | MAE=3.1361e-02 | t=0.0058s
    tv | MR=0.1 | seed=0 | MAE=3.5664e-02 | t=0.1578s
    trss | MR=0.1 | seed=0 | MAE=2.5778e-02 | t=0.0165s
    mean | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=3.1289e-02 | t=0.0027s
    tv | MR=0.1 | seed=1 | MAE=3.3707e-02 | t=0.1502s
    trss | MR=0.1 | seed=1 | MAE=2.3537e-02 | t=0.0161s

Completed: 2026-04-16T06:29:47.371219+00:00
Total rows: 8
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.