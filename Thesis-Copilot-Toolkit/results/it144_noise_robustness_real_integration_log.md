# Integration Log: it144_noise_robustness_real
Started: 2026-04-13T18:35:34.935518+00:00
Description: Noise robustness (non-gaussian) on real data

## Dataset: iv100hz_mat | rows=60
  Graph: knn__k3 built OK
    trss | MR=0.2 | seed=0 | MAE=3.4060e+01 | t=0.0197s
    heat_diffusion_temporal | MR=0.2 | seed=0 | MAE=3.8202e+02 | t=0.0417s
    tv | MR=0.2 | seed=0 | MAE=4.0539e+01 | t=0.1735s
    trss | MR=0.2 | seed=1 | MAE=3.4241e+01 | t=0.0196s
    heat_diffusion_temporal | MR=0.2 | seed=1 | MAE=3.8569e+02 | t=0.0420s
    tv | MR=0.2 | seed=1 | MAE=3.9758e+01 | t=0.1635s
    trss | MR=0.2 | seed=2 | MAE=3.5014e+01 | t=0.0194s
    heat_diffusion_temporal | MR=0.2 | seed=2 | MAE=3.7716e+02 | t=0.0390s
    tv | MR=0.2 | seed=2 | MAE=3.9854e+01 | t=0.1568s
    trss | MR=0.2 | seed=3 | MAE=3.3735e+01 | t=0.0184s
    heat_diffusion_temporal | MR=0.2 | seed=3 | MAE=3.7822e+02 | t=0.0415s
    tv | MR=0.2 | seed=3 | MAE=4.1041e+01 | t=0.1659s

## Dataset: physionet_eegmmidb_real | rows=60
  Graph: knn__k3 built OK
    trss | MR=0.2 | seed=0 | MAE=2.0376e-06 | t=0.0204s
    heat_diffusion_temporal | MR=0.2 | seed=0 | MAE=6.4679e-06 | t=0.0411s
    tv | MR=0.2 | seed=0 | MAE=4.0277e-06 | t=0.1756s
    trss | MR=0.2 | seed=1 | MAE=2.0268e-06 | t=0.0205s
    heat_diffusion_temporal | MR=0.2 | seed=1 | MAE=6.4801e-06 | t=0.0503s
    tv | MR=0.2 | seed=1 | MAE=3.9966e-06 | t=0.1894s
    trss | MR=0.2 | seed=2 | MAE=1.9394e-06 | t=0.0315s
    heat_diffusion_temporal | MR=0.2 | seed=2 | MAE=6.5037e-06 | t=0.0388s
    tv | MR=0.2 | seed=2 | MAE=3.9909e-06 | t=0.1856s
    trss | MR=0.2 | seed=3 | MAE=2.0292e-06 | t=0.0186s
    heat_diffusion_temporal | MR=0.2 | seed=3 | MAE=6.4704e-06 | t=0.0371s
    tv | MR=0.2 | seed=3 | MAE=4.1781e-06 | t=0.1660s

Completed: 2026-04-13T18:35:34.937948+00:00
Total rows: 120
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.