#!/usr/bin/env python
"""
deploy_to_latex.py — Vault → LaTeX deployment script

Usage:
    python deploy_to_latex.py --note PATH_TO_NOTE.md --confirm

Reads `deploy_target` and `deploy_section` from note frontmatter.
Shows a diff before writing. Requires --confirm to actually write.
Creates a .bak backup before writing. Logs to deploy_log.jsonl.

GUARDRAIL: This script will NOT write anything without --confirm.
"""

import sys
import os
import re
import json
import shutil
import difflib
import argparse
from datetime import datetime

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(VAULT_ROOT)
DEPLOY_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deploy_log.jsonl")


def parse_frontmatter(text):
    """Extract YAML frontmatter as a dict of key: value strings."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 4:].strip()
    fm = {}
    for line in fm_text.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def strip_vault_syntax(text):
    """
    Remove vault-specific syntax from markdown body:
    - [[wikilinks]] → plain text (keep display text if pipe: [[link|display]] → display)
    - Obsidian frontmatter (already stripped)
    - Bare [[link]] → link text without brackets
    """
    # [[link|display]] → display
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', text)
    # [[link]] → link (remove brackets, keep text)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    return text


def find_section_in_latex(latex_text, section_header):
    """Find the line number where section_header appears in latex_text."""
    lines = latex_text.splitlines()
    for i, line in enumerate(lines):
        if section_header.strip() in line:
            return i
    return None


def check_deploy_eligibility(fm):
    """Check frontmatter for deploy eligibility. Returns (ok, reason)."""
    status = fm.get("status", "")
    if status != "ready-to-deploy":
        return False, f"Note status is '{status}'. Must be 'ready-to-deploy' to deploy."
    if "deploy_target" not in fm:
        return False, "Missing 'deploy_target' in frontmatter."
    if "deploy_section" not in fm:
        return False, "Missing 'deploy_section' in frontmatter."
    return True, "OK"


def get_deploy_body(body_md):
    """
    Extract the deployable content from the note body.
    Strips the ## Notes / ## Key Arguments / ## Links structure,
    keeping only content under ## Deploy Content (if present)
    or the full ## Notes section.
    """
    # If there's an explicit ## Deploy Content section, use that
    deploy_match = re.search(r'^## Deploy Content\s*\n(.*?)(?=^## |\Z)', body_md, re.MULTILINE | re.DOTALL)
    if deploy_match:
        return deploy_match.group(1).strip()

    # Otherwise use ## Notes section
    notes_match = re.search(r'^## Notes\s*\n(.*?)(?=^## |\Z)', body_md, re.MULTILINE | re.DOTALL)
    if notes_match:
        content = notes_match.group(1).strip()
        if content:
            return content

    return None


def main():
    parser = argparse.ArgumentParser(description="Deploy vault note to LaTeX source")
    parser.add_argument("--note", required=True, help="Path to the vault note (.md)")
    parser.add_argument("--confirm", action="store_true", help="Actually write the changes (required to deploy)")
    parser.add_argument("--dry-run", action="store_true", help="Show diff only, do not write (default without --confirm)")
    args = parser.parse_args()

    note_path = os.path.abspath(args.note)
    if not os.path.exists(note_path):
        print(f"ERROR: Note not found: {note_path}")
        sys.exit(1)

    with open(note_path, encoding="utf-8") as f:
        note_text = f.read()

    fm, body = parse_frontmatter(note_text)

    # Eligibility check
    ok, reason = check_deploy_eligibility(fm)
    if not ok:
        print(f"\nDEPLOYMENT BLOCKED: {reason}")
        print("\nTo deploy, set in frontmatter:")
        print("  status: ready-to-deploy")
        print("  deploy_target: Chapter2/Chapter2_ProfitRate_Investment.tex")
        print('  deploy_section: "\\\\subsubsection{Your Section Title}"')
        sys.exit(1)

    deploy_target = fm["deploy_target"]
    deploy_section = fm["deploy_section"]
    latex_path = os.path.join(REPO_ROOT, deploy_target)

    if not os.path.exists(latex_path):
        print(f"ERROR: LaTeX target not found: {latex_path}")
        sys.exit(1)

    # Get deployable content
    deploy_content = get_deploy_body(body)
    if not deploy_content:
        print("ERROR: No deployable content found.")
        print("Add a '## Deploy Content' section or populate '## Notes' with content to deploy.")
        sys.exit(1)

    # Strip vault syntax
    deploy_content_clean = strip_vault_syntax(deploy_content)

    # Read LaTeX file
    with open(latex_path, encoding="utf-8") as f:
        latex_lines = f.readlines()

    latex_text = "".join(latex_lines)
    section_line = find_section_in_latex(latex_text, deploy_section)

    if section_line is None:
        print(f"ERROR: Could not find section '{deploy_section}' in {deploy_target}")
        print("Check that 'deploy_section' exactly matches a line in the LaTeX file.")
        sys.exit(1)

    # Build the new content block (as a LaTeX comment-fenced insert)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    insert_block = (
        f"\n% --- vault-deploy: {os.path.basename(note_path)} [{timestamp}] ---\n"
        f"{deploy_content_clean}\n"
        f"% --- end vault-deploy ---\n"
    )

    # Insert after the section header line
    new_lines = latex_lines[:section_line + 1] + [insert_block] + latex_lines[section_line + 1:]
    new_text = "".join(new_lines)

    # Show diff
    diff = list(difflib.unified_diff(
        latex_lines,
        new_lines,
        fromfile=f"{deploy_target} (original)",
        tofile=f"{deploy_target} (after deploy)",
        lineterm=""
    ))

    print("\n" + "="*60)
    print(f"DEPLOY PREVIEW: {os.path.basename(note_path)} → {deploy_target}")
    print("="*60)
    print(f"Section target: {deploy_section}")
    print(f"Insertion after line: {section_line + 1}")
    print(f"Content length: {len(deploy_content_clean)} chars")
    print("-"*60)
    print("DIFF:")
    for line in diff[:60]:
        print(line)
    if len(diff) > 60:
        print(f"... ({len(diff) - 60} more lines)")
    print("="*60)

    if not args.confirm:
        print("\nDRY RUN — no changes written.")
        print("Add --confirm to actually deploy.")
        sys.exit(0)

    # Final confirmation prompt
    print(f"\nAbout to write to: {latex_path}")
    print("A .bak backup will be created first.")
    answer = input("Type 'yes' to confirm deployment: ").strip().lower()
    if answer != "yes":
        print("Deployment cancelled.")
        sys.exit(0)

    # Create backup
    bak_path = latex_path + f".bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(latex_path, bak_path)
    print(f"Backup created: {bak_path}")

    # Write
    with open(latex_path, "w", encoding="utf-8") as f:
        f.write(new_text)

    # Update note status to 'deployed'
    new_note = note_text.replace("status: ready-to-deploy", "status: deployed")
    with open(note_path, "w", encoding="utf-8") as f:
        f.write(new_note)

    # Log
    log_entry = {
        "timestamp": timestamp,
        "note": note_path,
        "target": latex_path,
        "section": deploy_section,
        "chars_inserted": len(deploy_content_clean),
        "backup": bak_path
    }
    with open(DEPLOY_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

    print(f"\nDeployment complete.")
    print(f"  Written to: {latex_path}")
    print(f"  Note status updated to 'deployed'")
    print(f"  Logged to: {DEPLOY_LOG}")
    print(f"\nNext: rebuild LaTeX with 'cd Consolidated && ./build.sh'")


if __name__ == "__main__":
    main()
