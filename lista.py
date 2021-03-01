from nodo import nodoMatriz

nodo = nodoMatriz

class listanombres:

    def __init__(self):
        self.cabeza=None
        self.cola = None

    def vacio(self):
        if self.cabeza==None:
            return True

    def agregarnodo(self, nombre, fila, columna, ruta):
        nuevo = nodo(nombre, fila, columna, ruta)
        if self.vacio()==True:
            self.cabeza=nuevo
        else:
            nuevo.next=self.cabeza
            self.cabeza=nuevo

    def nodoprimero(self):
        if self.vacio()==True:
            return ("Lista Vacia")
        else:
            return self.cabeza

    def imprimir(self):
        i = self.cabeza
        while i:
            print(i.nombreM+ " -> ")
            #self.imprimir_valores()
            i=i.next

    def imprimir_valores(self):
        self.cabeza.imprmir()

    def buscarnodomatriz(self, nombre):
        nuevo = self.cabeza
        while (nuevo.nombreM!=nombre):
            if (nuevo != None):
                nuevo=nuevo.next
                if (nuevo==None):
                    return 0
        return nuevo