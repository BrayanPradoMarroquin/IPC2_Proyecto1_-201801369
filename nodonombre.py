from listaorden import listado_orden
#nodo del nombre de la matriz
class nodonombre:

    def __init__(self, nombre):
        self.nombre = nombre
        self.next = None
        self.listad = listado_orden()
        print(self.nombre)
#nombre de la fila
    def enviarnombre(self, nombre):
        self.listad.agregarnodo(nombre)
#enviar datos a la lsita de datos
    def enviarfilas(self, nombrefila, datobinario, datovalor):
        self.listad.buscarnombre(nombrefila, datobinario, datovalor)