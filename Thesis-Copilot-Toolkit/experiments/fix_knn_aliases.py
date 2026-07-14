#!/usr/bin/env python3
"""
Fix legacy knn_gaussian / vknn_gaussian names in schedule and batch JSONs.
Creates .bak copies before writing changes.
Run with --apply to modify files; default is dry-run.
"""
import argparse
from pathlib import Path
import sys

CHANGES = {"knn_gaussian": "knng", "vknn_gaussian": "vknng"}


def replace_in_text(text: str):
    count = 0
    for old, new in CHANGES.items():
        c = text.count(old)
        if c:
            text = text.replace(old, new)
            count += c
    return text, count


def process_file(p: Path, apply_changes: bool):
    s = p.read_text(encoding='utf-8')
    new_s, n = replace_in_text(s)
    if n == 0:
        return False, 0
    if apply_changes:
        bak = p.with_suffix(p.suffix + '.bak')
        bak.write_text(s, encoding='utf-8')
        p.write_text(new_s, encoding='utf-8')
    return True, n


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--schedule', required=True, help='Path to canonical schedule JSON')
    parser.add_argument('--apply', action='store_true', help='Write changes (create .bak copies)')
    args = parser.parse_args()

    schedule = Path(args.schedule)
    if not schedule.exists():
        print(f"Schedule not found: {schedule}")
        sys.exit(2)

    files = [schedule]
    batches_dir = schedule.parent / 'batches'
    if batches_dir.exists() and batches_dir.is_dir():
        files.extend(sorted(batches_dir.glob('*.json')))

    total_files = 0
    total_changes = 0
    modified = []
    for f in files:
        ok, n = process_file(f, args.apply)
        total_files += 1
        if ok:
            modified.append((f, n))
            total_changes += n

    print('Dry-run' if not args.apply else 'Applied changes')
    print(f'Files inspected: {total_files}')
    print(f'Total replacements: {total_changes}')
    if modified:
        print('Modified files:')
        for f, n in modified:
            print(f' - {f} : {n} replacements')
    else:
        print('No files needed changes.')

if __name__ == '__main__':
    main()
