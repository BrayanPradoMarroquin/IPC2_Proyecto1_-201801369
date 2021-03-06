import  xml.etree.ElementTree as ET
import metodosI
import os
import grafogenerar
from listanombre import listanombre
from lista import listanombres
listado = listanombre()
listamatriz = listanombres()
comparacion1 = True
comparacion2 = True
cont=0
#crear grafo de la matriz
def crearnodo(nombre, matriz, lista):
        fila = matriz.fila
        columna = matriz.columna
        print(nombre+ " con "+fila+" filas y "+columna+" columnas")
        grafogenerar.generargrafo(nombre, fila, columna, lista)
#ordenar las matrices
def enviarlista(listag, nombreMatriz, fila, columna):
        listado.agregarnodo(nombreMatriz)
        for i in range(1, (int(fila)+1)):
                listado.buscarnombre(nombreMatriz, i)
                for j in range(1,(int(columna)+1)):
                        binario = listag.buscardatocomparar(i, j)
                        valor = listag.buscardatobasegrafo(i, j)
                        listado.buscarnombrematriz(nombreMatriz, i, binario, valor)

def comparacion(bin1, bin2):
        if (bin1==bin2):
                return  True
        else:
                return False
#recorrer las filas descomprimidas
def nombrematriz(nombre, x, y):
        lista = listado.buscarnombrelist(nombre)
        listamatriz.agregarnodo(nombre, 0 , 0, 0)
        matriz = listamatriz.buscarnodomatriz(nombre)
        listaoperando = matriz.lista
        print(nombre)
        listad = lista.listad
        for i1 in range(1,(int(x)+1)):
                lista1 = listad.buscarnododato(i1)
                listanodos1 = lista1.lista
                for i2 in range(1,int(x)+1):
                        if i1!=i2:
                                lista2 = listad.buscarnododato(i2)
                                listanodos2 = lista2.lista
                                comparacion1 = True
                                cont=0
                                for j in range(1,(int(y)+1)):
                                        if (comparacion1!=False):
                                                databin1 = listanodos1.recorrerlistabinario(j)
                                                databin2 = listanodos2.recorrerlistabinario(j)
                                                data1 = listanodos1.recorrerlistadato(j)
                                                data2 = listanodos2.recorrerlistadato(j)
                                                comparacion2 = comparacion(databin1, databin2)
                                                comparacion0=comparacion1
                                                comparacion1=comparacion2
                                                if (comparacion1!=comparacion0):
                                                        comparacion1=False
                                                        t=0
                                                        if listaoperando.vacio()!=True:
                                                                while (t!=(int(cont))):
                                                                        operacion = listaoperando.eliminarnodo(i1)
                                                                        t=t+1
                                                else:
                                                        suma = int(data1) + int(data2)
                                                        cont=cont+1
                                                        listaoperando.agregarnodo(str(suma), str(i1), str(j))
                                        print("dato 1 es: "+ str(data1)+ " y el dato 2 es: "+str(data2))
#escribir archivo xml final
def creararchivo(ruta, listabase):
        data = ET.Element('matrices')
        for elem in ruta:
                datos = listamatriz.buscarnodomatriz(elem.get("nombre"))
                base = listabase.buscarnodomatriz(elem.get("nombre"))
                valores = datos.lista
                if valores.cabeza==None:
                        valores=base.lista
                matriz = ET.SubElement(data, "matriz", attrib={})
                matriz.set('name',datos.nombreM)
                #matriz.set('n= ', datos.fila)
                #matriz.set('m= ', datos.columna)
                for i in range(1, (int(elem.get("n"))+1)):
                        for j in range(1, (int(elem.get("m"))+1)):
                                valor = ET.SubElement(matriz, "dato", attrib={})
                                val = valores.buscardatobase(i, j)
                                valor.set('x',val.fila)
                                valor.text = val.valor
        mydata = ET.tostring(data)
        myfile = open("resultado.xml", "w")
        myfile.write(str(mydata))