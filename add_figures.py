with open("10-Implementation-EN.tex", "r", encoding="utf-8") as f:
    content = f.read()

# Find the position to insert (after \end{enumerate} in the update section)
search_text = "\item \textbf{Confirm to user}: LEON confirms: ``Done. John Doe is now DRE for External mirrors in J4U.''\n\end{enumerate}"

new_figures = """

\vspace{0.3cm}

\noindent\textbf{Update workflow visualization:}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.46\textwidth]{images_pfe/Component input.png}\hfill
    \includegraphics[width=0.46\textwidth]{images_pfe/question role.png}
    \caption{Component selection and role confirmation workflow.}
    \label{fig:workflow-io}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.46\textwidth]{images_pfe/update name1.png}\hfill
    \includegraphics[width=0.46\textwidth]{images_pfe/update name2.png}
    \caption{Confirmation prompt and Excel update execution workflow.}
    \label{fig:workflow-exec}
\end{figure}"""

if search_text in content:
    content = content.replace(search_text, search_text + new_figures)
    with open("10-Implementation-EN.tex", "w", encoding="utf-8") as f:
        f.write(content)
    print("Figures added successfully")
else:
    print("Search text not found")
