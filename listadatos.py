from nododato import nododato

nodo = nododato

class listados:
    def __init__(self):
        self.cabeza=None
        self.cola = None

    def vacio(self):
        if self.cabeza==None:
            return True

    def agregarnodo(self, dato, fila, columna):
        nuevo = nodo(dato, fila, columna)
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