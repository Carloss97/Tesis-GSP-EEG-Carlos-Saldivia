#!/usr/bin/env python3
import json
import os
from datetime import datetime

HERE = os.path.abspath(os.path.dirname(__file__))
SUMMARY_IN = os.path.join(HERE, 'retry_execution_summary.json')
OUT_SUMMARY = os.path.join(HERE, 'final_standardization_summary.json')
OUT_FAILED = os.path.join(HERE, 'failed_to_retry.json')
INDEX_PATH = os.path.abspath(os.path.join(HERE, '..', 'standardized_results', 'index.json'))

with open(SUMMARY_IN, 'r', encoding='utf-8') as f:
    data = json.load(f)

succeeded = [e.get('iteration') for e in data.get('succeeded', [])]
failed = [e.get('iteration') for e in data.get('failed', [])]
timed_out = [e.get('iteration') for e in data.get('timed_out', [])]

summary = {
    'generated_at': datetime.utcnow().isoformat() + 'Z',
    'succeeded_count': len(succeeded),
    'failed_count': len(failed),
    'timed_out_count': len(timed_out),
    'succeeded': succeeded,
    'failed': failed,
    'timed_out': timed_out,
    'index_path': INDEX_PATH,
}

with open(OUT_SUMMARY, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2)

with open(OUT_FAILED, 'w', encoding='utf-8') as f:
    json.dump({'failed_iterations': failed}, f, indent=2)

print(f"Succeeded: {len(succeeded)}, Failed: {len(failed)}, Timed out: {len(timed_out)}")
print('Wrote:', OUT_SUMMARY)
print('Wrote:', OUT_FAILED)
