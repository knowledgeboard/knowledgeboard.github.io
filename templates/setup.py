#!/usr/bin/env python
import os
import subprocess

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

for source in sources:
    if source.endswith("blog.md"):
        name = source[:-3].split("/")[1]
        out = open(f"{name}.html", "w")
        out.writelines(PRE)
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
