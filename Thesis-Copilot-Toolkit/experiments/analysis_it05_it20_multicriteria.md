# Multicriteria analysis â€” IT05 + IT20
Generated: 2026-04-14T01:50:10

## Criteria evaluated
- mean_based: ranking by mean MAE (mean + 0.5*std) on all data
- real_only_mean: same as mean_based but computed only on non-synthetic datasets
- median_based: ranking by median MAE (robust)
- stability_first: ranking by mean+std (penalize high variance)

### Mean-based (full)

**Top 3 generalists**
- aew__k4_sigma_corr0_5_sigma_dist1 | heat_diffusion_temporal: mean_mae=0.1356 std_mae=0.0988 datasets=4
    - physionet_eegmmidb: mae=2E-06
    - physionet_eegmmidb: mae=5E-06
    - physionet_eegmmidb: mae=1E-05
    - physionet_eegmmidb: mae=1.4E-05
    - synthetic_beta: mae=0.065834
- kalofolias | directed_tv: mean_mae=0.1358 std_mae=0.099 datasets=4
    - physionet_eegmmidb: mae=2E-06
    - physionet_eegmmidb: mae=6E-06
    - physionet_eegmmidb: mae=1.1E-05
    - physionet_eegmmidb: mae=1.5E-05
    - synthetic_beta: mae=0.065885
- aew__k4_sigma_corr0_5_sigma_dist1 | trss: mean_mae=0.1365 std_mae=0.0992 datasets=4
    - physionet_eegmmidb: mae=2E-06
    - physionet_eegmmidb: mae=4E-06
    - physionet_eegmmidb: mae=8E-06
    - physionet_eegmmidb: mae=1.2E-05
    - synthetic_beta: mae=0.065751

**Top 3 temporal**
- nnk__k4 | spline_temporal: mean_mae=0 std_mae=0 datasets=4
- knn__k3 | spline_temporal: mean_mae=0 std_mae=0 datasets=4
- knng__k4_sigma1 | spline_temporal: mean_mae=0 std_mae=0 datasets=4

**Top 3 instant**
- vknng__alpha1_k4_k_max8_k_min2 | mean: mean_mae=0.1369 std_mae=0.1005 datasets=4
- kalofolias | mean: mean_mae=0.1369 std_mae=0.1005 datasets=4
- knn__k5 | mean: mean_mae=0.1369 std_mae=0.1005 datasets=4

**Baselines**
- method=mean: best_graph=nnk__k4 mean_mae=0.1369
- method=nearest: best_graph=nnk__k4 mean_mae=0.1766
- method=linear: best_graph=nnk__k4 mean_mae=0.1634

### Real-only mean

**Top 3 generalists**

**Top 3 temporal**
- gaussian__sigma1 | spline_temporal: mean_mae=0 std_mae=0 datasets=1
- vknng__alpha1_k4_k_max8_k_min2 | spline_temporal: mean_mae=0 std_mae=0 datasets=1
- knn__k3 | spline_temporal: mean_mae=0 std_mae=0 datasets=1

**Top 3 instant**
- aew__k4_sigma_corr0_5_sigma_dist1 | gsmooth: mean_mae=0 std_mae=0 datasets=1
- aew__k4_sigma_corr0_5_sigma_dist1 | gsp: mean_mae=0 std_mae=0 datasets=1
- gaussian__sigma1 | gsp: mean_mae=0 std_mae=0 datasets=1

**Baselines**
- method=mean: best_graph=nnk__k4 mean_mae=0
- method=nearest: best_graph=nnk__k4 mean_mae=0
- method=linear: best_graph=nnk__k4 mean_mae=0

### Median-based (robust)

**Top 3 generalists**
- aew__k4_sigma_corr0_5_sigma_dist1 | gsmooth: mean_mae=0.1376 std_mae=0.1012 datasets=4
    - physionet_eegmmidb: mae=2E-06
    - physionet_eegmmidb: mae=4E-06
    - physionet_eegmmidb: mae=8E-06
    - physionet_eegmmidb: mae=1.2E-05
    - synthetic_alpha: mae=0.065433
- knn__k5 | tv: mean_mae=0.1371 std_mae=0.1005 datasets=4
    - physionet_eegmmidb: mae=2E-06
    - physionet_eegmmidb: mae=5E-06
    - physionet_eegmmidb: mae=9E-06
    - physionet_eegmmidb: mae=1.3E-05
    - synthetic_alpha: mae=0.061299
- gaussian__sigma1 | gsmooth: mean_mae=0.1373 std_mae=0.1006 datasets=4
    - physionet_eegmmidb: mae=2E-06
    - physionet_eegmmidb: mae=5E-06
    - physionet_eegmmidb: mae=9E-06
    - physionet_eegmmidb: mae=1.3E-05
    - synthetic_alpha: mae=0.06206

**Top 3 temporal**
- knn__k5 | spline_temporal: mean_mae=0 std_mae=0 datasets=4
- aew__k4_sigma_corr0_5_sigma_dist1 | spline_temporal: mean_mae=0 std_mae=0 datasets=4
- knn__k3 | spline_temporal: mean_mae=0 std_mae=0 datasets=4

**Top 3 instant**
- aew__k4_sigma_corr0_5_sigma_dist1 | gsmooth: mean_mae=0.1376 std_mae=0.1012 datasets=4
- gaussian__sigma1 | gsmooth: mean_mae=0.1373 std_mae=0.1006 datasets=4
- kalofolias | mean: mean_mae=0.1369 std_mae=0.1005 datasets=4

**Baselines**
- method=mean: best_graph=nnk__k4 mean_mae=0.1369
- method=nearest: best_graph=nnk__k4 mean_mae=0.1766
- method=linear: best_graph=nnk__k4 mean_mae=0.1634

### Stability-first

**Top 3 generalists**
- aew__k4_sigma_corr0_5_sigma_dist1 | heat_diffusion_temporal: mean_mae=0.1356 std_mae=0.0988 datasets=4
    - physionet_eegmmidb: mae=2E-06
    - physionet_eegmmidb: mae=5E-06
    - physionet_eegmmidb: mae=1E-05
    - physionet_eegmmidb: mae=1.4E-05
    - synthetic_beta: mae=0.065834
- kalofolias | directed_tv: mean_mae=0.1358 std_mae=0.099 datasets=4
    - physionet_eegmmidb: mae=2E-06
    - physionet_eegmmidb: mae=6E-06
    - physionet_eegmmidb: mae=1.1E-05
    - physionet_eegmmidb: mae=1.5E-05
    - synthetic_beta: mae=0.065885
- aew__k4_sigma_corr0_5_sigma_dist1 | trss: mean_mae=0.1365 std_mae=0.0992 datasets=4
    - physionet_eegmmidb: mae=2E-06
    - physionet_eegmmidb: mae=4E-06
    - physionet_eegmmidb: mae=8E-06
    - physionet_eegmmidb: mae=1.2E-05
    - synthetic_beta: mae=0.065751

**Top 3 temporal**
- nnk__k4 | spline_temporal: mean_mae=0 std_mae=0 datasets=4
- knn__k3 | spline_temporal: mean_mae=0 std_mae=0 datasets=4
- knng__k4_sigma1 | spline_temporal: mean_mae=0 std_mae=0 datasets=4

**Top 3 instant**
- vknng__alpha1_k4_k_max8_k_min2 | mean: mean_mae=0.1369 std_mae=0.1005 datasets=4
- kalofolias | mean: mean_mae=0.1369 std_mae=0.1005 datasets=4
- knn__k5 | mean: mean_mae=0.1369 std_mae=0.1005 datasets=4

**Baselines**
- method=mean: best_graph=nnk__k4 mean_mae=0.1369
- method=nearest: best_graph=nnk__k4 mean_mae=0.1766
- method=linear: best_graph=nnk__k4 mean_mae=0.1634


