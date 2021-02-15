from nodo import nodoMatriz

nodo = nodoMatriz

class listanombres:

    def __init__(self):
        self.cabeza=None
        self.cola = None

    def vacio(self):
        if self.cabeza==None:
            return True

    def agregarnodo(self, nombre, fila, columna):
        nuevo = nodo(nombre, fila, columna)
        if self.vacio()==True:
            self.cabeza=self.cola=nuevo
        else:
            nuevo.next=self.cola
            self.cabeza=nuevo

    def nodoprimero(self):
        if self.vacio()==True:
            return ("Lista Vacia")
        else:
            return self.cabeza



    #def imprimir(self):
    #    if self.vacio()==True:
    #        print("Lista Vacia")
    #    else:
    #        validar=True
    #        temp = self.cabeza
    #        while(validar):
    #            print(temp.getElemento())
    #            if temp==self.cola:
    #                validar=False
    #            else:
    #                temp=temp.next