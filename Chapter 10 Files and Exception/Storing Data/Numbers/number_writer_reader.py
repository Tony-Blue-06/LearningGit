from pathlib import Path
import json
import random

numbers = random.sample(range(1, 21), 5)
path = Path("Storing Data/numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)
print(numbers)
numbers = json.loads(path.read_text())
print(f"Numbers read from file: {numbers}")