#!/usr/bin/env python3
import json
from pathlib import Path
import re
from datetime import datetime

ROOT = Path('Thesis-Copilot-Toolkit') / 'standardized_results'
INDEX = ROOT / 'index.json'

TAG_RE = re.compile(r'(it\d{1,3}.*)', re.IGNORECASE)

summary = {}

for p in sorted(ROOT.iterdir()):
    if not p.is_dir():
        continue
    tag = p.name
    m = TAG_RE.match(tag)
    if not m:
        continue
    # detect artifacts
    stored = {
        'raw': None,
        'stats': None,
        'significance': None,
        'qa': None,
        'run_metadata': None,
        'integration_log': None,
        'nogo': None,
        'figures_count': 0,
        'tables_count': 0
    }
    # files
    for f in p.iterdir():
        if f.is_file():
            name = f.name.lower()
            if name == 'raw.csv':
                stored['raw'] = str(f.relative_to(ROOT))
            elif name == 'stats.csv':
                stored['stats'] = str(f.relative_to(ROOT))
            elif name == 'significance.csv':
                stored['significance'] = str(f.relative_to(ROOT))
            elif name in ('qa_report.md','qa.md'):
                stored['qa'] = str(f.relative_to(ROOT))
            elif name == 'run_metadata.json':
                stored['run_metadata'] = str(f.relative_to(ROOT))
            elif name == 'integration_log.md':
                stored['integration_log'] = str(f.relative_to(ROOT))
            elif name == 'nogo_report.md':
                stored['nogo'] = str(f.relative_to(ROOT))
    # figures
    figdir = p / 'figures'
    if figdir.exists() and figdir.is_dir():
        count = 0
        for pdf in figdir.rglob('*.pdf'):
            if pdf.is_file():
                count += 1
        stored['figures_count'] = count
    # tables
    tabdir = p / 'tables'
    if tabdir.exists() and tabdir.is_dir():
        count = 0
        for tex in tabdir.rglob('*.tex'):
            if tex.is_file():
                count += 1
        stored['tables_count'] = count

    # read metadata.json if exists
    source_candidates = {}
    meta_file = p / 'metadata.json'
    if meta_file.exists():
        try:
            data = json.loads(meta_file.read_text())
            source_candidates = data.get('source_candidates', {})
        except Exception:
            source_candidates = {}

    padded = re.search(r'it(\d{1,3})', tag, re.IGNORECASE)
    padded = f"it{int(padded.group(1)):03d}" if padded else tag

    summary[tag] = {
        'original_tag': tag,
        'padded': padded,
        'sanitized': tag,
        'stored': stored,
        'source_candidates': source_candidates,
        'collected_at': datetime.utcnow().isoformat() + 'Z'
    }

index = {'summary': summary, 'generated_at': datetime.utcnow().isoformat() + 'Z'}
INDEX.write_text(json.dumps(index, indent=2))
print(f"Wrote {INDEX}")
