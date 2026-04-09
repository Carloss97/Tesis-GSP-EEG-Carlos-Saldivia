#!/usr/bin/env python3
"""Cleanup helper

Actions performed:
- Consolidate nested `figures` and `tables` folders under each tag in
  `Thesis-Copilot-Toolkit/standardized_results/` into a single top-level
  `figures` (or `tables`) directory per tag, moving files and resolving name
  collisions.
- Archive `Thesis-Copilot-Toolkit/standardize_iterations/rerun_logs` into
  `Thesis-Copilot-Toolkit/standardize_iterations/archived_rerun_logs.tar.gz`
  and remove the original `rerun_logs` folder.
- Remove empty directories left behind.

This script is conservative: it moves files into canonical folders and
archives logs rather than permanently deleting them. A JSON report is written
to `cleanup_report.json`.
"""
from __future__ import annotations

import json
import shutil
import tarfile
from pathlib import Path
from datetime import datetime
import sys
import os


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
SR_DIR = REPO_ROOT / 'Thesis-Copilot-Toolkit' / 'standardized_results'
RERUN_LOGS = HERE / 'rerun_logs'
ARCHIVE_TAR = HERE / 'archived_rerun_logs.tar.gz'
REPORT_OUT = HERE / 'cleanup_report.json'


def unique_destination(dst: Path) -> Path:
    if not dst.exists():
        return dst
    stem = dst.stem
    suffix = dst.suffix
    parent = dst.parent
    i = 1
    while True:
        candidate = parent / f"{stem}_dup{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def move_files_from_nested(tag_dir: Path, name: str, report: dict):
    # Consolidate directories named `name` (e.g., 'figures', 'tables') under tag_dir
    target = tag_dir / name
    moved = 0
    if not target.exists():
        target.mkdir(parents=True, exist_ok=True)

    # Find all nested dirs named `name` except the top-level one
    for d in list(tag_dir.rglob(name)):
        try:
            if d.samefile(target):
                continue
        except Exception:
            # On some OSes samefile may fail for non-existing; ignore
            if d == target:
                continue

        # Move files from d into target preserving subfolders
        for f in d.rglob('*'):
            if f.is_file():
                try:
                    rel = f.relative_to(d)
                except Exception:
                    rel = f.name
                dst_dir = target / rel.parent
                dst_dir.mkdir(parents=True, exist_ok=True)
                dst = dst_dir / rel.name
                if dst.exists():
                    dst = unique_destination(dst)
                shutil.move(str(f), str(dst))
                report['moved_files'].append({'from': str(f), 'to': str(dst)})
                moved += 1

    report['tags_processed'].append({'tag': tag_dir.name, f'{name}_moved': moved})


def remove_empty_dirs(base: Path, report: dict):
    removed = 0
    # Walk from deepest to shallowest
    for d in sorted([p for p in base.rglob('*') if p.is_dir()], key=lambda p: -len(str(p))):
        try:
            if not any(d.iterdir()):
                d.rmdir()
                removed += 1
        except Exception:
            continue
    report['empty_dirs_removed'] = removed


def archive_and_remove_rerun_logs(report: dict):
    if not RERUN_LOGS.exists():
        report['rerun_logs_archived'] = False
        return

    try:
        with tarfile.open(ARCHIVE_TAR, 'w:gz') as tf:
            tf.add(RERUN_LOGS, arcname='rerun_logs')
        # After successful archive, remove the original folder
        shutil.rmtree(RERUN_LOGS)
        report['rerun_logs_archived'] = str(ARCHIVE_TAR)
    except Exception as e:
        report.setdefault('errors', []).append(f'archive_error: {e}')
        report['rerun_logs_archived'] = False


def main():
    report = {
        'run_at': datetime.utcnow().isoformat() + 'Z',
        'moved_files': [],
        'tags_processed': [],
        'empty_dirs_removed': 0,
        'rerun_logs_archived': False,
        'errors': [],
    }

    if not SR_DIR.exists():
        print('No standardized_results directory found at', SR_DIR)
        report['errors'].append('standardized_results_missing')
        with open(REPORT_OUT, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        return

    # Process each tag directory
    tags = [p for p in SR_DIR.iterdir() if p.is_dir()]
    for tag in tags:
        try:
            move_files_from_nested(tag, 'figures', report)
            move_files_from_nested(tag, 'tables', report)
        except Exception as e:
            report.setdefault('errors', []).append(f'{tag.name}_process_error: {e}')

        # Remove empty directories within the tag
        try:
            remove_empty_dirs(tag, report)
        except Exception as e:
            report.setdefault('errors', []).append(f'{tag.name}_cleanup_error: {e}')

    # Archive rerun_logs
    try:
        archive_and_remove_rerun_logs(report)
    except Exception as e:
        report.setdefault('errors', []).append(f'archive_top_error: {e}')

    # Final pass: remove any empty dirs under standardized_results root
    try:
        remove_empty_dirs(SR_DIR, report)
    except Exception as e:
        report.setdefault('errors', []).append(f'final_cleanup_error: {e}')

    # Write report
    try:
        with open(REPORT_OUT, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print('Cleanup report written to', REPORT_OUT)
    except Exception as e:
        print('Failed to write report:', e)


if __name__ == '__main__':
    main()
