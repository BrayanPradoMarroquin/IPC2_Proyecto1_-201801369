import xml.etree.ElementTree as ET
from tkinter import *
from tkinter.filedialog import askopenfilename
root = Tk()
root.withdraw()
root.update()

def generar(ruta):
    tree = ET.parse(ruta)
    Raiz = tree.getroot()
    return Raiz

def llamararchivo():
    pathString = askopenfilename(filetypes=[("Text files", "*.xml")])
    ruta = generar(pathString)
    return ruta

def mostrardatos(Raiz):
    for elem in Raiz:
        print(elem.attrib)
        for sub in elem:
            print(sub.attrib)