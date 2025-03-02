pandoc -o contents/about.html  contents/about.md
pandoc -o contents/research.html contents/research.md
pandoc -o contents/publications.html contents/publications.md
pandoc -o contents/notes.html contents/notes.md

#pandoc --mathjax -f markdown -t html5 notes/catastrophe_theory/catastrophe_theory.md -o notes/catastrophe_theory/catastrophe_theory.html
pandoc notes/catastrophe_theory/catastrophe_theory.md -s --mathjax -t html5 -o notes/catastrophe_theory/catastrophe_theory.html

#pandoc notes/catastrophe_theory/catastrophe_theory.md --css css/style_notes.css -s --mathjax -t html5 -o catastrophe_theory.html



python script.py