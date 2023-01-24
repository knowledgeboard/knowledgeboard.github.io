#!/usr/bin/env python
import os
from typing import Literal

import sys

file = open(sys.argv[1])
lines = file.readlines()
file.close()

i = lines.index("LINKS\n")
PRE = lines[:i]
POST = lines[i+1:]

sources = [sys.argv[2:]][0]

list_item = '''<ul>
    <li>
        <a href="{}">{}</a>
    </li>
</ul>
'''

def itemParser(item:str):
    info, url = item.split("](") #)
    info = info[1:]
    url = url[:-2]

    return info, url

for source in sources:
    _f = open(source)
    items = _f.readlines()
    _f.close()

    out = open("{}.html".format(source[:-3].split("/")[1]), "w")

    out.writelines(PRE)
     
    for item in items:
        if item == "": continue

        info, url = itemParser(item)
        if url=="":
            continue
        out.write(list_item.format(url, info))

    out.writelines(POST)
    out.close()
