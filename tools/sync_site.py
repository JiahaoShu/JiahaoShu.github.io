"""Copy the public site to its existing Vercel mirror, without Git mutations."""

import argparse
from pathlib import Path
import shutil
import subprocess


FILES = (
    ".gitattributes",
    "index.html",
    "stylesheet.css",
    "script.js",
    "vercel.json",
    "images/favicon.svg",
    "images/Jiahaoshu.jpg",
    "images/medals.jpg",
)


def git(directory, *args):
    return subprocess.check_output(
        ["git", "-C", str(directory), *args], text=True, encoding="utf-8"
    ).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--check", action="store_true", help="Compare without writing")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1]
    destination = args.destination.resolve(strict=True)
    remote = git(destination, "remote", "get-url", "origin").lower().removesuffix(".git")
    allowed = {
        "https://github.com/jiahaoshu/jiahaoshu.top",
        "git@github.com:jiahaoshu/jiahaoshu.top",
    }
    if remote not in allowed or Path(git(destination, "rev-parse", "--show-toplevel")).resolve() != destination:
        parser.error("Destination must be the root of the existing JiahaoShu/jiahaoshu.top checkout.")
    if not args.check and git(destination, "status", "--porcelain"):
        parser.error("Destination has local changes. Review and commit them before syncing.")
    different = []
    for name in FILES:
        target = destination / name
        if not target.resolve().is_relative_to(destination):
            parser.error(f"Destination path escapes the checkout: {name}")
        if not target.is_file() or (source / name).read_bytes() != target.read_bytes():
            different.append(name)
    if args.check:
        print("Different: " + ", ".join(different) if different else "All public site files match.")
        return int(bool(different))
    for name in different:
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / name, target)
        print("Copied " + name)
    print("Review, commit, and push both repositories separately; nothing has been published by this script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
