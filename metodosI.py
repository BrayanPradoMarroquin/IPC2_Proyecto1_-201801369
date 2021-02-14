import xml.etree.ElementTree as ET



def llamararchivo():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse('prueba.xml')
    prueba = tree.getroot()
    print(prueba)
