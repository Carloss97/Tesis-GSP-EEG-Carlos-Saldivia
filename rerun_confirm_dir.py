"""Re-run failed confirmatory iterations in a specified confirmatory results folder.
Usage:
  .venv\Scripts\python.exe rerun_confirm_dir.py --confirm-dir Thesis-Copilot-Toolkit\results_confirmatory_progressive_2026-04-16_02-57-11
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path('Thesis-Copilot-Toolkit')
BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'

spec = importlib.util.spec_from_file_location('base_mod', str(BASE_SCRIPT))
base_mod = importlib.util.module_from_spec(spec)
loader = spec.loader
sys.modules[spec.name] = base_mod
if loader is None:
    raise RuntimeError('Loader is None')
loader.exec_module(base_mod)


def parse_graph_tag(tag: str):
    if '__' in tag:
        parts = tag.split('__')
        g = parts[0]
        params = {}
        rest = '__'.join(parts[1:])
        for token in rest.split('_'):
            if token.startswith('k') and token[1:].isdigit():
                params['k'] = int(token[1:])
            elif token.startswith('sigma'):
                try:
                    params['sigma'] = float(token.replace('sigma', ''))
                except Exception:
                    pass
        return g, params
    return tag, {}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--confirm-dir', type=str, required=True)
    args = parser.parse_args()

    confirm_dir = Path(args.confirm_dir)
    if not confirm_dir.exists():
        print('Confirm dir not found:', confirm_dir)
        sys.exit(1)

    failed_p = confirm_dir / 'confirm_prog_failed.json'
    completed_p = confirm_dir / 'confirm_prog_completed.json'

    if not failed_p.exists():
        print('No failed file at', failed_p)
        return

    failed = json.loads(failed_p.read_text(encoding='utf-8'))
    completed = json.loads(completed_p.read_text(encoding='utf-8')) if completed_p.exists() else []

    check = base_mod.load_data_availability()
    availability = check.get('availability', {})
    data = check.get('data', {})

    new_failed: List[Dict[str, Any]] = []

    for entry in failed:
        it_name = entry.get('iter')
        print('Re-running', it_name)
        parts = it_name.split('_')
        if len(parts) < 4:
            print('Unexpected iter name format:', it_name)
            new_failed.append(entry)
            continue
        tag = '_'.join(parts[3:])
        meta_p = ROOT / 'results_screening_2000' / f"{tag}_run_metadata.json"
        if not meta_p.exists():
            print('Metadata not found for', tag)
            new_failed.append(entry)
            continue
        try:
            meta = json.loads(meta_p.read_text(encoding='utf-8'))
            ds = meta.get('datasets', [None])[0]
            ds_key = ds if availability.get(ds, {}).get('ok') else None
            if ds_key is None:
                # pick any available
                for k, v in availability.items():
                    if v.get('ok'):
                        ds_key = k
                        break
            if ds_key is None:
                print('No available dataset to run for', tag)
                new_failed.append(entry)
                continue

            graphs = meta.get('graphs', [])
            graph_spec = ('knn', {'k': 3})
            if graphs:
                gname, gparams = parse_graph_tag(str(graphs[0]))
                graph_spec = (gname, gparams)

            mlist = meta.get('missing_ratios', [0.2])
            methods = [meta.get('best_method')] if meta.get('best_method') else None

            it = base_mod.IterDef(
                it_name,
                it_name,
                f'Retry: {tag}',
                'Confirmatory',
                'Retry failed progressive confirm',
                [ds_key],
                mode='base',
                missing_list=mlist,
                seeds=list(range(4)),
                graph_specs=[graph_spec],
                methods=methods,
            )
            base_mod.RESULTS = confirm_dir
            base_mod._run_iteration(it, availability, data, operational_close_profile=False)
            print('Succeeded:', it_name)
            completed.append(it_name)
        except Exception as exc:
            print('Failed again for', it_name, exc)
            traceback.print_exc()
            new_failed.append({'iter': it_name, 'error': str(exc)})

    # write updated files
    confirm_dir.mkdir(parents=True, exist_ok=True)
    (confirm_dir / 'confirm_prog_completed.json').write_text(json.dumps(completed, ensure_ascii=False, indent=2), encoding='utf-8')
    if new_failed:
        (confirm_dir / 'confirm_prog_failed.json').write_text(json.dumps(new_failed, ensure_ascii=False, indent=2), encoding='utf-8')
    else:
        try:
            (confirm_dir / 'confirm_prog_failed.json').unlink()
        except Exception:
            pass

    print('Rerun complete. Completed count:', len(completed), 'Remaining failed:', len(new_failed))


if __name__ == '__main__':
    main()
