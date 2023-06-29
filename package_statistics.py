import argparse
import collections
from operator import itemgetter
import gzip
import requests


def file_download(architecture):
    # Download Contents file for the specified architecture
    url = f"http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{architecture}.gz"
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        # Locally save the architecture
        with open(f"Contents-{architecture}.gz", "wb") as f:
            f.write(r.content)
        return True
    else:
        return False


def file_parse(architecture):
    packages = collections.defaultdict(int)

    with gzip.open(f"Contents-{architecture}.gz", "rt", encoding="utf-8", errors="replace") as f:
        # Parse the table mapping filenames to packages
        for line in f:
            line = line.strip()
            if not line:
                continue
            filename, package_names = line.split(" ", 1)
            package_names = package_names.split(",")
            for package_name in package_names:
                packages[package_name] += 1

    return packages


def print_stats(packages):
    # Print statistics of the top 10 most common packages
    sorted_packages = sorted(packages.items(), key=itemgetter(1), reverse=True)[:10]
    print("{:<40s} {:<10s}".format("Package", "Number of Files"))
    print("-" * 70)

    for package, file_count in sorted_packages:
        print(f"{package:<40s} {file_count:<10d}")


def main():
    parser = argparse.ArgumentParser(description='Downloads and analyzes debian architectures')
    parser.add_argument("architecture", help="Debian architecture (amd64, arm64, mips etc.)")

    args = parser.parse_args()
    architecture = args.architecture

    if file_download(architecture):
        packages = file_parse(architecture)
        print_stats(packages)
    else:
        print("Failed to download the Contents file.")


if __name__ == "__main__":
    main()
