#!/usr/bin/env python3
"""
Monitor LT20 run log and print a compact update every 5 minutes.
Writes updates to `experiments/resume_lt20_and_run.monitor.log` and
prints the same output to stdout so the terminal shows periodic summaries.
"""
import time
import os
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
RUN_LOG = ROOT / 'experiments' / 'resume_lt20_and_run.fullrun.log'
MONITOR_LOG = ROOT / 'experiments' / 'resume_lt20_and_run.monitor.log'
SLEEP_SECONDS = 300  # 5 minutes

prev_pos = 0
line_count = 0
first = True

def _append_monitor(text: str):
    with open(MONITOR_LOG, 'a', encoding='utf-8', errors='replace') as mf:
        mf.write(text)
        mf.write('\n')

print('Monitor started; writing to', MONITOR_LOG)
_append_monitor(f"MONITOR START {datetime.now().isoformat()}\n")

while True:
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if RUN_LOG.exists():
        try:
            if first:
                # on first run, capture full file
                with open(RUN_LOG, 'r', encoding='utf-8', errors='replace') as f:
                    all_lines = f.readlines()
                total = len(all_lines)
                new_lines = all_lines[-50:]
                prev_pos = os.path.getsize(RUN_LOG)
                line_count = total
                first = False
            else:
                with open(RUN_LOG, 'rb') as f:
                    f.seek(prev_pos)
                    data = f.read()
                    prev_pos = f.tell()
                if data:
                    text = data.decode('utf-8', errors='replace')
                    new_lines = text.splitlines()
                else:
                    new_lines = []
                total = line_count + len(new_lines)
                line_count = total

            new_count = len(new_lines)
            tail = new_lines[-50:] if new_lines else []
            header = f'=== MONITOR {ts} total_lines={total} new_lines={new_count} ==='
            out_lines = [header] + [l.rstrip('\n') for l in tail]
            out = '\n'.join(out_lines)
            print(out)
            _append_monitor(out)
        except Exception as e:
            err = f'=== MONITOR {ts} ERROR reading log: {e} ==='
            print(err)
            _append_monitor(err)
    else:
        msg = f'=== MONITOR {ts} log not found: {RUN_LOG} ==='
        print(msg)
        _append_monitor(msg)

    time.sleep(SLEEP_SECONDS)
