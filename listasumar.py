from nodosumar import nodosuma

nodo = nodosuma

class listasuma:

    def __init__(self):
        self.cabeza=None

    def vacio(self):
        if self.cabeza==None:
            return  True

    def agregarnodo(self,binario1, binario2, valor1, valor2, j):
        nuevo = nodo(binario1, binario2, valor1, valor2, j)
        if self.vacio()==True:
            self.cabeza=nuevo
        else:
            nuevo.next=self.cabeza
            self.cabeza=nuevo
