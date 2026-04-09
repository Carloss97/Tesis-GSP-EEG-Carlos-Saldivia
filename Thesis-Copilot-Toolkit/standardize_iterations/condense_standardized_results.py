#!/usr/bin/env python3
"""
Condensa archivos duplicados en `standardized_results` agrupando los ficheros que contienen
"__dup" en archivos ZIP por cada `itNNN`.

Uso (dry-run por defecto):
  python condense_standardized_results.py --root ../standardized_results --outdir .

Para aplicar cambios (crear ZIPs y borrar originales):
  python condense_standardized_results.py --apply

Genera un JSON de reporte en `--outdir` con los candidatos (dryrun) o las acciones realizadas (apply).
"""
import argparse
import json
import os
import re
import time
import hashlib
import zipfile
from pathlib import Path


def parse_args():
    p = argparse.ArgumentParser(description='Condensa archivos __dup por itNNN (dry-run por defecto).')
    p.add_argument('--root', default='Thesis-Copilot-Toolkit/standardized_results', help='Ruta raíz de standardized_results')
    p.add_argument('--outdir', default='Thesis-Copilot-Toolkit/standardize_iterations', help='Dónde escribir reportes')
    p.add_argument('--apply', action='store_true', help='Aplicar cambios: crear ZIPs y eliminar archivos originales')
    p.add_argument('--pattern', default='__dup', help='Subcadena para detectar archivos duplicados (por defecto: __dup)')
    p.add_argument('--backup-path', default='Thesis-Copilot-Toolkit/standardize_iterations/standardized_results_backup.tar.gz', help='Ruta al backup (recomendada antes de aplicar)')
    p.add_argument('--verbose', action='store_true')
    return p.parse_args()


def find_it_dirs(root: Path):
    if not root.exists():
        return []
    it_dirs = [d for d in root.iterdir() if d.is_dir() and re.match(r'^it\d{3}$', d.name)]
    it_dirs.sort()
    return it_dirs


def collect_candidates(it_path: Path, pattern: str):
    candidates = []
    for dirpath, dirnames, filenames in os.walk(it_path):
        for fn in filenames:
            if pattern in fn:
                candidates.append(Path(dirpath) / fn)
    return candidates


def sha256_of_file(p: Path):
    h = hashlib.sha256()
    with p.open('rb') as fh:
        for chunk in iter(lambda: fh.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def create_archive(it_path: Path, candidates, timestamp: str):
    archive_name = f'archived_dup_files_{timestamp}.zip'
    archive_path = it_path / archive_name
    with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for p in candidates:
            arcname = p.relative_to(it_path).as_posix()
            zf.write(p, arcname)
    return archive_path


def write_manifest(it_path: Path, archive_path: Path, candidates):
    manifest = {'archive': archive_path.name, 'files': []}
    for p in candidates:
        rel = p.relative_to(it_path).as_posix()
        manifest['files'].append({'path': rel, 'size': p.stat().st_size, 'sha256': sha256_of_file(p)})
    manifest_path = it_path / (archive_path.stem + '_manifest.json')
    with manifest_path.open('w', encoding='utf-8') as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
    return manifest_path


def remove_files(candidates):
    removed = []
    errors = []
    for p in candidates:
        try:
            p.unlink()
            removed.append(str(p))
        except Exception as e:
            errors.append({'file': str(p), 'error': str(e)})
    return removed, errors


def main():
    args = parse_args()
    root = Path(args.root)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime('%Y%m%d_%H%M%S')

    report = {'root': str(root.resolve()), 'dry_run': not args.apply, 'apply': bool(args.apply), 'it_summaries': [], 'total_candidates': 0}

    it_dirs = find_it_dirs(root)
    for it in it_dirs:
        candidates = collect_candidates(it, args.pattern)
        if not candidates:
            continue
        total_size = sum(p.stat().st_size for p in candidates)
        sample = [str(p.relative_to(it).as_posix()) for p in candidates[:10]]
        it_summary = {'it': it.name, 'candidates_count': len(candidates), 'total_size_bytes': total_size, 'sample': sample}
        report['it_summaries'].append(it_summary)
        report['total_candidates'] += len(candidates)

        if args.apply:
            if not Path(args.backup_path).exists():
                print(f'Backup no encontrado en {args.backup_path}. Abortando apply para {it.name}.')
                it_summary['apply_status'] = 'backup_missing'
                continue
            archive_path = create_archive(it, candidates, timestamp)
            manifest_path = write_manifest(it, archive_path, candidates)
            removed, errors = remove_files(candidates)
            it_summary['archive'] = str(archive_path.name)
            it_summary['manifest'] = str(manifest_path.name)
            it_summary['removed_count'] = len(removed)
            it_summary['errors'] = errors

    report_name = f'condense_standardized_results_{"apply" if args.apply else "dryrun"}_report_{timestamp}.json'
    report_path = outdir / report_name
    with report_path.open('w', encoding='utf-8') as fh:
        json.dump(report, fh, indent=2, ensure_ascii=False)

    print(f'Wrote report: {report_path}')
    print(json.dumps({'root': report['root'], 'total_candidates': report['total_candidates'], 'it_count': len(report['it_summaries'])}))


if __name__ == '__main__':
    main()
