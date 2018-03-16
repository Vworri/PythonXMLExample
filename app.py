import os
from xml.etree import ElementTree
import json

filename = "nasa.xml"
full_path = os.path.abspath(os.path.join("data", filename))

data = []
dom = ElementTree.parse(full_path)

elems = dom.findall("dataset")

for e in elems:
    el = {}
    el["title"] = e.find("title").text
    try:
        el["desc"] = e.find("descriptions/description/para").text
    except AttributeError:
        el["desc"] = None
    el["auth"] = [(x.find("inital") +" "+ x.find("lastname") )for x in   e.findall("author")]
    data.append(el)
data = json.dumps(data, indent=4)
print(data)
    