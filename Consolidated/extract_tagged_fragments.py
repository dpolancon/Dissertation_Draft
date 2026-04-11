from __future__ import annotations

import sys
from pathlib import Path
import re


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "_generated"

FRAGMENTS = [
    ("../Chapter1/Chapter1_CriticalReplication.tex", "ch1body", "ch1body.tex"),
    ("../Chapter1/Chapter1_CriticalReplication.tex", "ch1appendix", "ch1appendix.tex"),
    ("../Chapter2/Chapter2_ProfitRate_Investment.tex", "ch2body", "ch2body.tex"),
    ("../Chapter2/Chapter2_ProfitRate_Investment.tex", "ch2appendix", "ch2appendix.tex"),
    ("../Chapter3/Chapter3_PEUP.tex", "ch3body", "ch3body.tex"),
    ("../Chapter3/Chapter3_PEUP.tex", "ch3appendix", "ch3appendix.tex"),
]

START_RE = re.compile(r"^\s*%<\*(?P<tag>[^>]+)>\s*$")
END_RE = re.compile(r"^\s*%</(?P<tag>[^>]+)>\s*$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def extract_tag(source_path: Path, tag: str) -> str:
    with source_path.open("r", encoding="utf-8", newline="") as handle:
        lines = handle.read().splitlines(keepends=True)

    start_lines: list[int] = []
    end_lines: list[int] = []

    for index, line in enumerate(lines):
        start_match = START_RE.match(line)
        if start_match and start_match.group("tag") == tag:
            start_lines.append(index)
            continue

        end_match = END_RE.match(line)
        if end_match and end_match.group("tag") == tag:
            end_lines.append(index)

    if len(start_lines) != 1:
        fail(f"{source_path}: expected exactly one start tag for '{tag}', found {len(start_lines)}")
    if len(end_lines) != 1:
        fail(f"{source_path}: expected exactly one end tag for '{tag}', found {len(end_lines)}")

    start_index = start_lines[0]
    end_index = end_lines[0]
    if start_index >= end_index:
        fail(f"{source_path}: tag '{tag}' ends before it starts")

    fragment = "".join(lines[start_index + 1 : end_index])
    if not fragment.strip():
        fail(f"{source_path}: tag '{tag}' is empty")

    return fragment


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for relative_source, tag, output_name in FRAGMENTS:
        source_path = (BASE_DIR / relative_source).resolve()
        if not source_path.exists():
            fail(f"missing source file: {source_path}")

        fragment = extract_tag(source_path, tag)
        output_path = OUTPUT_DIR / output_name
        with output_path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(fragment)

        print(f"Wrote {output_path.name} from {source_path.name}:{tag}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
