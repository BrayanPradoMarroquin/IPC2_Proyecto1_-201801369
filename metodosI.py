import xml.etree.ElementTree as ET
from tkinter import *
from tkinter.filedialog import askopenfilename
import metodosiniciales
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

def sobrelista(Raiz):
    print("Se estan buscando los datos")
    for elem in Raiz:
        listamatriz = lsita.buscarnodomatriz(elem.get("nombre"))
        listag = listamatriz.lista
        metodosiniciales.enviarlista(listag, listamatriz.nombreM, listamatriz.fila, listamatriz.columna)

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

def nombre(Raiz):
    for elem in Raiz:
        metodosiniciales.nombrematriz(elem.get("nombre"), elem.get("n"), elem.get("m"))

def creararchi(Raiz):
    metodosiniciales.creararchivo(Raiz, lsita)