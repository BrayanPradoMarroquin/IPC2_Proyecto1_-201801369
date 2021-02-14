import xml.etree.ElementTree as ET
from tkinter import *
from tkinter.filedialog import askopenfilename

def generar(ruta):
    tree = ET.parse(ruta)
    Raiz = tree.getroot()
    print(Raiz)

def llamararchivo():
    root = Tk()
    root.withdraw()
    root.update()
    pathString = askopenfilename(filetypes=[("Text files", "*.xml")])
    generar(pathString)

