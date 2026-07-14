#!/usr/bin/env python3
"""Lightweight docs linter + run-metadata validator.
Scans repository for Markdown file links (local) and validates that
all run metadata JSON files contain `normalization` and `missing_mode` keys.
Writes a JSON report to `Thesis-Copilot-Toolkit/scripts/verify_report.json`.
"""
from __future__ import annotations
import json
import re
from pathlib import Path
from typing import List, Dict

ROOT = Path(__file__).resolve().parents[2]
MD_EXCLUDE = {'.git', 'node_modules'}
IGNORE_SUFFIXES = {'.zip', '.tar', '.gz', '.7z', '.exe', '.dll', '.bin'}

link_re = re.compile(r"\[.*?\]\(([^)]+)\)")
image_re = re.compile(r"!\[.*?\]\(([^)]+)\)")


def is_ignored(path: Path) -> bool:
    s = str(path)
    for ex in MD_EXCLUDE:
        if f"/{ex}/" in s.replace('\\\\', '/'):
            return True
    if path.suffix.lower() in IGNORE_SUFFIXES:
        return True
    return False


def find_markdown_files() -> List[Path]:
    out = []
    for p in ROOT.rglob('*.md'):
        if is_ignored(p):
            continue
        out.append(p)
    return out


def check_link(md: Path, target: str) -> bool:
    # skip http(s) and mailto and anchors-only
    t = target.split()[0]
    if t.startswith('http://') or t.startswith('https://') or t.startswith('mailto:'):
        return True
    if t.startswith('#'):
        return True
    # strip query and anchor
    t = t.split('#')[0].split('?')[0]
    if not t:
        return True
    candidates = []
    if t.startswith('/'):
        candidates.append(ROOT / t.lstrip('/'))
    else:
        candidates.append((md.parent / t))
    # try adding .md if missing
    newc = []
    for c in candidates:
        newc.append(c)
        if not c.suffix:
            newc.append(c.with_suffix('.md'))
    for c in newc:
        try:
            if c.exists():
                return True
        except Exception:
            continue
    return False


def scan_markdown() -> Dict:
    broken = []
    md_files = find_markdown_files()
    for md in md_files:
        try:
            txt = md.read_text(encoding='utf-8')
        except Exception:
            continue
        for m in link_re.findall(txt) + image_re.findall(txt):
            if not check_link(md, m):
                broken.append({'file': str(md.relative_to(ROOT)), 'link': m})
    return {'md_scanned': len(md_files), 'broken_links': broken}


def find_run_meta_files() -> List[Path]:
    pats = list(ROOT.rglob('*_run_metadata.json')) + list(ROOT.rglob('*run_metadata.json'))
    # unique
    seen = set()
    out = []
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


def scan_metadata() -> Dict:
    missing = []
    errors = []
    meta_files = find_run_meta_files()
    for p in meta_files:
        try:
            j = json.loads(p.read_text(encoding='utf-8'))
        except Exception as e:
            errors.append({'file': str(p.relative_to(ROOT)), 'error': str(e)})
            continue
        missing_keys = []
        if 'normalization' not in j:
            missing_keys.append('normalization')
        if 'missing_mode' not in j:
            missing_keys.append('missing_mode')
        if missing_keys:
            missing.append({'file': str(p.relative_to(ROOT)), 'missing': missing_keys})
    return {'meta_scanned': len(meta_files), 'meta_missing': missing, 'meta_errors': errors}


def main():
    print('Repo root:', ROOT)
    print('Scanning Markdown files...')
    md_res = scan_markdown()
    print(f"Markdown files scanned: {md_res['md_scanned']}")
    print(f"Broken links found: {len(md_res['broken_links'])}")
    if md_res['broken_links']:
        for b in md_res['broken_links'][:20]:
            print(' -', b['file'], '->', b['link'])

    print('\nScanning run metadata JSON files...')
    meta_res = scan_metadata()
    print(f"Metadata files scanned: {meta_res['meta_scanned']}")
    print(f"Metadata files missing keys: {len(meta_res['meta_missing'])}")
    if meta_res['meta_missing']:
        for m in meta_res['meta_missing'][:40]:
            print(' -', m['file'], 'missing:', ','.join(m['missing']))
    if meta_res['meta_errors']:
        print('Metadata read errors:')
        for e in meta_res['meta_errors'][:20]:
            print(' -', e)

    report = {'markdown': md_res, 'metadata': meta_res}
    rpt_path = ROOT / 'Thesis-Copilot-Toolkit' / 'scripts' / 'verify_report.json'
    try:
        rpt_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
        print('\nReport written to', str(rpt_path))
    except Exception as e:
        print('\nFailed to write report:', e)

    # exit non-zero if issues found
    issues = len(md_res['broken_links']) + len(meta_res['meta_missing']) + len(meta_res['meta_errors'])
    if issues:
        print('\nIssues detected:', issues)
        raise SystemExit(2)
    print('\nNo issues detected.')

if __name__ == '__main__':
    main()
