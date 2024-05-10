import os
from argparse import ArgumentParser

from pathlib import Path
from patoolib import extract_archive


def scan_recursive(base_dir):
    for entry in os.scandir(base_dir):
        if entry.is_dir(follow_symlinks=False):
            yield from scan_recursive(entry.path)  # see below for Python 2.x
        elif entry.path.endswith('.zip') or entry.path.endswith('.rar') or entry.path.endswith('.7z'):
            yield entry

def main():
    parser = ArgumentParser()
    parser.add_argument('dir', help='Directory to extract the files')
    args = parser.parse_args()

    zip_files = [entry.path for entry in scan_recursive(args.dir)]

    for file in zip_files:
        try:
            folder = Path(file).parent
            extract_archive(file, outdir=folder)
        except Exception as e:
            print(f'Error extracting {file}: {e}')
            pass

if __name__ == '__main__':
    main()