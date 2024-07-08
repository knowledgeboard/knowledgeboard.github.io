#!/usr/bin/env python

from __future__ import annotations

import os
import subprocess

import sys
import re

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

blog_item = '''<div class="blog">
{}
</div>
'''

def itemParser(item:str):
    try:
        info, url = item.split("](") #)
    except:
        return "",""

    info = info[1:]
    url = url[:-2]

    return info, url

def findAndReplace(item:list[str], replace:str):
    # print(item)
    s = "".join(item)
    replaced = re.sub("@TITLE@", replace, s)
    s_split = replaced.split("\n") 
    print(s_split)
    quit()
    return s_split

for source in sources:
    name = source[:-3].split("/")[1]
    if source.endswith("blog.md"):
        out = open(f"{name}.html", "w")
        out.writelines(findAndReplace(PRE, "Blog"))
        blog_text = subprocess.Popen(["markdown", source],
                                     stdout=subprocess.PIPE).communicate()[0]
        blog_text = blog_text.decode()
        out.write(blog_item.format(blog_text))
        out.writelines(POST)
        out.close()
    else:
        _f = open(source)
        items = _f.readlines()
        _f.close()

        out = open("{}.html".format(name, "w"))

        out.writelines(findAndReplace(PRE, name))
        
        for item in items:
            if item == "": continue

            info, url = itemParser(item)
            if url=="":
                continue
            out.write(list_item.format(url, info))

        out.writelines(POST)
        out.close()
