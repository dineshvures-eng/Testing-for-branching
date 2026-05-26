import json
from pathlib import Path

p = Path("data.json")

# write
data = {"name": "Alice", "age": 30}
p.write_text(json.dumps(data, indent=2), encoding="utf-8")
print(f"Wrote {p}")

# read
print("Read back:", json.loads(p.read_text(encoding="utf-8")))
