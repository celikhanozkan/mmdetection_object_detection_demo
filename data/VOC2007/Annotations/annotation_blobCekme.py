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
    for member in root.findall("object"):
        
        if cnt == 0 :
            member[0].text = 'urun2'
            classes_names.append(member[0].text)
        else:
            member[0].text = 'urun'
            classes_names.append(member[0].text)
        for blob in member.findall("bndbox"):
            blob[0].text = str(round(int(blob[0].text) * (1024 / 800)))
            blob[2].text = str(round(int(blob[2].text) * (1024 / 800)))
            blob[1].text = str(round(int(blob[1].text) * (768 / 600)))
            blob[3].text = str(round(int(blob[3].text) * (768 / 600)))
            print(blob[0].text,'blobCoordinates')
        cnt += 1
    tree.write(xml_file)  
classes_names = list(set(classes_names))
classes_names.sort()
print(classes_names)
