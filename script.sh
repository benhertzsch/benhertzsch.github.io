pandoc -o contents/about.html  contents/about.md
pandoc -o contents/research.html contents/research.md
pandoc -o contents/publications.html contents/publications.md
pandoc -o contents/notes.html contents/notes.md

#pandoc --standalone --mathjax -f markdown -t html notes/catastrophe_theory/catastrophe_theory.md -o notes/catastrophe_theory/catastrophe_theory.html
pandoc notes/catastrophe_theory/catastrophe_theory.md -o notes/catastrophe_theory/catastrophe_theory.html


python script.py