#!/usr/bin/env python3
"""
Dry-run (and later apply) deep cleanup for Thesis-Copilot-Toolkit/standardized_results.
- Detects repeated/duplicated path components (e.g., repeated "figures" or repeated "it001_it001_...")
- Proposes normalized target paths by collapsing consecutive duplicates
- Writes a JSON report with proposed moves (does not move files unless --apply is used)
"""

import argparse
import json
from pathlib import Path
import sys


def compress_tokens(component: str) -> str:
    parts = component.split("_")
    out = []
    prev = None
    for p in parts:
        if p == prev:
            continue
        out.append(p)
        prev = p
    return "_".join(out)


def normalize_relpath(rel: Path) -> Path:
    parts = rel.parts
    new_parts = []
    prev_part = None
    for part in parts:
        # compress consecutive identical directory names
        if part == prev_part:
            continue
        comp = compress_tokens(part)
        # if normalizing internal tokens makes it equal to previous part, skip
        if comp == prev_part:
            prev_part = comp
            continue
        new_parts.append(comp)
        prev_part = comp
    return Path(*new_parts) if new_parts else Path('.')


def collect_moves(root: Path):
    moves = []
    seen_targets = {}
    conflicts = []
    total_files = 0
    for p in root.rglob('*'):
        if not p.is_file():
            continue
        total_files += 1
        rel = p.relative_to(root)
        normalized = normalize_relpath(rel)
        target = (root / normalized)
        # normalize path strings for comparison
        src_str = str(p)
        tgt_str = str(target)
        if src_str == tgt_str:
            continue
        # detect conflicts (multiple sources -> same target)
        if tgt_str in seen_targets and seen_targets[tgt_str] != src_str:
            conflicts.append({"from": src_str, "to": tgt_str, "other": seen_targets[tgt_str]})
        else:
            seen_targets[tgt_str] = src_str
            moves.append({"from": src_str, "to": tgt_str})
    unique_target_dirs = set([str(Path(m['to']).parent) for m in moves])
    return {
        "root": str(root),
        "total_files": total_files,
        "proposed_moves": len(moves),
        "unique_target_dirs": len(unique_target_dirs),
        "conflicts": len(conflicts),
        "sample_moves": moves[:200],
        "sample_conflicts": conflicts[:20]
    }, moves, conflicts


def apply_moves(moves, dry_run=False):
    applied = []
    skipped = []
    for m in moves:
        src = Path(m['from'])
        tgt = Path(m['to'])
        parent = tgt.parent
        try:
            parent.mkdir(parents=True, exist_ok=True)
            if not dry_run:
                if tgt.exists():
                    # avoid overwriting: create a unique name
                    base = tgt.stem
                    suf = tgt.suffix
                    i = 1
                    while True:
                        candidate = parent / f"{base}__dup{i}{suf}"
                        if not candidate.exists():
                            tgt = candidate
                            break
                        i += 1
                src.replace(tgt)
            applied.append({"from": str(src), "to": str(tgt)})
        except Exception as e:
            skipped.append({"from": str(src), "to": str(tgt), "error": str(e)})
    return applied, skipped


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default='Thesis-Copilot-Toolkit/standardized_results')
    parser.add_argument('--report', default='Thesis-Copilot-Toolkit/standardize_iterations/standardized_results_deep_cleanup_report.json')
    parser.add_argument('--dry-run', action='store_true', default=False)
    parser.add_argument('--apply', action='store_true', default=False)
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        print(json.dumps({"error": "root_not_found", "root": str(root)}))
        sys.exit(1)

    report, moves, conflicts = collect_moves(root)
    report['report_path'] = str(Path(args.report))

    if args.apply:
        applied, skipped = apply_moves(moves, dry_run=not args.apply)
        report['applied_count'] = len(applied)
        report['skipped_count'] = len(skipped)
        report['applied_sample'] = applied[:100]
        report['skipped_sample'] = skipped[:20]

    # write report
    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open('w', encoding='utf-8') as fh:
        json.dump(report, fh, indent=2, ensure_ascii=False)

    print(json.dumps(report, ensure_ascii=False))

if __name__ == '__main__':
    main()
