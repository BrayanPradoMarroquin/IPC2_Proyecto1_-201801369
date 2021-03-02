import metodosI
import grafogenerar
from listanombre import listanombre

listado = listanombre()
comparacion1 = True
comparacion2 = True
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
        print(nombre)
        listad = lista.listad
        for i1 in range(1,(int(x)+1)):
                lista1 = listad.buscarnododato(i1)
                listanodos1 = lista1.lista
                for i2 in range(1,int(x)+1):
                        if i1!=i2:
                                lista2 = listad.buscarnododato(i2)
                                listanodos2 = lista2.lista
                                for j in range(1,(int(y)+1)):
                                        databin1 = listanodos1.recorrerlistabinario(j)
                                        databin2 = listanodos2.recorrerlistabinario(j)
                                        data1 = listanodos1.recorrerlistadato(j)
                                        data2 = listanodos2.recorrerlistadato(j)
                                        #comparacion2 = comparacion(databin1, databin2)
                                        #comparacion1=comparacion2
                                        print("dato 1 es: "+ str(data1)+ " y el dato 2 es: "+str(data2))
