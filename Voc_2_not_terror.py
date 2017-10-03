import xml.etree.ElementTree as ET
import os

path  = os.listdir('Annotations')
for name in path:
    filename = os.path.join('Annotations',name)
    tree = ET.parse(filename)
    objs = tree.findall('object')
    for ix, obj in enumerate(objs):
        obj.find('name').text = 'not terror'
   
    tree.write(os.path.join('new_Annotations',name))
