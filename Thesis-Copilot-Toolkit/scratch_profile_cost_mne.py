import sys
import os
import time
from pathlib import Path
import warnings
import numpy as np
import mne
from scipy.spatial.distance import cdist

ROOT = Path('.').resolve()
sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_mne_sample_dataset
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals

def profile_methods():
    print("Cargando dataset MNE Sample...")
    data_dict = load_mne_sample_dataset()
    sfreq = data_dict['info'].get('sfreq', 600.0)
    data_clean = data_dict['signals']
    positions = data_dict['positions']
    ch_names = data_dict.get('ch_names', [f'CH{i}' for i in range(len(positions))])
    
    montage = mne.channels.make_dig_montage(ch_pos=dict(zip(ch_names, positions)))
    info = mne.create_info(ch_names, sfreq, 'eeg')
    info.set_montage(montage)
    
    D = len(ch_names)
    n_missing = int(D * 0.1) # 10%
    rng = np.random.default_rng(42)
    bad_idx = rng.choice(D, n_missing, replace=False) # random
    bad_ch_names = [ch_names[i] for i in bad_idx]
    
    # Precompute TRSS graph
    g = build_graph('knng', positions, k=4, sigma=1.0)
    adj = g['adjacency'].toarray() if hasattr(g['adjacency'], 'toarray') else np.asarray(g['adjacency'])
    
    # 1s, 4s, 16s at 600Hz
    sample_sizes = [600, 2400, 9600] 
    
    print("\n--- INICIANDO PROFILING DE COSTO COMPUTACIONAL ---")
    print(f"Dataset: MNE Sample ({D} canales) | Pérdida: Random 10% ({n_missing} canales)\n")
    print(f"{'Muestras':<10} | {'Tiempo MNE (ms)':<15} | {'Tiempo TRSS (ms)':<15} | {'Ratio (TRSS/MNE)'}")
    print("-" * 65)
    
    for n_samples in sample_sizes:
        data_missing = data_clean[:n_samples].copy()
        data_missing[:, bad_idx] = np.nan
        
        # --- Profile MNE ---
        raw_mne = mne.io.RawArray(data_missing.T.copy(), info, verbose=False)
        raw_mne.info['bads'] = bad_ch_names
        
        # warmup
        raw_mne.copy().interpolate_bads(reset_bads=True, method='spline', origin='auto', verbose=False)
        
        t0 = time.perf_counter()
        for _ in range(5):
            raw_mne.copy().interpolate_bads(reset_bads=True, method='spline', origin='auto', verbose=False)
        t_mne = ((time.perf_counter() - t0) / 5) * 1000
        
        # --- Profile TRSS ---
        # warmup
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            interpolate_signals('trss', data_missing, adjacency=adj, alpha=4.77, beta=0.0094, lr=0.05, n_iter=80)
            
        t0 = time.perf_counter()
        for _ in range(5):
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                interpolate_signals('trss', data_missing, adjacency=adj, alpha=4.77, beta=0.0094, lr=0.05, n_iter=80)
        t_trss = ((time.perf_counter() - t0) / 5) * 1000
        
        print(f"{n_samples:<10} | {t_mne:<15.2f} | {t_trss:<15.2f} | {t_trss/t_mne:.2f}x")

if __name__ == '__main__':
    profile_methods()
