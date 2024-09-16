import os
import re
import base64
import glob
import numpy as np

from Foundation import NSPropertyListSerialization, NSData


mainfile = os.path.join(os.environ["HOME"], "Documents", "TexStuff", "Main.bib")
paperpath = os.path.join(os.environ["HOME"], "Documents", "Papers")

with open(mainfile) as f:
    bib = f.read()

aliases = re.findall(r"bdsk-file-\d = {(\S*)}", bib)

files = []
for a in aliases:
    tmp = base64.b64decode(a.encode())
    files.append(
        os.path.join(
            paperpath, re.search(b"Papers/(.+?)(?=O\x11)", tmp).groups()[0].decode()
        )
    )


diskfiles = glob.glob(os.path.join(paperpath, "*.*"))


set(files) - set(diskfiles)

missing = list(set(diskfiles) - set(files))
np.sort(missing)


files = []
for a in aliases:
    decodedBytes = base64.b64decode(a)
    nsData = NSData.dataWithBytes_length_(decodedBytes, len(decodedBytes))
    (
        plist,
        fmt,
        error,
    ) = NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_(
        nsData, 0, None, None
    )
    files.append(os.path.join(paperpath, os.path.split(plist["relativePath"])[-1]))
