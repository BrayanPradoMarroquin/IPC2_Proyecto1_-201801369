import metodosI
import grafogenerar
from listanombre import listanombre

listado = listanombre()

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
                        print(str(binario) + " valor -> "+str(valor)+ " fila: "+str(i)+" Columna: "+str(j))

