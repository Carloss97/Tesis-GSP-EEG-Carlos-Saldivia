#!/usr/bin/env python3
"""
Compacta la estructura de `standardized_results` a una carpeta por iteración `itNNN`.
- Dry-run por defecto; usar `--apply` para mover.
- Genera un reporte JSON con estadísticas en `--report`.

Reglas de mapeo (heurística):
- Busca el ancestro con patrón `it\d{1,3}` y usa ese número como destino `itNNN`.
- Archivos PDF -> `itNNN/figures/`
- .tex -> `itNNN/tables/`
- Archivos con nombre conocido (raw.csv, stats.csv, significance.csv, run_metadata.json, qa_report.md, nogo_report.md, integration_log.md) se ponen en la raíz de `itNNN` con ese nombre.
- Para otros archivos, se preserva la estructura relativa debajo del directorio de origen identificado.
- Si hay colisiones al aplicar, se renombra con sufijo `__dupN`.
"""

from pathlib import Path
import argparse
import json
import re
from collections import defaultdict
import shutil
import sys

KNOWN_FILES = {
    'raw.csv': 'raw.csv',
    'stats.csv': 'stats.csv',
    'significance.csv': 'significance.csv',
    'run_metadata.json': 'run_metadata.json',
    'qa_report.md': 'qa_report.md',
    'qa.md': 'qa_report.md',
    'nogo_report.md': 'nogo_report.md',
    'integration_log.md': 'integration_log.md',
}

IT_RE = re.compile(r'it(\d{1,3})', re.IGNORECASE)


def find_it_parent(path: Path, root: Path):
    for parent in path.parents:
        try:
            parent.relative_to(root)
        except Exception:
            continue
        if IT_RE.search(parent.name):
            return parent
    return None


def canonical_dest(root: Path, it_number: int, src: Path, it_parent: Path):
    dest_base = root / f"it{int(it_number):03d}"
    parent_name = it_parent.name.lower()
    rel = src.relative_to(it_parent)
    rel_parts = rel.parts

    # Heurísticas por carpeta origen
    if 'figures' in parent_name or src.suffix.lower() in {'.pdf', '.png', '.jpg', '.jpeg'}:
        dest = dest_base / 'figures' / Path(*rel_parts)
        return dest
    if 'tables' in parent_name or src.suffix.lower() in {'.tex'}:
        dest = dest_base / 'tables' / Path(*rel_parts)
        return dest

    # Archivos conocidos -> raíz de la iteración
    name_lower = src.name.lower()
    if name_lower in KNOWN_FILES:
        dest = dest_base / KNOWN_FILES[name_lower]
        return dest

    # Si el primer componente relativo es un grupo (figures/tables/raw...), respetarlo
    if len(rel_parts) >= 1 and rel_parts[0].lower() in {'figures', 'tables', 'raw', 'data', 'meta'}:
        dest = dest_base / Path(*rel_parts)
        return dest

    # Por defecto, preservar la estructura relativa (si hay subcarpetas), o poner en la raíz
    if len(rel_parts) > 1:
        dest = dest_base / Path(*rel_parts)
    else:
        dest = dest_base / src.name
    return dest


def unique_path(path: Path):
    if not path.exists():
        return path
    base = path.stem
    suffix = path.suffix
    parent = path.parent
    i = 1
    while True:
        candidate = parent / f"{base}__dup{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def scan_and_plan(root: Path):
    root = root.resolve()
    stats = {
        'root': str(root),
        'files_scanned': 0,
        'planned_moves': 0,
        'unique_it_targets': set(),
        'dest_map': {},
        'conflicts': 0,
    }
    dest_to_srcs = defaultdict(list)
    planned = []

    for p in root.rglob('*'):
        if p.is_file():
            stats['files_scanned'] += 1
            it_parent = find_it_parent(p, root)
            if not it_parent:
                continue
            m = IT_RE.search(it_parent.name)
            if not m:
                continue
            it_num = int(m.group(1))
            dest = canonical_dest(root, it_num, p, it_parent)
            dest_to_srcs[str(dest)].append(str(p))
            planned.append((str(p), str(dest)))
            stats['unique_it_targets'].add(f"it{it_num:03d}")

    # detect conflicts where multiple sources map to same dest OR dest already exists on disk
    conflicts = []
    for dest, srcs in dest_to_srcs.items():
        if len(srcs) > 1:
            conflicts.append({'dest': dest, 'sources': srcs})
        else:
            # if file already exists on disk -> conflict (possible duplicate from previous runs)
            if Path(dest).exists():
                conflicts.append({'dest': dest, 'sources': srcs})

    stats['planned_moves'] = len(planned)
    stats['unique_it_targets'] = sorted(list(stats['unique_it_targets']))
    stats['conflicts'] = len(conflicts)
    stats['planned_sample'] = planned[:50]
    stats['conflict_sample'] = conflicts[:50]
    stats['dest_map'] = {k: v for k, v in list(dest_to_srcs.items())[:200]}  # truncated map sample
    return stats, planned, dest_to_srcs


def apply_moves(root: Path, planned, dest_to_srcs, dry_run: bool):
    root = root.resolve()
    applied = []
    skipped = []
    errors = []
    created_dups = 0

    # We'll move in sorted order for determinism
    for src_str, dest_str in sorted(planned, key=lambda x: x[0]):
        src = Path(src_str)
        dest = Path(dest_str)
        try:
            if dry_run:
                applied.append({'src': str(src), 'dest': str(dest), 'action': 'planned'})
                continue

            # Ensure parent exists
            dest.parent.mkdir(parents=True, exist_ok=True)

            # If dest exists, pick unique
            final_dest = dest
            if final_dest.exists():
                uniq = unique_path(final_dest)
                final_dest = uniq
                created_dups += 1

            # Move file
            shutil.move(str(src), str(final_dest))
            applied.append({'src': str(src), 'dest': str(final_dest)})

            # Try to remove empty parent folders up to root
            cur = src.parent
            while True:
                try:
                    if cur == root:
                        break
                    if not any(cur.iterdir()):
                        cur.rmdir()
                        cur = cur.parent
                    else:
                        break
                except Exception:
                    break

        except Exception as e:
            errors.append({'src': str(src), 'dest': str(dest), 'error': str(e)})

    return {'applied_count': len(applied), 'applied': applied[:200], 'errors': errors, 'created_dups': created_dups, 'skipped_count': len(skipped)}


def write_report(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--root', required=True)
    p.add_argument('--report', required=True)
    p.add_argument('--apply', action='store_true')
    p.add_argument('--dry-run', action='store_true')
    args = p.parse_args()

    root = Path(args.root)
    report_path = Path(args.report)

    if not root.exists():
        print(f"Root not found: {root}")
        sys.exit(2)

    dry_run = True if args.dry_run or not args.apply else False

    stats, planned, dest_to_srcs = scan_and_plan(root)

    out = {'summary': stats}
    out['dry_run'] = dry_run

    if dry_run:
        out['message'] = 'Dry-run: no files moved. Review planned_sample and conflict_sample.'
        write_report(report_path, out)
        print(json.dumps({'status': 'dry-run-complete', 'report': str(report_path)}))
        return

    # apply
    result = apply_moves(root, planned, dest_to_srcs, dry_run=False)
    out['apply_result'] = result
    write_report(report_path, out)
    print(json.dumps({'status': 'apply-complete', 'report': str(report_path), 'applied_count': result['applied_count']}))


if __name__ == '__main__':
    main()
