#!/usr/bin/env python3
"""
_legacy manifest generator.

Scans all _legacy/ directories in the repo (root + chapter-level),
generates MANIFEST.md with file metadata: path, size, last-modified date,
and git status (tracked/untracked).

Run from the repo root:
    python _legacy/update_manifest.py

Or invoke automatically via a git pre-commit hook or CI step.
"""

import os
import subprocess
import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / "_legacy" / "MANIFEST.md"

def get_git_tracked_files():
    """Return set of git-tracked file paths relative to repo root."""
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        return set(result.stdout.strip().split("\n"))
    except Exception:
        return set()

def find_legacy_files():
    """Find all files in any _legacy/ directory under repo root."""
    legacy_files = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        # Skip .git
        if ".git" in dirpath:
            continue
        dir_name = os.path.basename(dirpath)
        if dir_name == "_legacy":
            for fname in sorted(filenames):
                if fname == "MANIFEST.md" or fname == "update_manifest.py":
                    continue
                fpath = Path(dirpath) / fname
                legacy_files.append(fpath)
    return legacy_files

def file_info(fpath, tracked_files):
    """Return metadata dict for a legacy file."""
    rel = fpath.relative_to(REPO_ROOT).as_posix()
    stat = fpath.stat()
    modified = datetime.datetime.fromtimestamp(stat.st_mtime)
    size_kb = stat.st_size / 1024
    git_status = "tracked" if rel in tracked_files else "untracked"
    return {
        "path": rel,
        "size": f"{size_kb:.1f} KB",
        "modified": modified.strftime("%Y-%m-%d"),
        "git_status": git_status,
    }

def group_by_directory(file_infos):
    """Group file info dicts by their _legacy parent directory."""
    groups = {}
    for info in file_infos:
        parts = info["path"].split("/")
        # Find the _legacy part and take everything before it
        legacy_idx = parts.index("_legacy")
        parent = "/".join(parts[:legacy_idx]) if legacy_idx > 0 else "(root)"
        groups.setdefault(parent, []).append(info)
    return groups

def generate_manifest(groups):
    """Generate MANIFEST.md content."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Legacy Manifest",
        "",
        f"_Auto-generated on {now} by `_legacy/update_manifest.py`._",
        f"_Do not edit manually — run the script to refresh._",
        "",
    ]

    total = sum(len(files) for files in groups.values())
    lines.append(f"**{total} archived files** across {len(groups)} locations.")
    lines.append("")

    for parent in sorted(groups.keys()):
        files = groups[parent]
        if parent == "(root)":
            lines.append("## Root `_legacy/`")
        else:
            lines.append(f"## `{parent}/_legacy/`")
        lines.append("")
        lines.append("| File | Size | Modified | Git |")
        lines.append("|------|------|----------|-----|")
        for f in files:
            fname = f["path"].split("/")[-1]
            lines.append(f"| `{fname}` | {f['size']} | {f['modified']} | {f['git_status']} |")
        lines.append("")

    return "\n".join(lines)

def main():
    tracked = get_git_tracked_files()
    legacy_files = find_legacy_files()

    if not legacy_files:
        print("No legacy files found.")
        return

    file_infos = [file_info(f, tracked) for f in legacy_files]
    groups = group_by_directory(file_infos)
    manifest = generate_manifest(groups)

    MANIFEST_PATH.write_text(manifest, encoding="utf-8")
    print(f"Manifest written: {MANIFEST_PATH}")
    print(f"  {len(file_infos)} files catalogued")

if __name__ == "__main__":
    main()
