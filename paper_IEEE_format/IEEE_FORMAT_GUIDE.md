# IEEE Conference Format Quick Reference Guide

## Overview
This document provides a quick reference for key IEEE conference format rules applied in this paper.

## Document Class
```latex
\documentclass[conference]{IEEEtran}
```
- Use `conference` option for IEEE conference papers
- Use `journal` option for journal submissions

## Page Layout
- **Two-column format**: Automatic with IEEEtran conference class
- **Margins**: Handled automatically by the class file
- **Column separation**: Standard IEEE spacing
- **Page numbers**: Will be added by IEEE during production

## Title and Authors

### Title
```latex
\title{Your Paper Title*\\
{\footnotesize \textsuperscript{*}Note: Optional subtitle note}
}
```
- Capitalize principal words
- Avoid using "that uses" constructions
- No symbols or math in title

### Authors
```latex
\author{\IEEEauthorblockN{Author Name}
\IEEEauthorblockA{\textit{Department Name} \\
\textit{Organization Name}\\
City, Country \\
email@example.com}
}
```
- List authors left to right, then top to bottom
- Use `\and` between author blocks
- Keep affiliations succinct

## Abstract
```latex
\begin{abstract}
Your abstract text here...
\end{abstract}
```
- No symbols, special characters, footnotes, or math
- Typical length: 150-250 words
- Should be self-contained

## Keywords
```latex
\begin{IEEEkeywords}
keyword1, keyword2, keyword3
\end{IEEEkeywords}
```
- 3-7 keywords recommended
- Lowercase unless proper nouns

## Sections

### Main Sections
```latex
\section{Section Name}
```
- Roman numeral numbering (automatic)
- Capitalize first word and proper nouns

### Subsections
```latex
\subsection{Subsection Name}
```
- Uppercase letter numbering (A, B, C...)

### Subsubsections
```latex
\subsubsection{Subsubsection Name}
```
- Arabic numeral numbering (1, 2, 3...)

## Figures

### Basic Figure
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=3.5in]{path/to/figure.png}
    \caption{Your caption here.}
    \label{fig:yourlabel}
\end{figure}
```

### Key Rules
- Caption goes BELOW the figure
- Use `\includegraphics[width=3.5in]{}` for full-width figures
- Use `\includegraphics[width=\columnwidth]{}` for column-width figures
- Reference as: `Fig.~\ref{fig:yourlabel}` (abbreviated even at sentence start)
- Placement: Top and bottom of columns preferred

## Tables

### Basic Table
```latex
\begin{table}[h]
    \centering
    \caption{Your Table Title}
    \label{tab:yourlabel}
    \begin{tabular}{lcc}
    \toprule
    \textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
    \midrule
    Data 1 & Data 2 & Data 3 \\
    \bottomrule
    \end{tabular}
\end{table}
```

### Key Rules
- Caption goes ABOVE the table
- Use booktabs package for professional appearance: `\toprule`, `\midrule`, `\bottomrule`
- Reference as: `Table~\ref{tab:yourlabel}` (spell out, even at sentence start)
- Use table footnotes with superscript letters

## Equations

### Numbered Equations
```latex
\begin{equation}
    a + b = c
    \label{eq:yourlabel}
\end{equation}
```

### Key Rules
- Reference as: `\eqref{eq:yourlabel}` or `(\ref{eq:yourlabel})`
- At sentence start: "Equation~\eqref{eq:yourlabel} shows..."
- Not at sentence start: "as shown in~\eqref{eq:yourlabel}"
- Punctuate equations when part of sentence
- Italicize Roman variables, not Greek symbols

### Inline Math
```latex
The variable $x$ represents...
```

## Citations

### In Text
```latex
as shown by Smith~\cite{smith2020}
according to recent work~\cite{smith2020, jones2021}
```

### Bibliography Style
```latex
\bibliographystyle{IEEEtran}
\bibliography{references}
```

### Key Rules
- Use numerical citations [1], [2], etc.
- Sentence punctuation follows the bracket
- Don't use "Ref. [1]" except at sentence start: "Reference [1] shows..."
- Give all authors' names unless six or more (then use "et al.")

## Units and Abbreviations

### Units
- Use SI (MKS) units (encouraged)
- Spell out units in text: "a few henries" not "a few H"
- Use zero before decimals: "0.25" not ".25"

### Abbreviations
- Define on first use, even after abstract
- IEEE, SI, MKS, CGS, ac, dc, rms don't need definition
- No abbreviations in title or abstract

## Common Mistakes to Avoid

1. **"Data" is plural**, not singular
2. **$\mu_0$** is zero with subscript, not lowercase "o"
3. **Punctuation and quotes**: In American English, commas and periods go inside quotes only for complete thoughts
4. **"Effect" vs. "affect"**: effect is noun, affect is verb (usually)
5. **"i.e." means "that is"**, "e.g." means "for example"
6. **"et al."** has a period after "al" only
7. **Use "alternatively"** not "alternately" (unless you mean alternating)

## Special Sections

### Acknowledgments
```latex
\section*{Acknowledgment}
```
- Use asterisk for unnumbered section
- No "e" after "g" in American spelling

### References
```latex
\bibliographystyle{IEEEtran}
\bibliography{references}
```
- Automatically formatted by BibTeX

## Compilation Order

1. `pdflatex paper.tex` (first pass)
2. `bibtex paper` (process bibliography)
3. `pdflatex paper.tex` (second pass)
4. `pdflatex paper.tex` (final pass)

Or use the provided `compile.sh` script:
```bash
./compile.sh
```

## Package Requirements

Minimum required packages (included in template):
```latex
\usepackage{cite}              % Citation handling
\usepackage{amsmath,amssymb,amsfonts}  % Math
\usepackage{graphicx}          % Graphics
\usepackage{booktabs}          % Professional tables
```

## Column and Page Layout

- **Text width**: Two columns, managed automatically
- **Figure spanning**: Use `\begin{figure*}...\end{figure*}` for full-width figures
- **Table spanning**: Use `\begin{table*}...\end{table*}` for full-width tables

## Final Checklist

Before submission:
- [ ] Remove all template guidance text
- [ ] Update author names and affiliations
- [ ] Verify all figures are referenced and visible
- [ ] Check all citations are in references.bib
- [ ] Compile successfully without errors
- [ ] Check page limit compliance
- [ ] Verify abstract has no math/symbols
- [ ] Spell check entire document
- [ ] Check all URLs are valid (if included)
- [ ] Remove any \usepackage{} that aren't needed

## Resources

- IEEE Author Center: https://journals.ieeeauthorcenter.ieee.org/
- IEEEtran Class Documentation: http://www.ctan.org/pkg/ieeetran
- IEEE Editorial Style Manual: Available from IEEE

---

**Note**: This is a quick reference. For complete details, consult the official IEEE Author Guidelines and the IEEEtran class documentation.
