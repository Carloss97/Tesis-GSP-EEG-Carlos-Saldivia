import os
import json
import re
import shlex

HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SUMMARY_IN = os.path.join(HERE, 'rerun_execution_summary.json')
print('HERE=', HERE)
print('REPO_ROOT=', REPO_ROOT)

if not os.path.exists(SUMMARY_IN):
    print('No summary file at', SUMMARY_IN)
    raise SystemExit(1)

with open(SUMMARY_IN, 'r', encoding='utf-8') as f:
    data = json.load(f)
failed = data.get('failed', [])
if not failed:
    print('No failed entries in summary')
    raise SystemExit(0)

entry = failed[0]
cmd_str = entry.get('command')
print('original command:', cmd_str)

m = re.match(r"\s*&\s*'([^']+)'\s*(.*)", cmd_str)
if m:
    python_path = m.group(1)
    rest = m.group(2)
else:
    parts = cmd_str.strip().split()
    python_path = parts[0] if parts else None
    rest = ' '.join(parts[1:]) if len(parts) > 1 else ''

print('python_path=', python_path)
print('rest(raw)=', rest)
rest_norm = rest.replace('\\', '/')
print('rest_norm=', rest_norm)
args = shlex.split(rest_norm, posix=True)
print('args=', args)

arg0 = args[0] if args else None
if arg0:
    candidate = os.path.join(REPO_ROOT, arg0)
    candidate2 = os.path.join(REPO_ROOT, arg0.replace('/', os.sep))
    print('candidate=', candidate)
    print('candidate exists=', os.path.exists(candidate))
    print('candidate2=', candidate2)
    print('candidate2 exists=', os.path.exists(candidate2))
else:
    print('no arg0 parsed')
