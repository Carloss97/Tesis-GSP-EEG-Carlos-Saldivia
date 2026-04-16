# Integration Log: it150_061
Started: 2026-04-15T00:50:49.997244+00:00
Description: Bulk normalized run it150_061 dataset=mne_sample graph=knng miss=[0.1] mode=base

## Dataset: mne_sample | rows=14
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.0108s
    nearest | MR=0.1 | seed=0 | MAE=1.0002e-01 | t=0.0286s
    tikhonov | MR=0.1 | seed=0 | MAE=3.3972e-01 | t=0.0107s
    tv | MR=0.1 | seed=0 | MAE=7.9442e-02 | t=0.2140s
    trss | MR=0.1 | seed=0 | MAE=5.8626e-02 | t=0.0193s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.1407e-01 | t=0.0126s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.8502e-01 | t=5.7518s
    mean | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.0042s
    nearest | MR=0.1 | seed=1 | MAE=1.0381e-01 | t=0.0083s
    tikhonov | MR=0.1 | seed=1 | MAE=3.3950e-01 | t=0.0111s
    tv | MR=0.1 | seed=1 | MAE=7.8821e-02 | t=0.2546s
    trss | MR=0.1 | seed=1 | MAE=5.8160e-02 | t=0.0202s

Completed: 2026-04-15T00:50:49.997990+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.