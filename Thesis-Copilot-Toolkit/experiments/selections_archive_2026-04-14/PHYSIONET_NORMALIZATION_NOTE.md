# Physionet vs Synthetic scale note

Investigation revealed a units/scale mismatch between synthetic datasets and the PhysioNet EEG data:

- Synthetic generators (e.g. make_synthetic_alpha in experiments/run_canonical_experiment.py) produce sinusoids with amplitudes ~1.0 (noise ~0.08).
- PhysioNet loading (src/data/data_loader.py -> load_physionet_eegmmidb) returns raw EEG in Volts/microvolts (typical values ~1e-6), without rescaling.

This causes MAE values from physionet rows to be orders of magnitude smaller than synthetic MAE, biasing global aggregations.

Recommendation: either normalize per-dataset (e.g. z-score or scale to unit range) before computing MAE, or exclude physionet in cross-dataset aggregations. This run uses the latter (no physionet).
