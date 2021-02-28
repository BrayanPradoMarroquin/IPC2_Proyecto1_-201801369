import metodosI
import grafogenerar

def listasumarllamar(val1, val2, base1, base2, j, nombrematriz):
        metodosI.listasuma.buscar(val1, val2, base1, base2, j, nombrematriz)


def crearnodo(nombre, matriz, lista):
        fila = matriz.fila
        columna = matriz.columna
        print(nombre+ " con "+fila+" filas y "+columna+" columnas")
        grafogenerar.generargrafo(nombre, fila, columna, lista)

