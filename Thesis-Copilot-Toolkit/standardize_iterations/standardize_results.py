#!/usr/bin/env python3
"""
Standardiza artefactos de iteraciones (it1-it130) en una carpeta centralizada.

Uso:
  python standardize_results.py --source-root . --target-root Thesis-Copilot-Toolkit/standardized_results --min 1 --max 130 --yes

El script busca archivos/directorios que contengan tags tipo `itNN` o `itNN_suffix` y copia
los artefactos canonicos (raw, stats, significance, qa_report, run_metadata, figures, tables, etc.)
a una estructura uniforme:

  <target_root>/itNNN_originaltag/
    raw.csv
    stats.csv
    significance.csv
    qa_report.md
    run_metadata.json
    integration_log.md
    nogo_report.md
    figures/*.pdf
    tables/*.tex
    metadata.json

Genera ademas un index global `index.json` en el `target_root` con presencia/ausencia de artefactos.
"""
import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

TAG_RE = re.compile(r"(it\d{1,3}(?:_[a-z0-9_]+)*)", re.IGNORECASE)
EXCLUDE_DIRS = {'.git', '.venv', 'venv', '__pycache__', '.pytest_cache', '.mypy_cache'}


def find_tags_in_text(s):
    return [m.group(1).lower() for m in TAG_RE.finditer(s)]


def classify_path(p: Path, tag: str):
    name = p.name.lower()
    if p.is_dir():
        if name.endswith('_figures') or 'figures' in name:
            return 'figures_dir'
        if name.endswith('_tables') or 'tables' in name:
            return 'tables_dir'
        return None
    # files
    if name.endswith('_raw.csv') or (name.endswith('.csv') and 'raw' in name):
        return 'raw'
    if name.endswith('_stats.csv'):
        return 'stats'
    if name.endswith('_significance.csv'):
        return 'significance'
    if name.endswith('_qa_report.md') or name.endswith('_qa.md') or 'qa' in name and name.endswith('.md'):
        return 'qa'
    if name.endswith('_run_metadata.json') or name.endswith('run_metadata.json'):
        return 'run_metadata'
    if name.endswith('_integration_log.md') or name.endswith('integration_log.md'):
        return 'integration_log'
    if name.endswith('_nogo_report.md') or name.endswith('nogo_report.md'):
        return 'nogo'
    if name.endswith('.pdf') and 'fig' in name:
        return 'figure_file'
    if name.endswith('.tex') and ('tbl' in name or 'table' in name):
        return 'table_file'
    # fallback: treat PDFs under any figures-like parent as figures
    if name.endswith('.pdf'):
        return 'pdf'
    if name.endswith('.tex'):
        return 'tex'
    return None


def choose_best_candidate(cands):
    # cands: list of (path)
    if not cands:
        return None
    # prefer paths under Thesis-Copilot-Toolkit/results or /results/
    preferred = [p for p in cands if '/Thesis-Copilot-Toolkit/results/' in p.as_posix() or '/results/' in p.as_posix()]
    items = preferred or cands
    # choose most recently modified
    items_sorted = sorted(items, key=lambda p: p.stat().st_mtime if p.exists() else 0, reverse=True)
    return items_sorted[0]


def sanitize_tag(tag: str):
    tag = tag.lower()
    m = re.search(r'it(\d{1,3})', tag)
    if m:
        num = int(m.group(1))
    else:
        num = 0
    padded = f'it{num:03d}'
    sanitized = re.sub(r'[^a-z0-9_]+', '_', tag)
    return padded, sanitized


def copy_file(src: Path, dest: Path, dry_run=False):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dry_run:
        print(f"DRY RUN copy: {src} -> {dest}")
        return
    shutil.copy2(src, dest)


def copy_tree(src_dir: Path, dest_dir: Path, pattern='*', dry_run=False):
    if not src_dir.exists():
        return 0
    dest_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for p in sorted(src_dir.rglob(pattern)):
        if p.is_file():
            rel = p.relative_to(src_dir)
            tgt = dest_dir / rel
            copy_file(p, tgt, dry_run=dry_run)
            count += 1
    return count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-root', default='.', help='Raiz del repo a buscar')
    ap.add_argument('--target-root', default='Thesis-Copilot-Toolkit/standardized_results', help='Carpeta destino para resultados estandarizados')
    ap.add_argument('--min', type=int, default=1, help='Iteración mínima (num)')
    ap.add_argument('--max', type=int, default=130, help='Iteración máxima (num)')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--yes', action='store_true')
    args = ap.parse_args()

    src_root = Path(args.source_root).resolve()
    tgt_root = Path(args.target_root).resolve()
    print(f"Source root: {src_root}\nTarget root: {tgt_root}")

    candidates = defaultdict(lambda: defaultdict(list))

    print('Escaneando archivos (esto puede tardar)...')
    for p in src_root.rglob('*'):
        try:
            if any(part in EXCLUDE_DIRS for part in p.parts):
                continue
            s = p.as_posix().lower()
            tags = find_tags_in_text(s)
            if not tags:
                continue
            # pick first tag in path
            tag = tags[0]
            # ensure tag numeric range
            m = re.search(r'it(\d{1,3})', tag)
            if not m:
                continue
            num = int(m.group(1))
            if not (args.min <= num <= args.max):
                continue
            typ = classify_path(p, tag)
            if typ:
                candidates[tag][typ].append(p)
        except Exception as e:
            # ignore unreadable files
            continue

    if not candidates:
        print('No se encontraron artefactos con tags it1-it130 en el repo.')
        return

    summary = {}
    print(f'Iteraciones encontradas: {len(candidates)}')

    for tag, art_map in sorted(candidates.items(), key=lambda x: x[0]):
        padded, sanitized = sanitize_tag(tag)
        folder = tgt_root / f"{padded}_{sanitized}"
        # create structure
        figures_dir = folder / 'figures'
        tables_dir = folder / 'tables'
        folder.mkdir(parents=True, exist_ok=True)
        figures_dir.mkdir(parents=True, exist_ok=True)
        tables_dir.mkdir(parents=True, exist_ok=True)

        stored = {}
        # artifact mapping: choose best candidate for each known artifact
        for art_key in ['raw','stats','significance','qa','run_metadata','integration_log','nogo']:
            cand_list = art_map.get(art_key, [])
            cand = choose_best_candidate(cand_list) if cand_list else None
            if cand:
                dest_name = {
                    'raw':'raw.csv', 'stats':'stats.csv', 'significance':'significance.csv',
                    'qa':'qa_report.md','run_metadata':'run_metadata.json','integration_log':'integration_log.md','nogo':'nogo_report.md'
                }[art_key]
                dst = folder / dest_name
                copy_file(cand, dst, dry_run=args.dry_run)
                stored[art_key] = str(dst.relative_to(tgt_root))
            else:
                stored[art_key] = None

        # figures: prefer figures_dir candidate or individual pdfs
        fig_dir_candidate_list = art_map.get('figures_dir', [])
        fig_dir_candidate = choose_best_candidate(fig_dir_candidate_list) if fig_dir_candidate_list else None
        fig_count = 0
        if fig_dir_candidate:
            fig_count = copy_tree(fig_dir_candidate, figures_dir, pattern='*.pdf', dry_run=args.dry_run)
        else:
            # copy any pdfs matched for this tag
            pdfs = art_map.get('figure_file', []) + art_map.get('pdf', [])
            for pdf in pdfs:
                dst = figures_dir / pdf.name
                copy_file(pdf, dst, dry_run=args.dry_run)
                fig_count += 1
        stored['figures_count'] = fig_count

        # tables: prefer tables_dir or .tex files
        tab_dir_candidate_list = art_map.get('tables_dir', [])
        tab_dir_candidate = choose_best_candidate(tab_dir_candidate_list) if tab_dir_candidate_list else None
        tab_count = 0
        if tab_dir_candidate:
            tab_count = copy_tree(tab_dir_candidate, tables_dir, pattern='*.tex', dry_run=args.dry_run)
        else:
            texs = art_map.get('table_file', []) + art_map.get('tex', [])
            for tex in texs:
                dst = tables_dir / tex.name
                copy_file(tex, dst, dry_run=args.dry_run)
                tab_count += 1
        stored['tables_count'] = tab_count

        # write metadata
        metadata = {
            'original_tag': tag,
            'padded': padded,
            'sanitized': sanitized,
            'stored': stored,
            'source_candidates': {k: [str(x) for x in v] for k, v in art_map.items()},
            'collected_at': datetime.utcnow().isoformat() + 'Z'
        }
        meta_path = folder / 'metadata.json'
        if not args.dry_run:
            meta_path.write_text(json.dumps(metadata, indent=2))

        summary[tag] = metadata

    # write global index
    tgt_root.mkdir(parents=True, exist_ok=True)
    index_path = tgt_root / 'index.json'
    if not args.dry_run:
        index_path.write_text(json.dumps({'summary': summary, 'generated_at': datetime.utcnow().isoformat() + 'Z'}, indent=2))

    print('Estructura de resultados estandarizados creada en:', tgt_root)
    print('Resumen guardado en:', index_path)


if __name__ == '__main__':
    main()
