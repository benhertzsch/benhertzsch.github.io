pandoc -o contents/about.html  contents/about.md
pandoc -o contents/research.html contents/research.md
pandoc -o contents/publications.html contents/publications.md
pandoc -o contents/notes.html contents/notes.md

pandoc -o notes/catastrophe_theory/catastrophe_theory.html notes/catastrophe_theory/catastrophe_theory.md


python script.py