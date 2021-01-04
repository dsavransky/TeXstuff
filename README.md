# TeXstuff
Useful TeX, LaTeX and BibTeX things

Personal usage notes:
    mkdir -p ~/Library/texmf/bibtex/bst/
    mkdir -p ~/Library/texmf/bibtex/bib/
    mkdir -p ~/Library/texmf/tex/latex/

    ln -s $HOME/Documents/TeXstuff/bst ~/Library/texmf/bibtex/bst/mybst 
    ln -s $HOME/Documents/TeXstuff/sty ~/Library/texmf/tex/latex/mysty
    ln -s $HOME/Documents/TeXstuff/Main.bib ~/Library/texmf/bibtex/bib/
    ln -s $HOME/Documents/TeXstuff/images ~/Library/texmf/tex/latex/  #sig goes in there too

Engines go in ~/Library/TeXShop/Engines/
bin/latexmkrcshell goes in ~/Library/TeXShop/Engines/ (this is just a reminder - should just do a straight copy of the current latexmkrcedit in there and enable shell.


Bibdesk migration:
copy:
~/Library/Application Support/BibDesk/
~/Library/Preferences/edu.ucsd.cs.mmccrack.bibdesk.plist 

may be needed:
defaults read ~/Library/Preferences/edu.ucsd.cs.mmccrack.bibdesk.plist
