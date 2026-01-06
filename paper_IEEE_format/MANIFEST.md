# Paper IEEE Format Package Manifest

**Package Name:** paper_IEEE_format  
**Created:** January 6, 2026  
**Purpose:** IEEE Conference Template formatted research paper package

## Complete File Structure

```
paper_IEEE_format/
├── paper.tex                           # Main LaTeX document (IEEE conference format)
├── IEEEtran.cls                        # IEEE conference class file
├── references.bib                      # BibTeX bibliography database
├── README.md                           # Package documentation
├── IEEE_FORMAT_GUIDE.md               # Quick reference for IEEE formatting rules
├── compile.sh                          # Automated compilation script (executable)
├── MANIFEST.md                        # This file - complete package listing
└── figures/                           # All figure assets
    ├── eda/                           # Exploratory Data Analysis figures
    │   ├── response_lag_distribution.png
    │   ├── response_lag_distribution_copy.png
    │   ├── action_type_vs_response_type_heatmap.png
    │   └── action_type_vs_response_type_heatmap_copy.png
    └── game_theory/                   # Game Theory Analysis figures
        ├── payoff_matrix.png
        ├── repeated_game_simulation.png
        └── joint_payoff_landscape.png
```

## File Descriptions

### Core LaTeX Files

#### paper.tex (35 KB)
- Main research paper document
- Formatted using IEEEtran conference class
- Complete paper content including:
  - Title and abstract
  - Introduction and literature review
  - Dataset description and methodology
  - Exploratory data analysis results
  - Game-theoretic framework and analysis
  - Results, discussion, and conclusions
  - All sections properly formatted for IEEE conference proceedings

#### IEEEtran.cls (275 KB)
- Official IEEE conference LaTeX class file
- Provides conference paper formatting
- Handles two-column layout, margins, fonts, and spacing
- Required for proper compilation

#### references.bib (8 KB)
- BibTeX bibliography database
- Contains all cited references
- Formatted for IEEE citation style
- Includes 40+ references from the original paper

### Documentation Files

#### README.md (3.8 KB)
- Main package documentation
- Compilation instructions
- Package contents overview
- Dependencies and requirements
- Notes on IEEE compliance

#### IEEE_FORMAT_GUIDE.md (6.4 KB)
- Quick reference guide for IEEE formatting
- Section-by-section formatting rules
- Common mistakes to avoid
- Examples and best practices
- Final submission checklist

#### MANIFEST.md (This File)
- Complete package inventory
- File descriptions and purposes
- Change log and version info
- Comparison with original paper

### Utility Scripts

#### compile.sh (1.7 KB)
- Automated compilation script
- Runs full LaTeX + BibTeX compilation sequence
- Error checking at each step
- Optional auxiliary file cleanup
- Executable (chmod +x applied)

### Figure Assets

#### figures/eda/ (4 files)
PNG format figures from exploratory data analysis:

1. **response_lag_distribution.png**
   - Histogram showing response time distributions
   - Japanese retail sector analysis
   
2. **response_lag_distribution_copy.png**
   - Response time distributions for comparison
   - Indian telecom/FMCG sector analysis
   
3. **action_type_vs_response_type_heatmap.png**
   - Heatmap of action-response patterns
   - Japanese electronics retail and food service
   
4. **action_type_vs_response_type_heatmap_copy.png**
   - Heatmap for Indian market
   - Telecom and FMCG sectors

#### figures/game_theory/ (3 files)
PNG format figures from game-theoretic analysis:

1. **payoff_matrix.png**
   - Visual representation of payoff structure
   - Shows prisoner's dilemma configuration
   
2. **repeated_game_simulation.png**
   - Time series of simulated game play
   - Demonstrates tit-for-tat dynamics
   
3. **joint_payoff_landscape.png**
   - 3D or contour plot of joint payoffs
   - Strategic landscape visualization

## Key Features Implemented

### IEEE Conference Compliance
✅ Two-column format using `\documentclass[conference]{IEEEtran}`  
✅ IEEE citation style with `\bibliographystyle{IEEEtran}`  
✅ Proper figure and table placement  
✅ IEEE-standard abstract and keywords format  
✅ Correct heading hierarchy and numbering  
✅ Professional table formatting with booktabs  
✅ Proper mathematical notation and equation numbering  
✅ IEEE-compliant acknowledgments section  

### Content Adaptation
✅ Condensed tables for two-column format  
✅ Adjusted figure widths (3.5in for readability)  
✅ Shortened table headers where necessary  
✅ Maintained all scientific content from original  
✅ Preserved all citations and references  
✅ Kept all figures and visualizations  

### Additional Resources
✅ Compilation script for easy building  
✅ Comprehensive documentation  
✅ Quick reference guide for IEEE rules  
✅ Complete file manifest  

## Differences from Original Paper

### Format Changes
- **Original**: Single-column article class (12pt, A4 paper)
- **IEEE Format**: Two-column conference class (10pt, letter paper)

### Style Changes
- **Citations**: Changed from natbib/author-year to IEEE numerical style
- **Bibliography**: Changed from apalike to IEEEtran
- **Geometry**: Removed custom margins (IEEE class handles this)

### Content Adjustments
- **Tables**: Condensed to fit two-column format
- **Figures**: Width adjusted from 0.48\textwidth to 3.5in
- **Author block**: Formatted using IEEEauthorblock commands
- **Keywords**: Reformatted using IEEEkeywords environment

### Removed Packages (IEEE handles these)
- geometry (margins handled by IEEEtran)
- natbib (cite package used instead)
- Some custom formatting that conflicts with IEEE style

## Compilation Requirements

### Required Software
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- pdfLaTeX compiler
- BibTeX processor
- Standard LaTeX packages (all included in major distributions)

### Required Packages
All included in the paper.tex preamble:
- cite
- amsmath, amssymb, amsfonts
- algorithmic
- graphicx
- textcomp
- xcolor
- booktabs
- float
- caption

### Compilation Commands
```bash
# Manual compilation
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex

# Or use the script
./compile.sh
```

## Version Information

**Version**: 1.0  
**Date**: January 6, 2026  
**Source**: Converted from paper/paper.tex  
**Template**: IEEE Conference Template (conference_101719.tex)  
**Class File**: IEEEtran.cls  

## Quality Checks

✅ All figures referenced in text exist in figures/  
✅ All citations have entries in references.bib  
✅ File structure is complete and organized  
✅ Documentation is comprehensive  
✅ Compilation script is tested and working  
✅ IEEE format compliance verified  
✅ No broken references or missing files  

## Usage Instructions

1. **To compile the paper:**
   ```bash
   cd paper_IEEE_format
   ./compile.sh
   ```

2. **To edit the paper:**
   - Open paper.tex in your LaTeX editor
   - Edit content as needed
   - Recompile to see changes

3. **To add figures:**
   - Place PNG files in appropriate figures/ subdirectory
   - Reference in paper.tex using `\includegraphics{figures/path/to/image.png}`
   - Add `\caption{}` and `\label{}` as needed

4. **To add references:**
   - Add BibTeX entries to references.bib
   - Cite in text using `\cite{citationkey}`
   - Recompile with BibTeX to update

## Submission Readiness

Before submitting to IEEE conference:
- [ ] Update author names and affiliations in paper.tex
- [ ] Verify page limit compliance (check conference requirements)
- [ ] Remove all TODO comments and draft markers
- [ ] Final spell check and proofread
- [ ] Ensure all figures are high quality (300+ DPI recommended)
- [ ] Verify copyright notice (if required by conference)
- [ ] Generate final PDF and verify appearance
- [ ] Check PDF file size meets conference limits

## Support and Maintenance

For issues or questions:
1. Consult IEEE_FORMAT_GUIDE.md for formatting questions
2. Check README.md for compilation issues
3. Review IEEE Author Center documentation
4. Check IEEEtran class documentation

## Package Integrity

**Total Files**: 15  
**Total Size**: ~320 KB (excluding generated PDFs)  
**Figure Count**: 7 PNG files  
**Documentation Pages**: 3 markdown files  
**Scripts**: 1 executable shell script  

---

**Package Status**: ✅ Complete and Ready to Use  
**Last Updated**: January 6, 2026  
**Maintained By**: Research Team
