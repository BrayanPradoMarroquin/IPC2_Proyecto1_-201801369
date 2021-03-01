from listaorden import listado_orden

class nodonombre:

    def __init__(self, nombre):
        self.nombre = nombre
        self.next = None
        self.listad = listado_orden()
        print(self.nombre)

    def enviarnombre(self, nombre):
        self.listad.agregarnodo(nombre)