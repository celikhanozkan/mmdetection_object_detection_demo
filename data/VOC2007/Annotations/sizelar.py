#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:23:52 2020

@author: celikhan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:13:49 2020

@author: celikhan
"""
import os
import glob
import xml.etree.ElementTree as ET
import numpy as np

rootPath = "home/celikhan/GeciciCarrefourRaf"
anno_path = os.path.join(rootPath, "Annotations_v2")

print(anno_path,'annoPath')
classes_names = []
xml_list = []
#print(glob.glob(anno_path + "/*.xml"))
for i in range(90):
    xml_file = '{}.xml'.format(i)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    cnt = 0
    for member in root.findall("size"):
        member[0].text = "1024"
        member[1].text = "768"
    tree.write(xml_file)  
classes_names = list(set(classes_names))
classes_names.sort()
print(classes_names)
