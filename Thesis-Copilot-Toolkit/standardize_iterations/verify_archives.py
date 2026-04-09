#!/usr/bin/env python3
"""Verify sample archives created by condense_standardized_results.py.
Writes a compact JSON report to Thesis-Copilot-Toolkit/standardize_iterations/verify_archives_report_20260409_180004.json
"""
import json
import os
import zipfile
import hashlib
import random
import sys
import argparse
from pathlib import Path

ROOT = Path('Thesis-Copilot-Toolkit') / 'standardized_results'
REPORT = Path('Thesis-Copilot-Toolkit') / 'standardize_iterations' / 'condense_standardized_results_apply_report_20260409_180004.json'
OUT = Path('Thesis-Copilot-Toolkit') / 'standardize_iterations' / 'verify_archives_report_20260409_180004.json'
ZIPNAME = 'archived_dup_files_20260409_180004.zip'
MANIFEST = 'archived_dup_files_20260409_180004_manifest.json'


def load_it_list():
    if REPORT.exists():
        try:
            raw = json.loads(REPORT.read_text(encoding='utf-8'))
            its = [s.get('it') for s in raw.get('it_summaries', []) if s.get('it')]
            if its:
                return its
        except Exception:
            pass
    # fallback: scan ROOT for itNNN dirs
    its = []
    if ROOT.exists():
        for p in sorted(ROOT.iterdir()):
            if p.is_dir() and p.name.startswith('it'):
                its.append(p.name)
    return its


def load_manifest(manifest_path: Path):
    try:
        raw = json.loads(manifest_path.read_text(encoding='utf-8'))
    except Exception as e:
        return None, f'manifest_json_error:{e}'
    entries = []
    if isinstance(raw, dict):
        if 'files' in raw and isinstance(raw['files'], list):
            entries = raw['files']
        elif 'entries' in raw and isinstance(raw['entries'], list):
            entries = raw['entries']
        else:
            # possible mapping name -> meta
            if all(isinstance(v, dict) for v in raw.values()):
                for name, meta in raw.items():
                    e = {'name': name}
                    e.update(meta)
                    entries.append(e)
    elif isinstance(raw, list):
        entries = raw

    manifest_map = {}
    for e in entries:
        name = e.get('name') or e.get('filename') or e.get('path') or e.get('file') or e.get('relpath')
        if not name:
            # try find a candidate value
            for k, v in e.items():
                if isinstance(v, str) and ('name' in k.lower() or 'path' in k.lower() or 'file' in k.lower()):
                    name = v
                    break
        if not name:
            continue
        manifest_map[name] = {
            'sha256': (e.get('sha256') or e.get('sha') or e.get('digest') or None),
            'size': (e.get('size_bytes') or e.get('size') or e.get('size_b') or None)
        }
    return manifest_map, None


def check_it(itname: str):
    res = {'it': itname, 'zip_exists': False, 'manifest_exists': False, 'entries_checked': 0, 'matches': 0, 'mismatches': [], 'errors': []}
    itdir = ROOT / itname
    zip_path = itdir / ZIPNAME
    manifest_path = itdir / MANIFEST
    if not zip_path.exists():
        res['errors'].append(f'zip_missing:{zip_path}')
        return res
    res['zip_exists'] = True
    manifest_map = {}
    if manifest_path.exists():
        res['manifest_exists'] = True
        manifest_map, err = load_manifest(manifest_path)
        if err:
            res['errors'].append(err)
            manifest_map = {}
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            for zi in z.infolist():
                name = zi.filename
                if name.endswith('/'):
                    continue
                res['entries_checked'] += 1
                try:
                    with z.open(name) as fh:
                        h = hashlib.sha256()
                        for chunk in iter(lambda: fh.read(8192), b''):
                            h.update(chunk)
                        digest = h.hexdigest()
                        size = zi.file_size
                except Exception as e:
                    res['errors'].append(f'zip_read_error:{name}:{e}')
                    continue
                m = manifest_map.get(name)
                if not m:
                    base = os.path.basename(name)
                    m = manifest_map.get(base)
                if not m:
                    res['mismatches'].append({'file': name, 'reason': 'manifest_missing'})
                    continue
                expected_sha = m.get('sha256')
                expected_size = m.get('size')
                mismatch = False
                detail = {'file': name}
                if expected_sha and expected_sha.lower() != digest.lower():
                    mismatch = True
                    detail['sha_expected'] = expected_sha
                    detail['sha_actual'] = digest
                if expected_size is not None:
                    try:
                        if int(expected_size) != int(size):
                            mismatch = True
                            detail['size_expected'] = int(expected_size)
                            detail['size_actual'] = int(size)
                    except Exception:
                        pass
                if mismatch:
                    res['mismatches'].append(detail)
                else:
                    res['matches'] += 1
    except Exception as e:
        res['errors'].append(f'zip_error:{e}')
    return res


def main():
    its = load_it_list()
    if not its:
        print('No iteraciones encontradas', file=sys.stderr)
        sys.exit(2)
    parser = argparse.ArgumentParser()
    parser.add_argument('--all', action='store_true', help='Verify all its instead of sample')
    parser.add_argument('--sample-size', type=int, default=5, help='number of random its to sample (ignored if --all)')
    args = parser.parse_args()
    if args.all:
        sample = list(its)
    else:
        random.seed(42)
        sample = random.sample(its, min(args.sample_size, len(its)))
    results = []
    for itname in sample:
        r = check_it(itname)
        results.append(r)
    out = {'sample': sample, 'results': results}
    try:
        OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
    except Exception as e:
        print(json.dumps({'error': f'write_report_failed:{e}'}))
        sys.exit(3)
    total_checked = sum(r.get('entries_checked', 0) for r in results)
    total_mismatch = sum(len(r.get('mismatches', [])) for r in results)
    total_errors = sum(len(r.get('errors', [])) for r in results)
    print(json.dumps({'its_checked': len(results), 'total_entries': total_checked, 'total_mismatches': total_mismatch, 'total_errors': total_errors}))

if __name__ == '__main__':
    main()
