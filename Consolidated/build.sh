#!/bin/bash
# Build the consolidated dissertation
# Run from the Consolidated/ directory

# MiKTeX on Windows uses semicolons; TeX Live on Unix uses colons
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    export TEXINPUTS=".;../Chapter1/;../Chapter2/;../Chapter3/;../figures/;"
else
    export TEXINPUTS=".:../Chapter1/:../Chapter2/:../Chapter3/:../figures/:"
fi

pdflatex -interaction=scrollmode dissertation
bibtex dissertation
pdflatex -interaction=scrollmode dissertation
pdflatex -interaction=scrollmode dissertation

echo ""
echo "Done. Output: dissertation.pdf"
