# QUICK REFERENCE GUIDE - PFE REPORT FORMATTING

## Standardized Formatting Templates

### For New Sections
```latex
% ═════════════════════════════════════════════════════════════════════════════
\section{\textcolor[HTML]{0066CC}{Your Section Title}}
\label{sec:yourlabel}
% ═════════════════════════════════════════════════════════════════════════════

Content here...

\vspace{0.3cm}

\subsection*{\textcolor[HTML]{003D99}{Your Subsection Title}}

More content...
```

### For Figures
```latex
\begin{figure}[H]
  \centering
  \includegraphics[width=0.75\textwidth]{images_pfe/yourimage.png}
  \caption{Your descriptive caption here.}
  \label{fig:yourlabel}
\end{figure}
\FloatBarrier
```

### For Tables
```latex
\begin{table}[H]
\centering
\small
\setlength{\tabcolsep}{8pt}
\renewcommand{\arraystretch}{2.0}
\caption{Your table caption here.}
\label{tab:yourlabel}
\begin{tabularx}{\textwidth}{|X|X|X|}
\hline
\textcolor[HTML]{003D99}{\textbf{Column 1}} & 
\textcolor[HTML]{003D99}{\textbf{Column 2}} & 
\textcolor[HTML]{003D99}{\textbf{Column 3}} \\
\hline
Data 1 & Data 2 & Data 3 \\
\hline
\end{tabularx}
\end{table}
\FloatBarrier
```

### Spacing Rules
- **Between paragraphs:** `\vspace{0.3cm}`
- **Before major sections:** `\vspace{0.5cm}`
- **After figures/tables:** `\FloatBarrier`
- **Avoid:** Using `\\` for spacing

### Color Palette
- **Sections:** `#0066CC` (Primary Blue)
- **Subsections:** `#003D99` (Dark Blue)
- **Table headers:** `#003366` (Navy) or `#003D99`
- **Backgrounds:** `#E6F2FF`, `#F5F5F5` (Light tones)
- **Status colors:**
  - Success: `#006600` (Green)
  - Warning: `#CC6600` (Orange)
  - Error: `#CC0000` (Red)

### Chapter Structure
```latex
% ═════════════════════════════════════════════════════════════════════════════
% CHAPTER: Your Chapter Name
% ═════════════════════════════════════════════════════════════════════════════

\chapter{Your Chapter Title}
\label{chap:yourlabel}

% Content sections follow...
```

## File Organization

```
main.tex                     → Main document
├─ Front Matter
│  ├─ 01-Dedicace.tex       → Dedication
│  ├─ 02-Remerciements.tex  → Acknowledgments
│  ├─ 03-Resume.tex         → Abstract
│  └─ 04-Acronymes.tex      → Acronyms
├─ Main Chapters
│  ├─ 05-Introduction.tex
│  ├─ 05b-Entreprise.tex
│  ├─ 06-Art.tex
│  ├─ 09-Conception-ENGLISH.tex
│  ├─ 10-Implementation-EN.tex
│  ├─ 09-Results.tex
│  ├─ 10-Realisation.tex
│  ├─ 10-Discussion.tex
│  └─ 11-Conclusion.tex
└─ Back Matter
   └─ 12-Annexe.tex         → Appendices
```

## Compilation Commands

```bash
# Standard compilation
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex

# Or use latexmk
latexmk -pdf -synctex=1 main.tex
```

## Cross-References

Use consistent labeling:
- Chapters: `\label{chap:name}` → `\ref{chap:name}` or `Chapter~\ref{chap:name}`
- Sections: `\label{sec:name}` → `\ref{sec:name}` or `Section~\ref{sec:name}`
- Figures: `\label{fig:name}` → `\ref{fig:name}` or `Figure~\ref{fig:name}`
- Tables: `\label{tab:name}` → `\ref{tab:name}` or `Table~\ref{tab:name}`

## Common Patterns

### Itemized Lists
```latex
\begin{itemize}
  \item First point
  \item Second point
  \item Third point
\end{itemize}
```

### Enumerated Lists
```latex
\begin{enumerate}
  \item First step
  \item Second step
  \item Third step
\end{enumerate}
```

### Emphasized Text
```latex
\textbf{Bold text}
\textit{Italic text}
\textcolor[HTML]{0066CC}{\textbf{Colored bold text}}
```

---

**Last Updated:** May 26, 2026
**Status:** ✓ All files standardized
