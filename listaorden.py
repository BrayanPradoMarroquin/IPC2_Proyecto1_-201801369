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

    def buscarnombre(self, nombrebase, datobinario, datovalor):
        nuevo = self.cabeza
        while (nuevo.nombre != nombrebase):
            if (nuevo != None):
                nuevo = nuevo.next
                if (nuevo == None):
                    return 0
        nuevo.enviarnombre(datobinario, datovalor, nombrebase)

    def buscarnododato(self, nombre):
        nuevo = self.cabeza
        while (nuevo.nombre!=nombre):
            if (nuevo!=None):
                nuevo = nuevo.next
                if (nuevo==None):
                    return 0
        return nuevo