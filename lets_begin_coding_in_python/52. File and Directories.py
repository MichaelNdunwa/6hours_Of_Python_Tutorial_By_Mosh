from pathlib import Path

all_files = []
path = Path()
for file in path.glob("*.py"):
    print(file)
