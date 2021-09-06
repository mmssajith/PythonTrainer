"""
# XML file editi
"""

import xml.etree.ElementTree as ET
import warnings

def idsMessage(xml, message):
  warnings.filterwarnings("ignore")

  tree = ET.ElementTree(ET.fromstring(xml))

  root = tree.getroot()

  idList = []

  for entry in root.iter('entry'):
    if list(entry.text) == (message):
      idList.append(int(entry.attrib["id"]))
  return idList

xml = """<?xml version="1.0" encoding="UTF-8"?>
<log>
  <entry id="1">
    <message>Application started</message>
  </entry>
  <entry id="2">
    <message>Application ended</message>
  </entry>
</log>
"""

print(idsMessage(xml, 'Application ended'))