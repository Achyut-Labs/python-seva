import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")
parser.add_argument("directory")

args = parser.parse_args()

target_dir = Path(args.path)
Path(args.directory)
if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)