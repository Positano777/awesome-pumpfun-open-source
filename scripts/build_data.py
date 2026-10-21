import csv, json
from pathlib import Path
root = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((root / 'data/repositories.csv').open(encoding='utf-8-sig')))
(root / 'data/repositories.json').write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
