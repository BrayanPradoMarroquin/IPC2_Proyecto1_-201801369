from nodorden import nodo_orden
nodo = nodo_orden

class listado_orden:

    def __init__(self):
        self.cabeza = None

    def vacio(self):
        if self.cabeza==None:
            return True

    def agregarnodo(self, nombre):
        nuevo=nodo(nombre)
        if self.vacio()==True:
            self.cabeza=nuevo
        else:
            nuevo.next=self.cabeza
            self.cabeza=nuevo