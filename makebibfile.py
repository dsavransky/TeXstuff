import os
import glob
import re
mainfile = os.path.join(os.environ['HOME'],'Documents','TexStuff','Main.bib')

fname = glob.glob('*.bbl')[0]
with open(fname) as f:
    bbl = f.read()
citekeys = re.findall("\\\entry{([^\s}]*)}", bbl)

## doesn't work - screws up character escapes.
#from pybtex.database import parse_file, BibliographyData, Entry
#bib_data = parse_file(mainfile)
#
#out = BibliographyData()
#for key in citekeys:
#    out.add_entry(key,bib_data.entries[key])
#
#out.to_file('local.bib')


# trying with bibtool instead
import subprocess

with open('local.bib','wb') as f:
    for key in citekeys:
        f.write(subprocess.run(["bibtool", '--select {{"{}"}}'.format(key), mainfile],
                    cwd=os.path.curdir, check=True, capture_output=True).stdout)


