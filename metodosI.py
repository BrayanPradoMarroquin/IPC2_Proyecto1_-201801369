import xml.etree.ElementTree as ET
from tkinter import *
from tkinter.filedialog import askopenfilename
import metodosiniciales
from lista import listanombres
from listanombresuma import listanombrebase
lsita = listanombres()
listasuma=listanombrebase()
root = Tk()
root.withdraw()
root.update()

def generar(ruta):
    tree = ET.parse(ruta)
    Raiz = tree.getroot()
    return Raiz

def llamararchivo():
    pathString = askopenfilename(filetypes=[("Text files", "*.xml")])
    if pathString=="":
        print("No a elegido ningun archivo, debe elegir uno para continuar")
        llamararchivo()
    else:
        ruta = generar(pathString)
    return ruta

def mostrardatos(Raiz):
    for elem in Raiz:
        lsita.agregarnodo(elem.get("nombre"), elem.get("n"), elem.get("m"), elem)
        print(elem.get("nombre")+" "+ elem.get("n")+" "+elem.get("m"))
        #listasuma.agregarnododato(elem.get("nombre"), elem.get("n"), elem.get("m"))

def comparar(Raiz):
    for rama in Raiz:
        respuesta = lsita.buscar(rama.get("nombre"), rama, rama.get("n"), rama.get("m"))

def imprimir():
    lsita.imprimir()

def grafo(matriz):
    if matriz!="":
        listadato = lsita.buscarnodomatriz(matriz)
        if (listadato!=0):
            nombre = listadato.nombreM
            listado = listadato.lista
            metodosiniciales.crearnodo(nombre, listadato, listado)
            print("Grafica generada correctamente")
        else:
            print("No se encontro la lista solicitada")

