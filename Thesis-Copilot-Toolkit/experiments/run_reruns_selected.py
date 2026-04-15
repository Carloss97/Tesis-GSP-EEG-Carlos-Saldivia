# Auto-generated runner from selection rerun_selection_lt20.csv
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
_defs.append(IterDef('rerun_0_bci_competition_iv_2a_proxy_gaussian__sigma1_directed_tv', 'rerun_0_bci_competition_iv_2a_proxy_gaussian__sigma1_directed_tv', 'Rerun combo: bci_competition_iv_2a_proxy gaussian__sigma1 directed_tv mr=0.1', 'Rerun', 'Auto-generated rerun', ['bci_competition_iv_2a_proxy'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.1], methods=['directed_tv']))
_defs.append(IterDef('rerun_1_bci_competition_iv_2a_proxy_gaussian__sigma1_directed_tv', 'rerun_1_bci_competition_iv_2a_proxy_gaussian__sigma1_directed_tv', 'Rerun combo: bci_competition_iv_2a_proxy gaussian__sigma1 directed_tv mr=0.3', 'Rerun', 'Auto-generated rerun', ['bci_competition_iv_2a_proxy'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.3], methods=['directed_tv']))
_defs.append(IterDef('rerun_2_bci_competition_iv_2a_proxy_knn__k3_directed_tv', 'rerun_2_bci_competition_iv_2a_proxy_knn__k3_directed_tv', 'Rerun combo: bci_competition_iv_2a_proxy knn__k3 directed_tv mr=0.1', 'Rerun', 'Auto-generated rerun', ['bci_competition_iv_2a_proxy'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.1], methods=['directed_tv']))
_defs.append(IterDef('rerun_3_mne_sample_knn__k3_directed_tv', 'rerun_3_mne_sample_knn__k3_directed_tv', 'Rerun combo: mne_sample knn__k3 directed_tv mr=0.1', 'Rerun', 'Auto-generated rerun', ['mne_sample'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.1], methods=['directed_tv']))
_defs.append(IterDef('rerun_4_mne_sample_knn__k3_directed_tv', 'rerun_4_mne_sample_knn__k3_directed_tv', 'Rerun combo: mne_sample knn__k3 directed_tv mr=0.2', 'Rerun', 'Auto-generated rerun', ['mne_sample'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.2], methods=['directed_tv']))
_defs.append(IterDef('rerun_5_mne_sample_knn__k3_directed_tv', 'rerun_5_mne_sample_knn__k3_directed_tv', 'Rerun combo: mne_sample knn__k3 directed_tv mr=0.4', 'Rerun', 'Auto-generated rerun', ['mne_sample'], seeds=list(range(6)), graph_specs=[('knn', {'k': 3})], missing_list=[0.4], methods=['directed_tv']))
_defs.append(IterDef('rerun_6_synthetic_alpha_gaussian__sigma1_directed_tv', 'rerun_6_synthetic_alpha_gaussian__sigma1_directed_tv', 'Rerun combo: synthetic_alpha gaussian__sigma1 directed_tv mr=0.3', 'Rerun', 'Auto-generated rerun', ['synthetic_alpha'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.3], methods=['directed_tv']))
_defs.append(IterDef('rerun_7_synthetic_alpha_kalofolias_directed_tv', 'rerun_7_synthetic_alpha_kalofolias_directed_tv', 'Rerun combo: synthetic_alpha kalofolias directed_tv mr=0.3', 'Rerun', 'Auto-generated rerun', ['synthetic_alpha'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.3], methods=['directed_tv']))
_defs.append(IterDef('rerun_8_synthetic_alpha_knn__k5_directed_tv', 'rerun_8_synthetic_alpha_knn__k5_directed_tv', 'Rerun combo: synthetic_alpha knn__k5 directed_tv mr=0.3', 'Rerun', 'Auto-generated rerun', ['synthetic_alpha'], seeds=list(range(6)), graph_specs=[('knn', {'k': 5})], missing_list=[0.3], methods=['directed_tv']))
_defs.append(IterDef('rerun_9_synthetic_alpha_knng__k4_sigma1_directed_tv', 'rerun_9_synthetic_alpha_knng__k4_sigma1_directed_tv', 'Rerun combo: synthetic_alpha knng__k4_sigma1 directed_tv mr=0.3', 'Rerun', 'Auto-generated rerun', ['synthetic_alpha'], seeds=list(range(6)), graph_specs=[('knng', {'k': 4, 'sigma': 1.0})], missing_list=[0.3], methods=['directed_tv']))
_defs.append(IterDef('rerun_10_synthetic_alpha_vknng__alpha1_k4_k_max8_k_min2_directed_tv', 'rerun_10_synthetic_alpha_vknng__alpha1_k4_k_max8_k_min2_directed_tv', 'Rerun combo: synthetic_alpha vknng__alpha1_k4_k_max8_k_min2 directed_tv mr=0.3', 'Rerun', 'Auto-generated rerun', ['synthetic_alpha'], seeds=list(range(6)), graph_specs=[('vknng', {'k': 4})], missing_list=[0.3], methods=['directed_tv']))
_defs.append(IterDef('rerun_11_synthetic_beta_aew__k4_sigma_corr0_5_sigma_dist1_directed_tv', 'rerun_11_synthetic_beta_aew__k4_sigma_corr0_5_sigma_dist1_directed_tv', 'Rerun combo: synthetic_beta aew__k4_sigma_corr0_5_sigma_dist1 directed_tv mr=0.4', 'Rerun', 'Auto-generated rerun', ['synthetic_beta'], seeds=list(range(6)), graph_specs=[('aew', {'k': 4})], missing_list=[0.4], methods=['directed_tv']))
_defs.append(IterDef('rerun_12_synthetic_beta_gaussian__sigma1_directed_tv', 'rerun_12_synthetic_beta_gaussian__sigma1_directed_tv', 'Rerun combo: synthetic_beta gaussian__sigma1 directed_tv mr=0.3', 'Rerun', 'Auto-generated rerun', ['synthetic_beta'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.3], methods=['directed_tv']))
_defs.append(IterDef('rerun_13_synthetic_beta_gaussian__sigma1_directed_tv', 'rerun_13_synthetic_beta_gaussian__sigma1_directed_tv', 'Rerun combo: synthetic_beta gaussian__sigma1 directed_tv mr=0.4', 'Rerun', 'Auto-generated rerun', ['synthetic_beta'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.4], methods=['directed_tv']))
_defs.append(IterDef('rerun_14_synthetic_beta_kalofolias_directed_tv', 'rerun_14_synthetic_beta_kalofolias_directed_tv', 'Rerun combo: synthetic_beta kalofolias directed_tv mr=0.3', 'Rerun', 'Auto-generated rerun', ['synthetic_beta'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.3], methods=['directed_tv']))
_defs.append(IterDef('rerun_15_synthetic_beta_kalofolias_directed_tv', 'rerun_15_synthetic_beta_kalofolias_directed_tv', 'Rerun combo: synthetic_beta kalofolias directed_tv mr=0.4', 'Rerun', 'Auto-generated rerun', ['synthetic_beta'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.4], methods=['directed_tv']))
_defs.append(IterDef('rerun_16_synthetic_beta_knn__k5_directed_tv', 'rerun_16_synthetic_beta_knn__k5_directed_tv', 'Rerun combo: synthetic_beta knn__k5 directed_tv mr=0.4', 'Rerun', 'Auto-generated rerun', ['synthetic_beta'], seeds=list(range(6)), graph_specs=[('knn', {'k': 5})], missing_list=[0.4], methods=['directed_tv']))
_defs.append(IterDef('rerun_17_synthetic_beta_vknng__alpha1_k4_k_max8_k_min2_directed_tv', 'rerun_17_synthetic_beta_vknng__alpha1_k4_k_max8_k_min2_directed_tv', 'Rerun combo: synthetic_beta vknng__alpha1_k4_k_max8_k_min2 directed_tv mr=0.4', 'Rerun', 'Auto-generated rerun', ['synthetic_beta'], seeds=list(range(6)), graph_specs=[('vknng', {'k': 4})], missing_list=[0.4], methods=['directed_tv']))
_defs.append(IterDef('rerun_18_synthetic_broad_gaussian__sigma1_directed_tv', 'rerun_18_synthetic_broad_gaussian__sigma1_directed_tv', 'Rerun combo: synthetic_broad gaussian__sigma1 directed_tv mr=0.1', 'Rerun', 'Auto-generated rerun', ['synthetic_broad'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.1], methods=['directed_tv']))
_defs.append(IterDef('rerun_19_synthetic_broad_gaussian__sigma1_directed_tv', 'rerun_19_synthetic_broad_gaussian__sigma1_directed_tv', 'Rerun combo: synthetic_broad gaussian__sigma1 directed_tv mr=0.2', 'Rerun', 'Auto-generated rerun', ['synthetic_broad'], seeds=list(range(6)), graph_specs=[('gaussian', {'sigma': 1.0})], missing_list=[0.2], methods=['directed_tv']))
_defs.append(IterDef('rerun_20_synthetic_broad_kalofolias_directed_tv', 'rerun_20_synthetic_broad_kalofolias_directed_tv', 'Rerun combo: synthetic_broad kalofolias directed_tv mr=0.1', 'Rerun', 'Auto-generated rerun', ['synthetic_broad'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.1], methods=['directed_tv']))
_defs.append(IterDef('rerun_21_synthetic_broad_kalofolias_directed_tv', 'rerun_21_synthetic_broad_kalofolias_directed_tv', 'Rerun combo: synthetic_broad kalofolias directed_tv mr=0.2', 'Rerun', 'Auto-generated rerun', ['synthetic_broad'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.2], methods=['directed_tv']))
_defs.append(IterDef('rerun_22_synthetic_broad_knn__k5_directed_tv', 'rerun_22_synthetic_broad_knn__k5_directed_tv', 'Rerun combo: synthetic_broad knn__k5 directed_tv mr=0.1', 'Rerun', 'Auto-generated rerun', ['synthetic_broad'], seeds=list(range(6)), graph_specs=[('knn', {'k': 5})], missing_list=[0.1], methods=['directed_tv']))
_defs.append(IterDef('rerun_23_synthetic_broad_knn__k5_directed_tv', 'rerun_23_synthetic_broad_knn__k5_directed_tv', 'Rerun combo: synthetic_broad knn__k5 directed_tv mr=0.2', 'Rerun', 'Auto-generated rerun', ['synthetic_broad'], seeds=list(range(6)), graph_specs=[('knn', {'k': 5})], missing_list=[0.2], methods=['directed_tv']))
_defs.append(IterDef('rerun_24_synthetic_broad_knn__k5_directed_tv', 'rerun_24_synthetic_broad_knn__k5_directed_tv', 'Rerun combo: synthetic_broad knn__k5 directed_tv mr=0.3', 'Rerun', 'Auto-generated rerun', ['synthetic_broad'], seeds=list(range(6)), graph_specs=[('knn', {'k': 5})], missing_list=[0.3], methods=['directed_tv']))
_defs.append(IterDef('rerun_25_synthetic_broad_knng__k4_sigma1_directed_tv', 'rerun_25_synthetic_broad_knng__k4_sigma1_directed_tv', 'Rerun combo: synthetic_broad knng__k4_sigma1 directed_tv mr=0.1', 'Rerun', 'Auto-generated rerun', ['synthetic_broad'], seeds=list(range(6)), graph_specs=[('knng', {'k': 4, 'sigma': 1.0})], missing_list=[0.1], methods=['directed_tv']))
_defs.append(IterDef('rerun_26_synthetic_broad_vknng__alpha1_k4_k_max8_k_min2_directed_tv', 'rerun_26_synthetic_broad_vknng__alpha1_k4_k_max8_k_min2_directed_tv', 'Rerun combo: synthetic_broad vknng__alpha1_k4_k_max8_k_min2 directed_tv mr=0.1', 'Rerun', 'Auto-generated rerun', ['synthetic_broad'], seeds=list(range(6)), graph_specs=[('vknng', {'k': 4})], missing_list=[0.1], methods=['directed_tv']))
_defs.append(IterDef('rerun_27_synthetic_16ch_kalofolias_graph_time_tikhonov', 'rerun_27_synthetic_16ch_kalofolias_graph_time_tikhonov', 'Rerun combo: synthetic_16ch kalofolias graph_time_tikhonov mr=0.4', 'Rerun', 'Auto-generated rerun', ['synthetic_16ch'], seeds=list(range(6)), graph_specs=[('kalofolias', {})], missing_list=[0.4], methods=['graph_time_tikhonov']))

# (rest of the file is unchanged; all occurrences of 'mne_sample_proxy' were replaced with 'mne_sample')

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
