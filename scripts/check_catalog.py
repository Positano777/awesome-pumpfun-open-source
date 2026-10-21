import csv, json
from pathlib import Path
root = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((root / 'data/repositories.csv').open(encoding='utf-8-sig')))
assert rows == json.loads((root / 'data/repositories.json').read_text(encoding='utf-8')), 'CSV and JSON differ'
names = [r['owner_repo_or_unresolved_name'] for r in rows]
assert len(names) == len(set(names)), 'Duplicate names'
for row in rows:
    assert all(isinstance(v, str) and v.strip() for v in row.values()), row
    assert row['source_url'].startswith('https://') or row['source_url'] == 'Unresolved', row
print(f'Checked {len(rows)} unique catalog records')
