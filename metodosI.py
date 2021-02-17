import xml.etree.ElementTree as ET
from tkinter import *
from tkinter.filedialog import askopenfilename
from lista import listanombres
lsita = listanombres()
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
        print(elem.get("nombre") + " " + elem.get("n")+ " "+ elem.get("m"))
        lsita.agregarnodo(elem.get("nombre"), elem.get("n"), elem.get("m"), elem)


