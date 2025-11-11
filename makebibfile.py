import os
import glob
import re
import subprocess

mainfile = os.path.join(os.environ["HOME"], "Documents", "TexStuff", "Main.bib")
localfile = "local.bib"

# get all citations from bbl
fname = glob.glob("*.bbl")[0]
with open(fname) as f:
    bbl = f.read()
citekeys = re.findall(r"\\entry{([^\s}]*)}", bbl)
# citekeys = re.findall("\\\entry{([^\s}]*)}", bbl)
# citekeys = re.findall("bibitem{([^\s}]*)}", bbl)


if os.path.exists(localfile):
    with open(localfile) as f:
        lcl = f.read()
    # lclkeys = re.findall("@[^\s^{]*{\s*([^\s,]*),",lcl)
    lclkeys = re.findall(r"@[^\s^{]*{\s*([^\s,]*),", lcl)
    citekeys = list(set(citekeys) - set(lclkeys))

if len(citekeys) > 0:
    with open("local.bib", "ab") as f:
        for key in citekeys:
            f.write(
                subprocess.run(
                    ["bibtool", '--select {{"{}"}}'.format(key), mainfile],
                    cwd=os.path.curdir,
                    check=True,
                    capture_output=True,
                ).stdout
            )


## doesn't work - screws up character escapes.
# from pybtex.database import parse_file, BibliographyData, Entry
# bib_data = parse_file(mainfile)
#
# out = BibliographyData()
# for key in citekeys:
#    out.add_entry(key,bib_data.entries[key])
#
# out.to_file('local.bib')
