import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")
parser.add_argument("directory")

args = parser.parse_args()

# print(args[0], args[1], args[2])

target_dir = Path(args.path)
target_dir = Path(args.directory)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)