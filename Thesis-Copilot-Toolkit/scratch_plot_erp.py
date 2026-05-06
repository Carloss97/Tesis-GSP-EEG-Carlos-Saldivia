import sys
from pathlib import Path
import warnings
import numpy as np
import mne
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

ROOT = Path('.').resolve()
sys.path.insert(0, str(ROOT))

from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals

def main():
    print("Loading MNE Sample...")
    data_path = mne.datasets.sample.data_path()
    raw_fname = data_path / 'MEG' / 'sample' / 'sample_audvis_raw.fif'
    
    raw = mne.io.read_raw_fif(raw_fname, preload=True, verbose=False)
    # Filter for ERPs
    raw.filter(1, 30, fir_design='firwin', verbose=False)
    
    # Extract events (Auditory Left = 1)
    events = mne.find_events(raw, stim_channel='STI 014', verbose=False)
    event_id = {'Auditory/Left': 1}
    
    # Pick EEG channels
    picks = mne.pick_types(raw.info, meg=False, eeg=True, eog=False, stim=False, exclude='bads')
    
    # Epoching
    epochs = mne.Epochs(raw, events, event_id, tmin=-0.2, tmax=0.5, picks=picks, baseline=(None, 0), preload=True, verbose=False)
    
    # Get Evoked ground truth
    evoked_gt = epochs.average()
    
    # Get positions
    pos_dict = {ch: epochs.info['chs'][idx]['loc'][:3] for idx, ch in enumerate(epochs.ch_names)}
    positions = np.array([pos_dict[ch] for ch in epochs.ch_names])
    n_channels = len(epochs.ch_names)
    
    # Simulate static Nearby 40% mask
    n_missing = int(n_channels * 0.4)
    rng = np.random.default_rng(42)
    center_idx = rng.choice(n_channels)
    dists = cdist(positions, positions)
    bad_idx = np.argsort(dists[center_idx])[:n_missing]
    bad_ch_names = [epochs.ch_names[i] for i in bad_idx]
    
    print(f"Bad channels (40% nearby): {bad_ch_names}")
    
    # Target channel to plot (let's pick the center one)
    target_ch = epochs.ch_names[center_idx]
    target_idx = center_idx
    
    # --- MNE Interpolation ---
    print("Interpolating MNE...")
    epochs_mne = epochs.copy()
    epochs_mne.info['bads'] = bad_ch_names
    epochs_mne.interpolate_bads(reset_bads=True, method='spline', origin='auto', verbose=False)
    evoked_mne = epochs_mne.average()
    
    # --- TRSS Interpolation ---
    print("Interpolating TRSS...")
    data_epochs = epochs.get_data(copy=True) # (n_epochs, n_channels, n_times)
    n_epochs, _, n_times = data_epochs.shape
    
    data_trss_epochs = np.zeros_like(data_epochs)
    
    g = build_graph('knng', positions, k=4, sigma=1.0)
    adj = g['adjacency'].toarray() if hasattr(g['adjacency'], 'toarray') else np.asarray(g['adjacency'])
    
    # Use TRSS Optimized values found previously for mne_sample nearby 0.4
    for i in range(n_epochs):
        ep_data = data_epochs[i].T.copy() # (n_times, n_channels)
        ep_data[:, bad_idx] = np.nan
        
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            res = interpolate_signals('trss', ep_data, adjacency=adj, alpha=0.24, beta=0.01, lr=0.05, n_iter=80)
        
        data_trss_epochs[i] = res['reconstructed'].T
    
    # Create TRSS Epochs object for easy averaging
    epochs_trss = mne.EpochsArray(data_trss_epochs, epochs.info, tmin=-0.2, verbose=False)
    evoked_trss = epochs_trss.average()
    
    # --- Plotting ERP ---
    print("Plotting...")
    times = evoked_gt.times * 1000 # to ms
    
    gt_data = evoked_gt.data[target_idx] * 1e6 # to uV
    mne_data = evoked_mne.data[target_idx] * 1e6
    trss_data = evoked_trss.data[target_idx] * 1e6
    
    plt.figure(figsize=(10, 6))
    plt.plot(times, gt_data, label='Ground Truth', color='black', linewidth=2)
    plt.plot(times, mne_data, label='MNE (Spherical Spline)', color='purple', linestyle='--', linewidth=2)
    plt.plot(times, trss_data, label='TRSS (Optimizado)', color='#004b87', linestyle='-.', linewidth=2)
    
    plt.axvline(0, color='gray', linestyle=':')
    plt.axhline(0, color='gray', linestyle=':')
    
    plt.title(f'ERP Reconstruido en MNE Sample (Pérdida estática 40% cluster)\nCanal {target_ch} (Estimulo Auditivo Izquierdo)')
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Amplitud (µV)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    out_path = ROOT / 'results_optuna_final' / 'erp_comparison_static_mne_trss.png'
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Plot saved to {out_path}")
    
    # --- Plotting Single Time Series Snippet ---
    raw_gt = epochs.get_data()[0] # First epoch
    raw_mne = epochs_mne.get_data()[0]
    raw_trss = epochs_trss.get_data()[0]
    
    gt_ts = raw_gt[target_idx] * 1e6
    mne_ts = raw_mne[target_idx] * 1e6
    trss_ts = raw_trss[target_idx] * 1e6
    
    plt.figure(figsize=(12, 4))
    plt.plot(times, gt_ts, label='Ground Truth', color='black', alpha=0.8)
    plt.plot(times, mne_ts, label='MNE (Spline)', color='purple', alpha=0.8)
    plt.plot(times, trss_ts, label='TRSS', color='#004b87', alpha=0.8)
    
    plt.title(f'Serie de Tiempo (1 Época Unica) - Canal {target_ch}')
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Amplitud (µV)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    out_ts = ROOT / 'results_optuna_final' / 'ts_comparison_static_mne_trss.png'
    plt.savefig(out_ts, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {out_ts}")

if __name__ == '__main__':
    main()
