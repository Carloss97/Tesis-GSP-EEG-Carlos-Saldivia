#!/usr/bin/env python3
"""Add missing `normalization` and `missing_mode` keys to run metadata JSON files.

Usage:
  & "C:\\Users\\sarlo\\anaconda3\\python.exe" "Thesis-Copilot-Toolkit/scripts/fix_run_metadata_keys.py"

This script edits files in-place. It will write a small log at
`Thesis-Copilot-Toolkit/scripts/fix_run_metadata_log.json` with a list of
modified files.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[2]
OUT_LOG = ROOT / 'Thesis-Copilot-Toolkit' / 'scripts' / 'fix_run_metadata_log.json'


def find_run_meta_files() -> List[Path]:
    pats = list(ROOT.rglob('*_run_metadata.json')) + list(ROOT.rglob('*run_metadata.json'))
    seen = set()
    out: List[Path] = []
    for p in pats:
        try:
            rp = p.resolve()
        except Exception:
            continue
        if rp in seen:
            continue
        seen.add(rp)
        out.append(p)
    return out


def main():
    files = find_run_meta_files()
    modified = []
    print(f"Found {len(files)} run metadata files to inspect.")
    for p in files:
        try:
            txt = p.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Failed reading {p}: {e}")
            continue
        try:
            j = json.loads(txt)
        except Exception as e:
            print(f"Invalid JSON in {p}: {e}")
            continue
        changed = False
        if 'normalization' not in j:
            j['normalization'] = None
            changed = True
        if 'missing_mode' not in j:
            j['missing_mode'] = None
            changed = True
        if changed:
            try:
                p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
                modified.append(str(p.relative_to(ROOT)))
            except Exception as e:
                print(f"Failed writing {p}: {e}")
    print(f"Modified {len(modified)} files.")
    try:
        OUT_LOG.write_text(json.dumps({'modified': modified}, ensure_ascii=False, indent=2), encoding='utf-8')
        print('Wrote log to', OUT_LOG)
    except Exception as e:
        print('Failed to write log:', e)

if __name__ == '__main__':
    main()
