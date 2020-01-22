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
    for member in root.findall("object"):
        temp = np.random.rand()
        if temp <= 0.5:
            member[0].text = 'urun1'
            classes_names.append(member[0].text)
        else:
            member[0].text = 'urun2'
            classes_names.append(member[0].text)
    tree.write(xml_file)    
classes_names = list(set(classes_names))
classes_names.sort()
print(classes_names)