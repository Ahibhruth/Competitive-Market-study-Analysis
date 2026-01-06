# IEEE Conference Format Paper Package

This directory contains the complete research paper formatted according to IEEE conference template standards.

## Package Contents

### Main Files
- **paper.tex** - Main LaTeX document formatted using IEEEtran class for conference proceedings
- **IEEEtran.cls** - IEEE conference class file (required for compilation)
- **references.bib** - BibTeX bibliography file with all citations

### Figures
- **figures/eda/** - Exploratory Data Analysis visualizations
  - `response_lag_distribution.png` - Response lag distributions
  - `action_type_vs_response_type_heatmap.png` - Japanese market heatmap
  - `action_type_vs_response_type_heatmap_copy.png` - Indian market heatmap
  - Additional copies for variations

- **figures/game_theory/** - Game-theoretic analysis visualizations
  - `payoff_matrix.png` - Payoff structure visualization
  - `repeated_game_simulation.png` - Simulation results
  - `joint_payoff_landscape.png` - Joint payoff landscape

## Compilation Instructions

### Using pdflatex:
```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

### Using latexmk (recommended):
```bash
latexmk -pdf paper.tex
```

### Using Overleaf:
1. Upload all files to an Overleaf project
2. Ensure IEEEtran.cls is in the root directory
3. Set the compiler to pdfLaTeX
4. Compile normally

## IEEE Conference Template Compliance

This paper follows IEEE conference template standards including:
- Two-column format using `\documentclass[conference]{IEEEtran}`
- IEEE-style citations using `\bibliographystyle{IEEEtran}`
- Proper figure and table formatting
- Standard IEEE section structure
- Appropriate heading levels and formatting

## Key Formatting Features

### Document Structure
- Conference paper format (two-column)
- Abstract with IEEE keywords
- Standard sections: Introduction, Literature Review, Methodology, Results, Conclusion
- Acknowledgments section
- IEEE-style bibliography

### Tables and Figures
- All figures positioned using `[htbp]` for optimal placement
- Figure captions below figures
- Table captions above tables
- Proper figure width specifications (`3.5in` for column-spanning figures)
- All graphics use PNG format for compatibility

### Mathematical Content
- Equations numbered consecutively
- Proper mathematical notation using amsmath package
- In-line and display equations formatted according to IEEE standards

### Citations
- Numerical citation style using `\cite{}`
- IEEE-standard bibliography formatting
- All references properly formatted in references.bib

## Dependencies

Required LaTeX packages (included in preamble):
- cite - Citation management
- amsmath, amssymb, amsfonts - Mathematical notation
- graphicx - Graphics inclusion
- booktabs - Professional table formatting
- float - Figure placement control
- caption - Caption formatting

## Paper Metadata

**Title:** Reactive Competition in Oligopolistic Markets: An Empirical and Game-Theoretic Study of Pricing Dynamics

**Abstract:** This study investigates competitive pricing dynamics in oligopolistic markets using a novel dataset of event-based actions from the electronics retail and telecommunications sectors.

**Keywords:** competitive dynamics, game theory, oligopoly, pricing strategy, exploratory data analysis

## Notes

- All author information is currently anonymized (as per double-blind review if needed)
- Update author names and affiliations before submission
- Verify all figure references are correct after compilation
- Check that all citations are properly formatted
- Ensure compliance with specific conference page limits

## License and Attribution

This research paper and associated materials are part of the Competitive Market Study Analysis project.

---

**Created:** January 2026  
**Format:** IEEE Conference Template  
**Compiler:** pdfLaTeX or XeLaTeX recommended
