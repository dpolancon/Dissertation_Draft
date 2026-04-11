@echo off
REM Build the consolidated dissertation
REM Run from the Consolidated\ directory

python extract_tagged_fragments.py
if errorlevel 1 exit /b %errorlevel%

set TEXINPUTS=.;../Chapter1/;../Chapter2/;../Chapter3/;../figures/;

pdflatex dissertation
if errorlevel 1 exit /b %errorlevel%
bibtex dissertation
if errorlevel 1 exit /b %errorlevel%
pdflatex dissertation
if errorlevel 1 exit /b %errorlevel%
pdflatex dissertation
if errorlevel 1 exit /b %errorlevel%

echo.
echo Done. Output: dissertation.pdf
