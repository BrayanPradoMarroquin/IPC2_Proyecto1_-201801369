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

    def buscarnodo(self, ruta, x, y):
        for j in range(1,(int(y)+1)):
            for i in range(1,(int(x)+1)):
                if (i!=j):
                    valor1 = self.buscardato(j,j)
                    valor2 = self.buscardato(i,j)
                    print(str(valor1)+" || "+str(valor2))
                    valorbase1 = self.buscardatobase(j,j)
                    valorbase2 = self.buscardatobase(i,j)


    def imprimir(self):
        i = self.cabeza
        while i:
            print(i.valor + " -> ")
            i = i.next


