#!/bin/bash

# IEEE Conference Paper Compilation Script
# This script compiles the paper.tex file using pdflatex and bibtex

echo "=========================================="
echo "IEEE Conference Paper Compilation Script"
echo "=========================================="
echo ""

# Check if paper.tex exists
if [ ! -f "paper.tex" ]; then
    echo "Error: paper.tex not found in current directory"
    exit 1
fi

# Check if IEEEtran.cls exists
if [ ! -f "IEEEtran.cls" ]; then
    echo "Error: IEEEtran.cls not found in current directory"
    exit 1
fi

echo "Step 1: First pdflatex compilation..."
pdflatex -interaction=nonstopmode paper.tex
if [ $? -ne 0 ]; then
    echo "Error in first pdflatex compilation"
    exit 1
fi

echo ""
echo "Step 2: Running bibtex..."
bibtex paper
if [ $? -ne 0 ]; then
    echo "Warning: bibtex encountered issues (this may be normal)"
fi

echo ""
echo "Step 3: Second pdflatex compilation..."
pdflatex -interaction=nonstopmode paper.tex
if [ $? -ne 0 ]; then
    echo "Error in second pdflatex compilation"
    exit 1
fi

echo ""
echo "Step 4: Final pdflatex compilation..."
pdflatex -interaction=nonstopmode paper.tex
if [ $? -ne 0 ]; then
    echo "Error in final pdflatex compilation"
    exit 1
fi

echo ""
echo "=========================================="
echo "Compilation completed successfully!"
echo "Output file: paper.pdf"
echo "=========================================="
echo ""

# Clean up auxiliary files (optional)
read -p "Do you want to clean up auxiliary files (.aux, .log, .bbl, etc.)? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Cleaning up auxiliary files..."
    rm -f *.aux *.log *.bbl *.blg *.out *.toc *.lof *.lot *.synctex.gz
    echo "Cleanup complete!"
fi

echo ""
echo "Done!"
