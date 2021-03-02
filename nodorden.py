from listadatoorden import lista_dato_orden
#nodo de las listas de las filas
class nodo_orden:

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = lista_dato_orden()
        self.next = None

    def enviarnombre(self, datobinario, datovalor, nombrebase):
        self.lista.agregarnodo(datovalor, datobinario, nombrebase)