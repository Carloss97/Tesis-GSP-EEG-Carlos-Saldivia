import re
from pathlib import Path
p = Path('build/main.log')
if not p.exists():
    print('NO_LOG')
    raise SystemExit(1)
text = p.read_text(encoding='utf-8')
keys = sorted(set(re.findall(r"Citation `([^']+)' undefined", text)))
if not keys:
    print('NONE')
else:
    print('\n'.join(keys))
