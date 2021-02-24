from nodonombresumar import nodonombre
import nodonombresumar
nodo = nodonombre

class listanombrebase:

    def __init__(self):
        self.cabeza=None

    def vacio(self):
        if self.cabeza==None:
            return True

    def agregarnododato(self, nombre, fila, columna):
        nuevo = nodo(nombre, fila, columna)
        if self.vacio()==True:
            self.cabeza=nuevo
        else:
            nuevo.next=self.cabeza
            self.cabeza=nuevo

    def buscar(self, val1, val2, base1, base2, j, nombrex):
        nuevo = self.cabeza
        while (nuevo!=None) and (nuevo.nombrematriz!=nombrex):
            nuevo=nuevo.next
        nodonombresumar.listardatos(val1, val2, base1, base2, j, nuevo.lista)