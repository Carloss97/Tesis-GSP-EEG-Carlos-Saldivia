
# Auto-generated runner from selection rerun_selection_lt5.csv
# Use with caution: this script will call the iteration engine and execute runs.
import importlib.util
from dataclasses import replace
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'

# load base module
spec = importlib.util.spec_from_file_location('run121130', str(BASE_SCRIPT))
mod = importlib.util.module_from_spec(spec)
loader = spec.loader
import sys as _sys
_sys.modules[spec.name] = mod
loader.exec_module(mod)

IterDef = mod.IterDef

_defs = []
_defs.append(IterDef('rerun_0_mne_sample_proxy_knn__k3_directed_tv', 'rerun_0_mne_sample_proxy_knn__k3_directed_tv', 'Rerun combo: mne_sample_proxy knn__k3 directed_tv mr=0.1', 'Rerun', 'Auto-generated rerun', ['mne_sample_proxy'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.1], methods=['directed_tv']))
_defs.append(IterDef('rerun_1_mne_sample_proxy_knn__k3_directed_tv', 'rerun_1_mne_sample_proxy_knn__k3_directed_tv', 'Rerun combo: mne_sample_proxy knn__k3 directed_tv mr=0.2', 'Rerun', 'Auto-generated rerun', ['mne_sample_proxy'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.2], methods=['directed_tv']))
_defs.append(IterDef('rerun_2_synthetic_16ch_kalofolias_graph_time_tikhonov', 'rerun_2_synthetic_16ch_kalofolias_graph_time_tikhonov', 'Rerun combo: synthetic_16ch kalofolias graph_time_tikhonov mr=0.4', 'Rerun', 'Auto-generated rerun', ['synthetic_16ch'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.4], methods=['graph_time_tikhonov']))
_defs.append(IterDef('rerun_3_bci_competition_iv_2a_proxy_kalofolias_heat_diffusion_temporal', 'rerun_3_bci_competition_iv_2a_proxy_kalofolias_heat_diffusion_temporal', 'Rerun combo: bci_competition_iv_2a_proxy kalofolias heat_diffusion_temporal mr=0.1', 'Rerun', 'Auto-generated rerun', ['bci_competition_iv_2a_proxy'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.1], methods=['heat_diffusion_temporal']))
_defs.append(IterDef('rerun_4_bci_competition_iv_2a_proxy_kalofolias_heat_diffusion_temporal', 'rerun_4_bci_competition_iv_2a_proxy_kalofolias_heat_diffusion_temporal', 'Rerun combo: bci_competition_iv_2a_proxy kalofolias heat_diffusion_temporal mr=0.3', 'Rerun', 'Auto-generated rerun', ['bci_competition_iv_2a_proxy'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.3], methods=['heat_diffusion_temporal']))
_defs.append(IterDef('rerun_5_bci_competition_iv_2a_proxy_kalofolias_heat_diffusion_temporal', 'rerun_5_bci_competition_iv_2a_proxy_kalofolias_heat_diffusion_temporal', 'Rerun combo: bci_competition_iv_2a_proxy kalofolias heat_diffusion_temporal mr=0.4', 'Rerun', 'Auto-generated rerun', ['bci_competition_iv_2a_proxy'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.4], methods=['heat_diffusion_temporal']))
_defs.append(IterDef('rerun_6_mne_sample_proxy_kalofolias_heat_diffusion_temporal', 'rerun_6_mne_sample_proxy_kalofolias_heat_diffusion_temporal', 'Rerun combo: mne_sample_proxy kalofolias heat_diffusion_temporal mr=0.1', 'Rerun', 'Auto-generated rerun', ['mne_sample_proxy'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.1], methods=['heat_diffusion_temporal']))
_defs.append(IterDef('rerun_7_mne_sample_proxy_kalofolias_heat_diffusion_temporal', 'rerun_7_mne_sample_proxy_kalofolias_heat_diffusion_temporal', 'Rerun combo: mne_sample_proxy kalofolias heat_diffusion_temporal mr=0.2', 'Rerun', 'Auto-generated rerun', ['mne_sample_proxy'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.2], methods=['heat_diffusion_temporal']))
_defs.append(IterDef('rerun_8_mne_sample_proxy_kalofolias_heat_diffusion_temporal', 'rerun_8_mne_sample_proxy_kalofolias_heat_diffusion_temporal', 'Rerun combo: mne_sample_proxy kalofolias heat_diffusion_temporal mr=0.3', 'Rerun', 'Auto-generated rerun', ['mne_sample_proxy'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.3], methods=['heat_diffusion_temporal']))
_defs.append(IterDef('rerun_9_physionet_eegmmidb_gaussian_rbfi_tps', 'rerun_9_physionet_eegmmidb_gaussian_rbfi_tps', 'Rerun combo: physionet_eegmmidb gaussian rbfi_tps mr=0.4', 'Rerun', 'Auto-generated rerun', ['physionet_eegmmidb'], seeds=list(range(6)), graph_specs=[('gaussian', {})], missing_list=[0.4], methods=['rbfi_tps']))
_defs.append(IterDef('rerun_10_mne_sample_proxy_gaussian__sigma1_temporal_laplacian', 'rerun_10_mne_sample_proxy_gaussian__sigma1_temporal_laplacian', 'Rerun combo: mne_sample_proxy gaussian__sigma1 temporal_laplacian mr=0.1', 'Rerun', 'Auto-generated rerun', ['mne_sample_proxy'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.1], methods=['temporal_laplacian']))
_defs.append(IterDef('rerun_11_mne_sample_proxy_gaussian__sigma1_temporal_laplacian', 'rerun_11_mne_sample_proxy_gaussian__sigma1_temporal_laplacian', 'Rerun combo: mne_sample_proxy gaussian__sigma1 temporal_laplacian mr=0.3', 'Rerun', 'Auto-generated rerun', ['mne_sample_proxy'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.3], methods=['temporal_laplacian']))
_defs.append(IterDef('rerun_12_bci_competition_iv_2a_proxy_kalofolias_trss', 'rerun_12_bci_competition_iv_2a_proxy_kalofolias_trss', 'Rerun combo: bci_competition_iv_2a_proxy kalofolias trss mr=0.2', 'Rerun', 'Auto-generated rerun', ['bci_competition_iv_2a_proxy'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.2], methods=['trss']))
_defs.append(IterDef('rerun_13_bci_competition_proxy_kalofolias_trss', 'rerun_13_bci_competition_proxy_kalofolias_trss', 'Rerun combo: bci_competition_proxy kalofolias trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['bci_competition_proxy'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_14_bci_iv2a_real_s1_gaussian__sigma1.0_trss', 'rerun_14_bci_iv2a_real_s1_gaussian__sigma1.0_trss', 'Rerun combo: bci_iv2a_real_s1 gaussian__sigma1.0 trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['bci_iv2a_real_s1'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_15_bci_iv2a_real_s1_knn__k3_trss', 'rerun_15_bci_iv2a_real_s1_knn__k3_trss', 'Rerun combo: bci_iv2a_real_s1 knn__k3 trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['bci_iv2a_real_s1'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_16_bci_iv2a_real_s2_gaussian__sigma1.0_trss', 'rerun_16_bci_iv2a_real_s2_gaussian__sigma1.0_trss', 'Rerun combo: bci_iv2a_real_s2 gaussian__sigma1.0 trss mr=0.1', 'Rerun', 'Auto-generated rerun', ['bci_iv2a_real_s2'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.1], methods=['trss']))
_defs.append(IterDef('rerun_17_bci_iv2a_real_s2_gaussian__sigma1.0_trss', 'rerun_17_bci_iv2a_real_s2_gaussian__sigma1.0_trss', 'Rerun combo: bci_iv2a_real_s2 gaussian__sigma1.0 trss mr=0.3', 'Rerun', 'Auto-generated rerun', ['bci_iv2a_real_s2'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.3], methods=['trss']))
_defs.append(IterDef('rerun_18_bci_iv2a_real_s2_gaussian__sigma1.0_trss', 'rerun_18_bci_iv2a_real_s2_gaussian__sigma1.0_trss', 'Rerun combo: bci_iv2a_real_s2 gaussian__sigma1.0 trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['bci_iv2a_real_s2'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_19_bci_iv2a_real_s2_knn__k3_trss', 'rerun_19_bci_iv2a_real_s2_knn__k3_trss', 'Rerun combo: bci_iv2a_real_s2 knn__k3 trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['bci_iv2a_real_s2'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_20_iris_graph_signal_gaussian__sigma1.0_trss', 'rerun_20_iris_graph_signal_gaussian__sigma1.0_trss', 'Rerun combo: iris_graph_signal gaussian__sigma1.0 trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['iris_graph_signal'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_21_iris_graph_signal_knn__k3_trss', 'rerun_21_iris_graph_signal_knn__k3_trss', 'Rerun combo: iris_graph_signal knn__k3 trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['iris_graph_signal'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_22_iv100hz_mat_knn__k3_trss', 'rerun_22_iv100hz_mat_knn__k3_trss', 'Rerun combo: iv100hz_mat knn__k3 trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['iv100hz_mat'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_23_mne_sample_proxy_kalofolias_trss', 'rerun_23_mne_sample_proxy_kalofolias_trss', 'Rerun combo: mne_sample_proxy kalofolias trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['mne_sample_proxy'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_24_physionet_eegmmidb_aew_trss', 'rerun_24_physionet_eegmmidb_aew_trss', 'Rerun combo: physionet_eegmmidb aew trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['physionet_eegmmidb'], seeds=list(range(6)), graph_specs=[('aew', {})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_25_physionet_eegmmidb_gaussian_trss', 'rerun_25_physionet_eegmmidb_gaussian_trss', 'Rerun combo: physionet_eegmmidb gaussian trss mr=0.1', 'Rerun', 'Auto-generated rerun', ['physionet_eegmmidb'], seeds=list(range(6)), graph_specs=[('gaussian', {})], missing_list=[0.1], methods=['trss']))
_defs.append(IterDef('rerun_26_physionet_eegmmidb_knng_trss', 'rerun_26_physionet_eegmmidb_knng_trss', 'Rerun combo: physionet_eegmmidb knng trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['physionet_eegmmidb'], seeds=list(range(6)), graph_specs=[('knng', {})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_27_physionet_eegmmidb_nnk_trss', 'rerun_27_physionet_eegmmidb_nnk_trss', 'Rerun combo: physionet_eegmmidb nnk trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['physionet_eegmmidb'], seeds=list(range(6)), graph_specs=[('nnk', {})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_28_physionet_eegmmidb_vknng_trss', 'rerun_28_physionet_eegmmidb_vknng_trss', 'Rerun combo: physionet_eegmmidb vknng trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['physionet_eegmmidb'], seeds=list(range(6)), graph_specs=[('vknng', {})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_29_physionet_eegmmidb_real_gaussian__sigma1.0_trss', 'rerun_29_physionet_eegmmidb_real_gaussian__sigma1.0_trss', 'Rerun combo: physionet_eegmmidb_real gaussian__sigma1.0 trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['physionet_eegmmidb_real'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_30_physionet_eegmmidb_real_knn__k3_trss', 'rerun_30_physionet_eegmmidb_real_knn__k3_trss', 'Rerun combo: physionet_eegmmidb_real knn__k3 trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['physionet_eegmmidb_real'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_31_synthetic_32ch_kalofolias_trss', 'rerun_31_synthetic_32ch_kalofolias_trss', 'Rerun combo: synthetic_32ch kalofolias trss mr=0.1', 'Rerun', 'Auto-generated rerun', ['synthetic_32ch'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.1], methods=['trss']))
_defs.append(IterDef('rerun_32_synthetic_32ch_kalofolias_trss', 'rerun_32_synthetic_32ch_kalofolias_trss', 'Rerun combo: synthetic_32ch kalofolias trss mr=0.2', 'Rerun', 'Auto-generated rerun', ['synthetic_32ch'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.2], methods=['trss']))
_defs.append(IterDef('rerun_33_synthetic_32ch_kalofolias_trss', 'rerun_33_synthetic_32ch_kalofolias_trss', 'Rerun combo: synthetic_32ch kalofolias trss mr=0.3', 'Rerun', 'Auto-generated rerun', ['synthetic_32ch'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.3], methods=['trss']))
_defs.append(IterDef('rerun_34_synthetic_32ch_kalofolias_trss', 'rerun_34_synthetic_32ch_kalofolias_trss', 'Rerun combo: synthetic_32ch kalofolias trss mr=0.4', 'Rerun', 'Auto-generated rerun', ['synthetic_32ch'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.4], methods=['trss']))
_defs.append(IterDef('rerun_35_iv100hz_mat_gaussian__sigma1.0_tv', 'rerun_35_iv100hz_mat_gaussian__sigma1.0_tv', 'Rerun combo: iv100hz_mat gaussian__sigma1.0 tv mr=0.4', 'Rerun', 'Auto-generated rerun', ['iv100hz_mat'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.4], methods=['tv']))
_defs.append(IterDef('rerun_36_mne_sample_proxy_gaussian__sigma1_tv', 'rerun_36_mne_sample_proxy_gaussian__sigma1_tv', 'Rerun combo: mne_sample_proxy gaussian__sigma1 tv mr=0.2', 'Rerun', 'Auto-generated rerun', ['mne_sample_proxy'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.2], methods=['tv']))
_defs.append(IterDef('rerun_37_movielens_graph_signal_gaussian__sigma1.0_tv', 'rerun_37_movielens_graph_signal_gaussian__sigma1.0_tv', 'Rerun combo: movielens_graph_signal gaussian__sigma1.0 tv mr=0.4', 'Rerun', 'Auto-generated rerun', ['movielens_graph_signal'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.4], methods=['tv']))
_defs.append(IterDef('rerun_38_movielens_graph_signal_knn__k3_tv', 'rerun_38_movielens_graph_signal_knn__k3_tv', 'Rerun combo: movielens_graph_signal knn__k3 tv mr=0.4', 'Rerun', 'Auto-generated rerun', ['movielens_graph_signal'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.4], methods=['tv']))

def main():
    keys = [d.key for d in _defs]
    parser = mod.argparse.ArgumentParser(description='Run selected reruns')
    parser.add_argument('--tags', nargs='+', default=keys, choices=keys, help='Subset to run')
    parser.add_argument('--light-profile', action='store_true')
    parser.add_argument('--stop-on-error', action='store_true')
    args = parser.parse_args()

    failed = []
    completed = []
    availability = mod.load_data_availability()['availability']
    data = mod.load_data_availability()['data']

    for k in args.tags:
        it = next((d for d in _defs if d.key == k), None)
        if it is None:
            print('Unknown tag', k)
            continue
        try:
            if args.light_profile:
                it = replace(it, seeds=[0,1])
            mod._run_iteration(it, availability, data, operational_close_profile=False)
            completed.append(k)
            print('[OK]', k)
        except Exception as exc:
            failed.append({'iteration': k, 'error': str(exc)})
            print('[SKIPPED]', k, exc)
            if args.stop_on_error:
                raise

    print('Completed:', completed)
    if failed:
        (mod.RESULTS / 'rerun_selected_skipped.json').write_text(mod.json.dumps(failed, ensure_ascii=False, indent=2), encoding='utf-8')

if __name__ == '__main__':
    main()
