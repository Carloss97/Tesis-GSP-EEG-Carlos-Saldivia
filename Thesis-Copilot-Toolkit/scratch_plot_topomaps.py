import sys
import os
from pathlib import Path
import warnings
import numpy as np
import mne
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import optuna

optuna.logging.set_verbosity(optuna.logging.WARNING)

ROOT = Path('.').resolve()
sys.path.insert(0, str(ROOT))

os.environ["BCI_IV_2A_PATH"] = str(ROOT / "datasets" / "BCICIV_2a_gdf")

from src.data.data_loader import load_bci_competition_iv_2a, load_mne_sample_dataset, load_physionet_eegmmidb
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from src.evaluation.evaluation import evaluate_signals

def create_topomaps_multi(loader, dataset_name):
    print(f"\n[{dataset_name}] Generando Grids de Topomapas...")
    try:
        data_dict = loader()
    except Exception as e:
        print(f"Error loading {dataset_name}: {e}")
        return
        
    sfreq = data_dict['info'].get('sfreq', 250.0)
    data_clean_full = data_dict['signals'][:4000].copy()
    positions = data_dict['positions']
    ch_names = data_dict.get('ch_names', [f'CH{i}' for i in range(len(positions))])
    
    montage = mne.channels.make_dig_montage(ch_pos=dict(zip(ch_names, positions)))
    info = mne.create_info(ch_names, sfreq, 'eeg')
    info.set_montage(montage)
    
    data_clean = mne.filter.filter_data(data_clean_full.T, sfreq, 1.0, 30.0, verbose=False).T
    D = len(ch_names)
    
    # Pick a high variance peak
    variances = np.var(data_clean, axis=1)
    t_peak = np.argmax(variances[1000:3000]) + 1000
    
    scenarios = [
        ('random', 0.1), ('nearby', 0.1), 
        ('random', 0.4), ('nearby', 0.4)
    ]
    
    fig_inst, axes_inst = plt.subplots(4, 4, figsize=(16, 16))
    fig_err, axes_err = plt.subplots(4, 2, figsize=(10, 16))
    
    for i, (mode, loss) in enumerate(scenarios):
        print(f"  -> Scenario {mode} {loss*100}%")
        n_missing = int(D * loss)
        rng = np.random.default_rng(42)
        if mode == 'random':
            bad_idx = rng.choice(D, n_missing, replace=False)
        else:
            center_idx = rng.choice(D)
            dists = cdist(positions, positions)
            bad_idx = np.argsort(dists[center_idx])[:n_missing]
            
        bad_ch_names = [ch_names[idx] for idx in bad_idx]
        data_missing = data_clean.copy()
        data_missing[:, bad_idx] = np.nan
        
        # MNE
        raw_mne = mne.io.RawArray(data_missing.T.copy(), info, verbose=False)
        raw_mne.info['bads'] = bad_ch_names
        raw_mne.interpolate_bads(reset_bads=True, method='spline', origin='auto', verbose=False)
        data_mne = raw_mne.get_data().T
        
        # TRSS Opt
        g = build_graph('knng', positions, k=4, sigma=1.0)
        adj = g['adjacency'].toarray() if hasattr(g['adjacency'], 'toarray') else np.asarray(g['adjacency'])
        
        def objective(trial):
            alpha = trial.suggest_float("alpha", 0.1, 5.0, log=True)
            beta = trial.suggest_float("beta", 0.001, 1.0, log=True)
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                res = interpolate_signals('trss', data_missing[:1500], adjacency=adj, alpha=alpha, beta=beta, lr=0.05, n_iter=80)
            met = evaluate_signals(data_clean[:1500, bad_idx], res['reconstructed'][:, bad_idx], metrics=['mae'])
            return met['mae']
        study = optuna.create_study(direction="minimize")
        study.optimize(objective, n_trials=5)
        best_p = study.best_params
        
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            res_trss = interpolate_signals('trss', data_missing, adjacency=adj, alpha=best_p['alpha'], beta=best_p['beta'], lr=0.05, n_iter=80)
        data_trss = res_trss['reconstructed']
        
        # Instant values
        val_gt = data_clean[t_peak]
        val_missing = data_missing[t_peak].copy()
        val_missing[np.isnan(val_missing)] = 0.0
        val_mne = data_mne[t_peak]
        val_trss = data_trss[t_peak]
        
        vmax = max(np.max(np.abs(val_gt)), np.max(np.abs(val_mne)), np.max(np.abs(val_trss)))
        vmin = -vmax
        mask = np.zeros(D, dtype=bool); mask[bad_idx] = True
        mask_params = dict(marker='x', markerfacecolor='black', markeredgecolor='black', linewidth=0, markersize=8)
        
        # Row labels
        title_prefix = f"[{mode.capitalize()} {int(loss*100)}%]"
        
        # Instant Plot Row i
        mne.viz.plot_topomap(val_gt, info, axes=axes_inst[i,0], show=False, vlim=(vmin, vmax), cmap='RdBu_r')
        if i == 0: axes_inst[i,0].set_title('Ground Truth')
        axes_inst[i,0].set_ylabel(title_prefix, size='large', rotation=90)
        
        mne.viz.plot_topomap(val_missing, info, axes=axes_inst[i,1], show=False, vlim=(vmin, vmax), cmap='RdBu_r', mask=mask, mask_params=mask_params)
        if i == 0: axes_inst[i,1].set_title('Señal Dañada')
        
        mne.viz.plot_topomap(val_mne, info, axes=axes_inst[i,2], show=False, vlim=(vmin, vmax), cmap='RdBu_r')
        if i == 0: axes_inst[i,2].set_title('MNE')
        
        mne.viz.plot_topomap(val_trss, info, axes=axes_inst[i,3], show=False, vlim=(vmin, vmax), cmap='RdBu_r')
        if i == 0: axes_inst[i,3].set_title('TRSS (Opt)')
        
        # Error Plot Row i
        rmse_mne = np.sqrt(np.mean((data_clean - data_mne)**2, axis=0)) * 1e6
        rmse_trss = np.sqrt(np.mean((data_clean - data_trss)**2, axis=0)) * 1e6
        max_err = max(np.max(rmse_mne[bad_idx]), np.max(rmse_trss[bad_idx]))
        
        mne.viz.plot_topomap(rmse_mne, info, axes=axes_err[i,0], show=False, vlim=(0, max_err), cmap='Reds', mask=mask, mask_params=dict(marker='o', markerfacecolor='none', markeredgecolor='black', linewidth=0, markersize=8))
        if i == 0: axes_err[i,0].set_title('RMSE MNE')
        axes_err[i,0].set_ylabel(title_prefix, size='large')
        axes_err[i,0].text(0, -0.7, f"Mean Error: {np.mean(rmse_mne[bad_idx]):.2f}uV", ha='center')
        
        mne.viz.plot_topomap(rmse_trss, info, axes=axes_err[i,1], show=False, vlim=(0, max_err), cmap='Reds', mask=mask, mask_params=dict(marker='o', markerfacecolor='none', markeredgecolor='black', linewidth=0, markersize=8))
        if i == 0: axes_err[i,1].set_title('RMSE TRSS')
        axes_err[i,1].text(0, -0.7, f"Mean Error: {np.mean(rmse_trss[bad_idx]):.2f}uV", ha='center')

    fig_inst.suptitle(f'Topografía Instantánea Multicaso - {dataset_name.upper()}', fontsize=20)
    fig_err.suptitle(f'Topomapas RMSE Multicaso - {dataset_name.upper()}', fontsize=20)
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    out_inst = ROOT / 'results_optuna_final' / f'grid_topomap_instant_{dataset_name}.png'
    out_err = ROOT / 'results_optuna_final' / f'grid_topomap_rmse_{dataset_name}.png'
    
    fig_inst.savefig(out_inst, dpi=300, bbox_inches='tight')
    fig_err.savefig(out_err, dpi=300, bbox_inches='tight')
    plt.close('all')

def main():
    datasets = [
        (load_physionet_eegmmidb, 'physionet'),
        (load_bci_competition_iv_2a, 'bci_iv'),
        (load_mne_sample_dataset, 'mne_sample')
    ]
    for loader, name in datasets:
        create_topomaps_multi(loader, name)

if __name__ == '__main__':
    main()
