import sys
import os
import time
import warnings
import numpy as np
import mne
import scipy.interpolate
from sklearn.decomposition import FastICA
from scipy.spatial.distance import cdist
from pathlib import Path

ROOT = Path('.').resolve()
sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_physionet_eegmmidb
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from src.evaluation.evaluation import evaluate_signals

def run_all_baselines():
    print("Cargando dataset Physionet...")
    data_dict = load_physionet_eegmmidb()
    sfreq = data_dict['info'].get('sfreq', 160.0)
    # Get 4 seconds of data
    data_raw = data_dict['signals'][:640].copy() 
    positions = data_dict['positions']
    ch_names = data_dict.get('ch_names', [f'CH{i}' for i in range(len(positions))])
    
    # Filter data to make it fair for MNE
    data_clean = mne.filter.filter_data(data_raw.T, sfreq, 1.0, 30.0, verbose=False).T
    
    montage = mne.channels.make_dig_montage(ch_pos=dict(zip(ch_names, positions)))
    info = mne.create_info(ch_names, sfreq, 'eeg')
    info.set_montage(montage)
    
    D = len(ch_names)
    
    # Escenario: Alta Perdida (Nearby 40%)
    n_missing = int(D * 0.4)
    rng = np.random.default_rng(42)
    center_idx = rng.choice(D)
    dists = cdist(positions, positions)
    bad_idx = np.argsort(dists[center_idx])[:n_missing]
    good_idx = np.array([i for i in range(D) if i not in bad_idx])
    
    bad_ch_names = [ch_names[i] for i in bad_idx]
    
    data_missing = data_clean.copy()
    data_missing[:, bad_idx] = np.nan
    
    results = {}
    
    print(f"\n--- BENCHMARK MULTI-MÉTODO ---")
    print(f"Pérdida: Nearby 40% ({n_missing} canales) | Ventana: 640 muestras (4 segs)\n")
    
    # 1. MNE (Spherical Spline)
    t0 = time.perf_counter()
    raw_mne = mne.io.RawArray(data_missing.T.copy(), info, verbose=False)
    raw_mne.info['bads'] = bad_ch_names
    raw_mne.interpolate_bads(reset_bads=True, method='spline', origin='auto', verbose=False)
    t_mne = time.perf_counter() - t0
    mne_recon = raw_mne.get_data().T
    res_mne = evaluate_signals(data_clean[:, bad_idx], mne_recon[:, bad_idx], ['mae', 'rmse'])
    results['MNE (Spherical Spline)'] = {'mae': res_mne['mae'], 'time': t_mne}
    
    # 2. RBFI (Thin-Plate Spline)
    t0 = time.perf_counter()
    rbf_recon = data_missing.copy()
    for t in range(len(data_missing)):
        val_good = data_missing[t, good_idx]
        pos_good = positions[good_idx]
        pos_bad = positions[bad_idx]
        
        # Scipy RBF
        rbfi = scipy.interpolate.Rbf(pos_good[:,0], pos_good[:,1], pos_good[:,2], val_good, function='thin_plate')
        rbf_recon[t, bad_idx] = rbfi(pos_bad[:,0], pos_bad[:,1], pos_bad[:,2])
    t_rbf = time.perf_counter() - t0
    res_rbf = evaluate_signals(data_clean[:, bad_idx], rbf_recon[:, bad_idx], ['mae', 'rmse'])
    results['RBFI (Thin-Plate)'] = {'mae': res_rbf['mae'], 'time': t_rbf}
    
    # 3. ICA (FastICA)
    t0 = time.perf_counter()
    # Usamos los canales buenos para entrenar ICA y proyectar
    ica = FastICA(n_components=15, random_state=42)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        sources = ica.fit_transform(data_clean[:, good_idx]) # mezclas de los buenos
        # esto es una simplificación extrema, normalmente ICA requiere todos los canales.
        # Un pipeline ICA de imputación hace PCA iterativo. Usaremos un proxy simple:
    t_ica = time.perf_counter() - t0
    
    # Para ser justos, corremos TRSS
    t0 = time.perf_counter()
    g = build_graph('knng', positions, k=4, sigma=1.0)
    adj = g['adjacency'].toarray() if hasattr(g['adjacency'], 'toarray') else np.asarray(g['adjacency'])
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        res_trss_data = interpolate_signals('trss', data_missing, adjacency=adj, alpha=1.5, beta=0.01, lr=0.05, n_iter=80)
    t_trss = time.perf_counter() - t0
    res_trss = evaluate_signals(data_clean[:, bad_idx], res_trss_data['reconstructed'][:, bad_idx], ['mae', 'rmse'])
    results['TRSS (GSP)'] = {'mae': res_trss['mae'], 'time': t_trss}
    
    print(f"{'Método':<25} | {'MAE (µV)':<10} | {'Tiempo (s)':<10}")
    print("-" * 50)
    for method, metrics in results.items():
        print(f"{method:<25} | {metrics['mae']*1e6:<10.2f} | {metrics['time']:<10.3f}")

if __name__ == '__main__':
    run_all_baselines()
