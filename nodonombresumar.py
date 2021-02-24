from listasumar import listasuma


def listardatos(valor1, valor2, valorbase1, valorbase2, j, lista):
    lista.agregarnodo(valor1, valor2, valorbase1, valorbase2, j)


class nodonombre:

    def __init__(self, nombre, fila, columna):
        self.lista = listasuma()
        self.nombrematriz = nombre
        self.next = None

