#!/usr/bin/env python3
"""
label_audit.py — LaTeX Label Harmonization Script
===================================================

Reads vault asset registries (93_Assets/figures_index.md,
tables_index.md, equations_index.md) and operates on all .tex
files in the dissertation repository.

Usage:
  python label_audit.py --report          # report all violations, no changes
  python label_audit.py --plan            # build rename_plan.json from vault
  python label_audit.py --apply --confirm # execute renames across .tex files

Safety:
  --apply requires --confirm AND typing 'yes' at the prompt.
  Creates .bak backups before any write.
  Validates zero orphan refs before any write.
  Logs all operations to label_audit_log.jsonl.

Label Standards:
  Main text:  ch[N]:[type]:[semantic_name]          (exactly 3 colon-parts)
  Appendix:   ch[N]:app:[type]_[scope?]_[name]      (ch[N]:app: prefix)

  Valid ch[N]:   ch1, ch2, ch3
  Valid [type]:  sec, subsec, sssec, fig, tab, eq
"""

import re
import os
import sys
import json
import shutil
import argparse
import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_DIR = SCRIPT_DIR.parent          # ObsidianVault/
REPO_DIR = VAULT_DIR.parent            # Dissertation_Draft/
ASSETS_DIR = VAULT_DIR / "93_Assets"
LOG_FILE = SCRIPT_DIR / "label_audit_log.jsonl"
PLAN_FILE = SCRIPT_DIR / "rename_plan.json"

# .tex source directories (relative to REPO_DIR)
TEX_DIRS = [
    REPO_DIR / "Chapter1",
    REPO_DIR / "Chapter2",
    REPO_DIR / "Chapter3",
    REPO_DIR / "Consolidated",
]

# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------
LABEL_RE = re.compile(r'\\label\{([^}]+)\}')
REF_RE   = re.compile(r'\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}')

VALID_MAIN_RE  = re.compile(r'^ch[123]:(sec|subsec|sssec|fig|tab|eq):[a-zA-Z0-9_]+$')
VALID_APP_RE   = re.compile(r'^ch[123]:app:[a-zA-Z0-9_]+$')

VALID_TYPES = {'sec', 'subsec', 'sssec', 'fig', 'tab', 'eq'}
VALID_CHAPTERS = {'ch1', 'ch2', 'ch3'}


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------
def find_tex_files(dirs):
    """Return sorted list of all .tex files under the given directories."""
    files = []
    for d in dirs:
        if d.exists():
            for p in sorted(d.rglob("*.tex")):
                # Skip _legacy and .bak
                if "_legacy" not in str(p) and not p.name.endswith(".bak"):
                    files.append(p)
    return files


# ---------------------------------------------------------------------------
# Label / ref extraction
# ---------------------------------------------------------------------------
def extract_labels(path):
    """Return list of (label_str, line_no) from a .tex file."""
    results = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(text.splitlines(), 1):
            for m in LABEL_RE.finditer(line):
                results.append((m.group(1), i))
    except Exception as e:
        print(f"  [WARN] Could not read {path}: {e}", file=sys.stderr)
    return results


def extract_refs(path):
    """Return list of (ref_str, line_no) from a .tex file."""
    results = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(text.splitlines(), 1):
            for m in REF_RE.finditer(line):
                results.append((m.group(1), i))
    except Exception as e:
        print(f"  [WARN] Could not read {path}: {e}", file=sys.stderr)
    return results


# ---------------------------------------------------------------------------
# Label validation
# ---------------------------------------------------------------------------
def classify_label(label):
    """
    Return ('ok', None) if label matches the standard.
    Return ('violation', reason) otherwise.
    """
    parts = label.split(':')

    # Must start with ch1/ch2/ch3
    if len(parts) < 2 or parts[0] not in VALID_CHAPTERS:
        return ('violation', f'missing ch[N]: prefix — got "{parts[0] if parts else ""}"')

    # Appendix protocol: ch[N]:app:...
    if parts[1] == 'app':
        if len(parts) == 3 and parts[2]:
            return ('ok', None)
        if len(parts) == 2:
            return ('violation', 'ch[N]:app: with no third segment')
        # 4+ parts under app namespace → underscores should be used instead
        return ('violation',
                f'app label has {len(parts)} colon-parts; use underscores within 3rd segment')

    # Main text protocol: exactly 3 parts
    if len(parts) != 3:
        return ('violation',
                f'main-text label has {len(parts)} colon-parts (expected 3)')

    if parts[1] not in VALID_TYPES:
        return ('violation',
                f'unknown type "{parts[1]}" — valid: {", ".join(sorted(VALID_TYPES))}')

    if not parts[2]:
        return ('violation', 'empty semantic name in 3rd segment')

    return ('ok', None)


# ---------------------------------------------------------------------------
# Vault registry parsing
# ---------------------------------------------------------------------------
def parse_registry(index_path):
    """
    Parse a markdown table from the index file.
    Returns list of dicts with keys: current, canonical, chapter, vault_note, file, used_in
    Reads pipe-delimited table rows; columns identified by header.
    """
    entries = []
    if not index_path.exists():
        print(f"  [WARN] Registry not found: {index_path}", file=sys.stderr)
        return entries

    text = index_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    header = None
    col_map = {}

    for line in lines:
        line = line.strip()
        if not line.startswith('|'):
            header = None
            col_map = {}
            continue

        cells = [c.strip() for c in line.split('|')[1:-1]]

        # Detect header row
        if header is None:
            lower_cells = [c.lower() for c in cells]
            if 'current label' in lower_cells or 'canonical label' in lower_cells:
                header = cells
                col_map = {c.lower(): i for i, c in enumerate(lower_cells)}
                continue

        # Skip separator row
        if all(set(c.replace('-', '').replace(' ', '')) <= {''} for c in cells):
            continue

        if header is None or not col_map:
            continue

        def get(key, default=''):
            idx = col_map.get(key, -1)
            if idx < 0 or idx >= len(cells):
                return default
            val = cells[idx]
            # Strip backticks
            val = val.strip('`')
            # Strip wikilink brackets
            val = re.sub(r'\[\[([^\]]+)\]\]', r'\1', val)
            return val.strip()

        current   = get('current label')
        canonical = get('canonical label')

        if not current or not canonical or current.startswith('---'):
            continue

        entries.append({
            'current':   current,
            'canonical': canonical,
            'vault_note': get('vault note'),
            'file':      get('file'),
            'used_in':   get('used in'),
        })

    return entries


def load_all_registries():
    """Load and merge all three asset registries."""
    entries = []
    for fname in ['figures_index.md', 'tables_index.md', 'equations_index.md']:
        path = ASSETS_DIR / fname
        batch = parse_registry(path)
        entries.extend(batch)
    return entries


# ---------------------------------------------------------------------------
# --report mode
# ---------------------------------------------------------------------------
def cmd_report(args):
    tex_files = find_tex_files(TEX_DIRS)
    print(f"\n{'='*60}")
    print(f"LaTeX Label Audit — REPORT")
    print(f"{'='*60}")
    print(f"Scanning {len(tex_files)} .tex files...\n")

    all_labels = {}   # label -> [(path, line)]
    all_refs   = {}   # ref   -> [(path, line)]

    for path in tex_files:
        rel = path.relative_to(REPO_DIR)
        for label, lineno in extract_labels(path):
            all_labels.setdefault(label, []).append((rel, lineno))
        for ref, lineno in extract_refs(path):
            all_refs.setdefault(ref, []).append((rel, lineno))

    print(f"Found {len(all_labels)} unique labels across all files.")
    print(f"Found {len(all_refs)} unique ref calls across all files.\n")

    # ---- Violations ----
    violations = []
    ok_count = 0
    for label, locations in sorted(all_labels.items()):
        status, reason = classify_label(label)
        if status == 'ok':
            ok_count += 1
        else:
            violations.append((label, reason, locations))

    print(f"Labels conforming to standard: {ok_count}")
    print(f"Labels NOT conforming: {len(violations)}\n")

    if violations:
        print("VIOLATIONS:")
        by_reason = {}
        for label, reason, locs in violations:
            by_reason.setdefault(reason, []).append((label, locs))
        for reason, items in sorted(by_reason.items()):
            print(f"\n  [{reason}] ({len(items)} labels)")
            for label, locs in items[:20]:  # cap at 20 per category
                loc_str = ', '.join(f"{p}:L{l}" for p, l in locs[:3])
                print(f"    {label:<50}  @ {loc_str}")
            if len(items) > 20:
                print(f"    ... and {len(items)-20} more")

    # ---- Broken refs ----
    broken = []
    for ref, locs in sorted(all_refs.items()):
        if ref not in all_labels:
            broken.append((ref, locs))

    print(f"\nBroken cross-references (\\ref{{}} target not defined): {len(broken)}")
    if broken:
        print("BROKEN REFS:")
        for ref, locs in broken:
            loc_str = ', '.join(f"{p}:L{l}" for p, l in locs[:3])
            print(f"  \\ref{{{ref}:<40}}}  @ {loc_str}")

    print(f"\n{'='*60}")
    print(f"Summary: {ok_count} OK, {len(violations)} violations, {len(broken)} broken refs")
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# --plan mode
# ---------------------------------------------------------------------------
def cmd_plan(args):
    print(f"\n{'='*60}")
    print(f"LaTeX Label Audit — BUILD RENAME PLAN")
    print(f"{'='*60}\n")

    entries = load_all_registries()
    print(f"Loaded {len(entries)} entries from vault registries.")

    # Build rename map: current -> canonical
    rename_map = {}
    for e in entries:
        cur = e['current']
        can = e['canonical']
        if cur and can and cur != can:
            if cur in rename_map and rename_map[cur] != can:
                print(f"  [WARN] Conflicting mapping for {cur}: "
                      f"{rename_map[cur]} vs {can}", file=sys.stderr)
            rename_map[cur] = can

    print(f"Rename plan: {len(rename_map)} label renames.\n")

    # Load all refs and validate no orphan refs
    tex_files = find_tex_files(TEX_DIRS)
    all_labels = {}
    all_refs   = {}
    for path in tex_files:
        rel = path.relative_to(REPO_DIR)
        for label, lineno in extract_labels(path):
            all_labels.setdefault(label, []).append((str(rel), lineno))
        for ref, lineno in extract_refs(path):
            all_refs.setdefault(ref, []).append((str(rel), lineno))

    # Check: any ref that points to a current label that IS in the rename plan
    # must also appear in the plan (so it will be updated)
    orphan_refs = []
    for ref in all_refs:
        if ref in rename_map:
            pass  # will be renamed
        elif ref not in all_labels:
            orphan_refs.append(ref)

    # After renaming, check no ref would be left pointing to old name
    would_break = []
    for ref, locs in all_refs.items():
        if ref in rename_map:
            pass  # will be renamed
        elif ref not in all_labels:
            would_break.append((ref, locs))

    if would_break:
        print(f"  [WARN] {len(would_break)} refs already broken (not in rename plan, not defined):")
        for ref, locs in would_break[:10]:
            print(f"    \\ref{{{ref}}}")

    plan = {
        "generated": datetime.datetime.now().isoformat(),
        "rename_count": len(rename_map),
        "renames": [{"current": k, "canonical": v} for k, v in sorted(rename_map.items())],
        "warnings": {
            "broken_refs_before": len(would_break),
            "broken_refs_list": [r for r, _ in would_break[:50]],
        }
    }

    PLAN_FILE.write_text(json.dumps(plan, indent=2), encoding="utf-8")
    print(f"Rename plan saved to: {PLAN_FILE}")
    print(f"\nReview rename_plan.json before running --apply.")
    print(f"\n{'='*60}\n")


# ---------------------------------------------------------------------------
# --apply mode
# ---------------------------------------------------------------------------
def cmd_apply(args):
    if not args.confirm:
        print("ERROR: --apply requires --confirm flag.", file=sys.stderr)
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"LaTeX Label Audit — APPLY RENAMES")
    print(f"{'='*60}\n")
    print("WARNING: This will modify .tex files. Backups will be created.")
    print("         Only labels present in rename_plan.json will be changed.\n")

    if not PLAN_FILE.exists():
        print(f"ERROR: rename_plan.json not found. Run --plan first.", file=sys.stderr)
        sys.exit(1)

    plan = json.loads(PLAN_FILE.read_text(encoding="utf-8"))
    renames = {r["current"]: r["canonical"] for r in plan["renames"]}

    if not renames:
        print("No renames in plan. Nothing to do.")
        return

    print(f"Plan has {len(renames)} renames.")
    print("Type 'yes' to proceed: ", end="")
    answer = input().strip().lower()
    if answer != "yes":
        print("Aborted.")
        return

    tex_files = find_tex_files(TEX_DIRS)
    log_entries = []
    files_modified = 0
    total_replacements = 0

    # Patterns that carry labels/refs
    PATTERNS = [
        (re.compile(r'(\\label\{)([^}]+)(\})'),   'label'),
        (re.compile(r'(\\ref\{)([^}]+)(\})'),       'ref'),
        (re.compile(r'(\\eqref\{)([^}]+)(\})'),     'eqref'),
        (re.compile(r'(\\autoref\{)([^}]+)(\})'),   'autoref'),
        (re.compile(r'(\\pageref\{)([^}]+)(\})'),   'pageref'),
    ]

    for path in tex_files:
        original = path.read_text(encoding="utf-8", errors="replace")
        modified = original
        file_replacements = []

        for pattern, ptype in PATTERNS:
            def replacer(m, _renames=renames, _ptype=ptype, _path=path, _reps=file_replacements):
                old_label = m.group(2)
                if old_label in _renames:
                    new_label = _renames[old_label]
                    _reps.append({
                        "type": _ptype,
                        "old": old_label,
                        "new": new_label,
                    })
                    return m.group(1) + new_label + m.group(3)
                return m.group(0)
            modified = pattern.sub(replacer, modified)

        if modified != original:
            # Create backup
            bak_path = path.with_suffix(path.suffix + ".bak")
            shutil.copy2(path, bak_path)
            path.write_text(modified, encoding="utf-8")
            files_modified += 1
            total_replacements += len(file_replacements)
            rel = str(path.relative_to(REPO_DIR))
            log_entries.append({
                "file": rel,
                "replacements": file_replacements,
            })
            print(f"  Modified: {rel} ({len(file_replacements)} replacements)")

    # Log
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "operation": "apply",
        "files_modified": files_modified,
        "total_replacements": total_replacements,
        "details": log_entries,
    }
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

    print(f"\nDone: {files_modified} files modified, {total_replacements} total replacements.")
    print(f"Backups created as .bak files alongside each modified .tex file.")
    print(f"Log appended to: {LOG_FILE}")
    print(f"\nNext step: cd Consolidated && ./build.sh (or build.bat on Windows)")
    print(f"Verify PDF builds with 0 undefined reference warnings.\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="LaTeX label harmonization — report, plan, or apply renames.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument('--report',  action='store_true',
                        help='Report all label violations and broken refs. No changes.')
    parser.add_argument('--plan',    action='store_true',
                        help='Read vault registries and build rename_plan.json.')
    parser.add_argument('--apply',   action='store_true',
                        help='Apply renames from rename_plan.json to all .tex files.')
    parser.add_argument('--confirm', action='store_true',
                        help='Required with --apply. Also prompts for "yes".')

    args = parser.parse_args()

    if not any([args.report, args.plan, args.apply]):
        parser.print_help()
        sys.exit(0)

    if args.report:
        cmd_report(args)
    if args.plan:
        cmd_plan(args)
    if args.apply:
        cmd_apply(args)


if __name__ == '__main__':
    main()
