# Resumen it131–it150

- Archivos analizados: 20
- Filas combinadas: 4525
- Métrica: `mae`

## Estadísticas por combo (see CSV)
- CSV resumen: it131_it150_summary.csv
- CSV comparación vs baseline: it131_it150_vs_it120_comparison.csv

## Top 10 combos (mejor media)
- bci_iv2a_real_s3 | knn__k3 | trss | missing=0.05 — n=6, mean=1.303079e-07 CI95=[1.283809e-07,1.320166e-07]
- bci_iv2a_real_s2 | knn__k3 | trss | missing=0.05 — n=6, mean=1.459894e-07 CI95=[1.401417e-07,1.536236e-07]
- bci_iv2a_real_s3 | kalofolias | trss | missing=0.1 — n=6, mean=2.132563e-07 CI95=[2.079514e-07,2.182386e-07]
- bci_iv2a_real_s3 | gaussian__sigma1.0 | trss | missing=0.1 — n=6, mean=2.132563e-07 CI95=[2.083629e-07,2.180364e-07]
- bci_iv2a_real_s3 | knn__k3 | sobolev_temporal | missing=0.1 — n=8, mean=2.448265e-07 CI95=[2.419347e-07,2.482613e-07]
- bci_iv2a_real_s2 | kalofolias | trss | missing=0.1 — n=6, mean=2.473601e-07 CI95=[2.407061e-07,2.546377e-07]
- bci_iv2a_real_s2 | gaussian__sigma1.0 | trss | missing=0.1 — n=6, mean=2.473601e-07 CI95=[2.406298e-07,2.547364e-07]
- bci_iv2a_real_s3 | knn__k3 | nearest | missing=0.1 — n=5, mean=2.532336e-07 CI95=[2.463061e-07,2.626750e-07]
- bci_iv2a_real_s3 | knn__k3 | directed_tv | missing=0.05 — n=6, mean=2.645105e-07 CI95=[2.569081e-07,2.718926e-07]
- bci_iv2a_real_s3 | knn__k3 | trss | missing=0.1 — n=31, mean=2.667144e-07 CI95=[2.649307e-07,2.684986e-07]

## Comparación vs baseline (it120/unified)
### Top 10 mejoras (delta negativo = mejor)
- iv100hz_mat|knn__k3|mean|mr=0.2 — mean_new=4.159726e+01, mean_old=4.169133e+01, delta=-9.407932e-02, p=0.734, r_rb=-0.167
- iv100hz_mat|knn__k3|tikhonov|mr=0.2 — mean_new=1.007121e+02, mean_old=1.007264e+02, delta=-1.426362e-02, p=0.746, r_rb=0.200
- bci_iv2a_real_s1|knn__k3|trss|mr=0.2 — mean_new=1.500771e-06, mean_old=1.701323e-06, delta=-2.005523e-07, p=0.228, r_rb=0.507
- bci_iv2a_real_s1|gaussian__sigma1.0|mean|mr=0.2 — mean_new=2.391008e-06, mean_old=2.468947e-06, delta=-7.793880e-08, p=0.193, r_rb=0.636
- bci_iv2a_real_s1|gaussian__sigma1.0|tv|mr=0.2 — mean_new=2.391008e-06, mean_old=2.468947e-06, delta=-7.793880e-08, p=0.193, r_rb=0.636
- bci_iv2a_real_s1|knn__k3|mean|mr=0.2 — mean_new=2.405129e-06, mean_old=2.468947e-06, delta=-6.381779e-08, p=0.183, r_rb=0.576
- bci_iv2a_real_s1|knn__k3|tv|mr=0.2 — mean_new=2.411966e-06, mean_old=2.468752e-06, delta=-5.678561e-08, p=0.179, r_rb=0.571
- bci_iv2a_real_s1|knn__k3|tikhonov|mr=0.2 — mean_new=5.399089e-06, mean_old=5.444767e-06, delta=-4.567836e-08, p=0.174, r_rb=0.643
- bci_iv2a_real_s1|gaussian__sigma1.0|trss|mr=0.2 — mean_new=1.668781e-06, mean_old=1.713669e-06, delta=-4.488724e-08, p=0.197, r_rb=0.600
- physionet_eegmmidb_real|knn__k3|trss|mr=0.4 — mean_new=5.088313e-06, mean_old=5.130726e-06, delta=-4.241291e-08, p=0.613, r_rb=0.333

### Top 10 empeoramientos
- iv100hz_mat|knn__k3|tv|mr=0.2 — mean_new=5.002567e+01, mean_old=4.055568e+01, delta=9.469984e+00, p=0.826, r_rb=-0.100
- iv100hz_mat|knn__k3|trss|mr=0.2 — mean_new=3.905284e+01, mean_old=3.400998e+01, delta=5.042862e+00, p=0.877, r_rb=-0.071
- iv100hz_mat|gaussian__sigma1.0|tv|mr=0.2 — mean_new=2.676462e+01, mean_old=2.545905e+01, delta=1.305569e+00, p=0.613, r_rb=-0.333
- iv100hz_mat|gaussian__sigma1.0|mean|mr=0.2 — mean_new=4.179148e+01, mean_old=4.169133e+01, delta=1.001432e-01, p=0.613, r_rb=-0.333
- iv100hz_mat|gaussian__sigma1.0|trss|mr=0.2 — mean_new=2.988233e+01, mean_old=2.983085e+01, delta=5.147790e-02, p=0.743, r_rb=-0.200
- iv100hz_mat|knn__k3|trss|mr=0.4 — mean_new=8.824397e+01, mean_old=8.819303e+01, delta=5.094734e-02, p=0.866, r_rb=0.167
- physionet_eegmmidb_real|knn__k3|trss|mr=0.2 — mean_new=2.793846e-06, mean_old=1.962616e-06, delta=8.312306e-07, p=0.857, r_rb=-0.079
- physionet_eegmmidb_real|knn__k3|tv|mr=0.2 — mean_new=4.763436e-06, mean_old=3.982037e-06, delta=7.813984e-07, p=0.941, r_rb=-0.037
- physionet_eegmmidb_real|gaussian__sigma1.0|trss|mr=0.2 — mean_new=3.025482e-06, mean_old=3.007181e-06, delta=1.830046e-08, p=0.82, r_rb=0.133
- bci_iv2a_real_s2|knn__k3|trss|mr=0.4 — mean_new=1.406227e-06, mean_old=1.394422e-06, delta=1.180482e-08, p=0.613, r_rb=-0.333