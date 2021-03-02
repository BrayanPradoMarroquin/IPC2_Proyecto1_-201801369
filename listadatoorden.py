from nododatoorden import nodordenlist

nodo = nodordenlist

class lista_dato_orden:

    def __init__(self):
        self.cabeza = None

    def vacio(self):
        if self.cabeza==None:
            return True

    def agregarnodo(self, dato, binario, fila):
        nuevo = nodo(dato, binario, fila)
        if self.vacio()==True:
            self.cabeza=nuevo
        else:
            nuevo.next = self.cabeza
            self.cabeza = nuevo

    def recorrerlistabinario(self, recorrido):
        nuevo = self.cabeza
        cont = 0
        while (cont!=(int(recorrido)-1)):
            nuevo = nuevo.next
            cont +=1
        return nuevo.binario

    def recorrerlistadato(self, recorrido):
        nuevo = self.cabeza
        cont = 0
        while (cont!=(int(recorrido)-1)):
            nuevo = nuevo.next
            cont +=1
        return nuevo.dato