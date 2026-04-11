#!/bin/bash
# Build the consolidated dissertation
# Run from the Consolidated/ directory

set -euo pipefail

# MiKTeX on Windows uses semicolons; TeX Live on Unix uses colons
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    export TEXINPUTS=".;../Chapter1/;../Chapter2/;../Chapter3/;../figures/;"
else
    export TEXINPUTS=".:../Chapter1/:../Chapter2/:../Chapter3/:../figures/:"
fi

if command -v python >/dev/null 2>&1; then
    PYTHON_BIN=python
else
    PYTHON_BIN=python3
fi

"$PYTHON_BIN" extract_tagged_fragments.py

pdflatex -interaction=scrollmode dissertation
bibtex dissertation
pdflatex -interaction=scrollmode dissertation
pdflatex -interaction=scrollmode dissertation

echo ""
echo "Done. Output: dissertation.pdf"
