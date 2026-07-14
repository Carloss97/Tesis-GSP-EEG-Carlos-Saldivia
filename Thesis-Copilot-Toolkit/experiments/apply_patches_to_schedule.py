#!/usr/bin/env python3
"""
Apply patch operations to an experiments schedule JSON to produce a canonical schedule.

Usage:
  python Thesis-Copilot-Toolkit/experiments/apply_patches_to_schedule.py

Defaults expect to find:
  - Thesis-Copilot-Toolkit/experiments/schedules/it01-it50_schedule_final.json
  - Thesis-Copilot-Toolkit/experiments/patch_operations.json

Output:
  - Thesis-Copilot-Toolkit/experiments/schedules/it01-it50_schedule_final_canonical.json
"""
import json
import argparse
import os
import sys
from datetime import datetime


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(obj, path):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def unique_preserve_order(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def apply_ops(schedule, patches):
    iterations = schedule.get('iterations', [])
    iter_map = {it.get('key'): it for it in iterations}
    modified = set()
    removed_count = 0

    for patch in patches:
        key = patch.get('iteration')
        it = iter_map.get(key)
        if not it:
            print(f"Warning: iteration {key} not found in schedule", file=sys.stderr)
            continue
        for op in patch.get('ops', []):
            typ = op.get('type')
            if typ == 'map_dataset':
                canonical = op.get('canonical')
                variant = op.get('variant')
                if canonical:
                    it['datasets'] = [canonical]
                    if variant:
                        it['dataset_variant'] = variant
                    modified.add(key)
            elif typ == 'map_graph':
                original = op.get('original')
                canonical = op.get('canonical')
                gs = it.get('graph_specs', [])
                changed = False
                for g in gs:
                    if isinstance(g, list) and g and g[0] == original:
                        g[0] = canonical
                        changed = True
                if changed:
                    modified.add(key)
            elif typ == 'map_method':
                original = op.get('original')
                canonical = op.get('canonical')
                methods = it.get('methods', [])
                if original in methods:
                    methods = [canonical if m == original else m for m in methods]
                    it['methods'] = unique_preserve_order(methods)
                    modified.add(key)
            elif typ == 'remove_method':
                original = op.get('original')
                methods = it.get('methods', [])
                new_methods = [m for m in methods if m != original]
                if len(new_methods) != len(methods):
                    removed_count += (len(methods) - len(new_methods))
                    it['methods'] = unique_preserve_order(new_methods)
                    modified.add(key)
            else:
                print(f"Info: operation type '{typ}' not recognized, skipping.", file=sys.stderr)

    return schedule, modified, removed_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--schedule', default='Thesis-Copilot-Toolkit/experiments/schedules/it01-it50_schedule_final.json')
    parser.add_argument('--patch', default='Thesis-Copilot-Toolkit/experiments/patch_operations.json')
    parser.add_argument('--out', default='Thesis-Copilot-Toolkit/experiments/schedules/it01-it50_schedule_final_canonical.json')
    args = parser.parse_args()

    if not os.path.exists(args.schedule):
        print(f"Error: schedule file not found: {args.schedule}", file=sys.stderr)
        sys.exit(2)
    if not os.path.exists(args.patch):
        print(f"Error: patch file not found: {args.patch}", file=sys.stderr)
        sys.exit(2)

    schedule = load_json(args.schedule)
    patch_doc = load_json(args.patch)
    patches = patch_doc.get('patches', [])

    print(f"Applying {len(patches)} patch entries to schedule {args.schedule}...")
    schedule_out, modified, removed_count = apply_ops(schedule, patches)

    schedule_out['generated'] = datetime.utcnow().isoformat() + 'Z'
    save_json(schedule_out, args.out)

    print(f"Patches applied. Iterations modified: {len(modified)}. Methods removed: {removed_count}.")
    print(f"Canonical schedule written to: {args.out}")


if __name__ == '__main__':
    main()
