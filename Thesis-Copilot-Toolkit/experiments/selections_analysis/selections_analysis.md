# Selections analysis â€” per-graph, per-method, top combos

## Global stats
- Global mean MAE: 0.221047
- Global std MAE: 0.127225

## Top 10 by mean MAE
- aew__k4_sigma_corr0_5_sigma_dist1|heat_diffusion_temporal: mean=0.135567 median=0.132588 graph=aew__k4_sigma_corr0_5_sigma_dist1 method=heat_diffusion_temporal
- kalofolias|directed_tv: mean=0.135784 median=0.133484 graph=kalofolias method=directed_tv
- aew__k4_sigma_corr0_5_sigma_dist1|trss: mean=0.136464 median=0.129533 graph=aew__k4_sigma_corr0_5_sigma_dist1 method=trss
- gaussian__sigma1|heat_diffusion_temporal: mean=0.1365 median=0.131566 graph=gaussian__sigma1 method=heat_diffusion_temporal
- gaussian__sigma1|directed_tv: mean=0.136801 median=0.138097 graph=gaussian__sigma1 method=directed_tv
- gaussian__sigma1|mean: mean=0.136906 median=0.129792 graph=gaussian__sigma1 method=mean
- knng__k4_sigma1|mean: mean=0.136906 median=0.129792 graph=knng__k4_sigma1 method=mean
- aew__k4_sigma_corr0_5_sigma_dist1|mean: mean=0.136906 median=0.129792 graph=aew__k4_sigma_corr0_5_sigma_dist1 method=mean
- nnk__k4|mean: mean=0.136906 median=0.129792 graph=nnk__k4 method=mean
- knn__k5|mean: mean=0.136906 median=0.129792 graph=knn__k5 method=mean

## Top 10 by median MAE
- aew__k4_sigma_corr0_5_sigma_dist1|gsmooth: median=0.126405 mean=0.137605 graph=aew__k4_sigma_corr0_5_sigma_dist1 method=gsmooth
- knn__k5|tv: median=0.129474 mean=0.137128 graph=knn__k5 method=tv
- gaussian__sigma1|gsmooth: median=0.129493 mean=0.137314 graph=gaussian__sigma1 method=gsmooth
- aew__k4_sigma_corr0_5_sigma_dist1|trss: median=0.129533 mean=0.136464 graph=aew__k4_sigma_corr0_5_sigma_dist1 method=trss
- gaussian__sigma1|tv: median=0.129537 mean=0.137137 graph=gaussian__sigma1 method=tv
- kalofolias|tv: median=0.129792 mean=0.13694 graph=kalofolias method=tv
- nnk__k4|mean: median=0.129792 mean=0.136906 graph=nnk__k4 method=mean
- gaussian__sigma1|mean: median=0.129792 mean=0.136906 graph=gaussian__sigma1 method=mean
- knn__k3|mean: median=0.129792 mean=0.136906 graph=knn__k3 method=mean
- aew__k4_sigma_corr0_5_sigma_dist1|mean: median=0.129792 mean=0.136906 graph=aew__k4_sigma_corr0_5_sigma_dist1 method=mean

## Per-graph best combos (summary)
- knn__k3: best_combo=knn__k3|mean mean=0.136906 combos=22
- nnk__k4: best_combo=nnk__k4|mean mean=0.136906 combos=22
- gaussian__sigma1: best_combo=gaussian__sigma1|heat_diffusion_temporal mean=0.1365 combos=22
- aew__k4_sigma_corr0_5_sigma_dist1: best_combo=aew__k4_sigma_corr0_5_sigma_dist1|heat_diffusion_temporal mean=0.135567 combos=22
- kalofolias: best_combo=kalofolias|directed_tv mean=0.135784 combos=22
- knn__k5: best_combo=knn__k5|mean mean=0.136906 combos=22
- vknng__alpha1_k4_k_max8_k_min2: best_combo=vknng__alpha1_k4_k_max8_k_min2|mean mean=0.136906 combos=22
- knng__k4_sigma1: best_combo=knng__k4_sigma1|mean mean=0.136906 combos=22

