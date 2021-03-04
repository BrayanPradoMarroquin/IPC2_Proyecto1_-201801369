from nododato import nododato

nodo = nododato

class listados:
    def __init__(self):
        self.cabeza=None
        self.cola = None

    def vacio(self):
        if self.cabeza==None:
            return  True

    def agregarnodo(self, dato, fila, columna):
        nuevo = nodo(dato, fila, columna)
        if self.vacio()==True:
            self.cabeza=nuevo
        else:
            nuevo.next=self.cabeza
            self.cabeza=nuevo

    def primernodo(self):
        if self.vacio()==True:
            return  ("Lista Vacia")
        else:
            return self.cabeza

    def buscardato(self, x, y):
        nuevo = self.cabeza
        while (nuevo!=None) :
                    if (nuevo.fila==str(x)) & (nuevo.columna==str(y)):
                        return nuevo.binario
                    nuevo=nuevo.next

    def buscardatobase(self, x, y):
        nuevo = self.cabeza
        while (nuevo != None):
            if (nuevo.fila == str(x)) & (nuevo.columna == str(y)):
                return nuevo.valor
            nuevo = nuevo.next

    def imprimir(self):
        i = self.cabeza
        while i:
            print(str(i.valor) + " -> ")
            i = i.next

    def buscardatobasegrafo(self, x, y):
        nuevo = self.cabeza
        while (nuevo != None):
            if (nuevo.fila == str(x)) & (nuevo.columna == str(y)):
                return nuevo.valor
            if (x==0) | (y==0):
                return 0
            nuevo = nuevo.next

    def buscardatocomparar(self, x, y):
        nuevo = self.cabeza
        while (nuevo != None):
            if (nuevo.fila == str(x)) & (nuevo.columna == str(y)):
                return nuevo.binario
            if (x==0) | (y==0):
                return 0
            nuevo = nuevo.next

    def eliminarnodo(self, fila):
        anterior = None
        while (self.cabeza.fila!=fila) & (self.cabeza!=None):
            anterior=self.cabeza
            self.cabeza=self.cabeza.next
        if (self.cabeza==None):
            print("valor no encontrado")
        else:
            if (anterior==None):
                self.cabeza=self.cabeza.next
            else:
                anterior.next=self.cabeza.next
        return "operacion completada"

    def buscardatobase(self, x, y):
        nuevo = self.cabeza
        while (nuevo != None):
            if (nuevo.fila == str(x)) & (nuevo.columna == str(y)):
                return nuevo
            nuevo = nuevo.next
