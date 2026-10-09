"""
Directory statistics CLI tool
"""

import os, argparse, sys

def get_stats(path):
    total_files = total_dirs = total_size = 0
    for root, dirs, files in os.walk(path):
        total_dirs += len(dirs)
        total_files += len(files)
        for f in files:
            try:
                total_size += os.path.getsize(os.path.join(root, f))
            except OSError:
                continue
    return total_files, total_dirs, total_size

def main():
    parser = argparse.ArgumentParser(description="Show statistics of a directory")
    parser.add_argument('path', nargs='?', default='.', help='Directory to analyze')
    args = parser.parse_args()
    if not os.path.isdir(args.path):
        print(f"Error: '{args.path}' is not a directory", file=sys.stderr)
        sys.exit(1)
    files, dirs, size = get_stats(args.path)
    print(f"Path: {os.path.abspath(args.path)}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")
    print(f"Total size: {size} bytes")

if __name__ == "__main__":
    main()