#!/usr/bin/env python3
import time
from pathlib import Path
from datetime import datetime
ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'
LOG = ROOT / 'experiments' / 'propose_and_try_mappings.progress.log'

while True:
    files = list(RESULTS.rglob('rerun_*_raw.csv'))
    done = len(files)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, 'a', encoding='utf-8') as fh:
        fh.write(f"{now} DONE:{done}\n")
    time.sleep(300)
