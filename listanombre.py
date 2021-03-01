from nodonombre import nodonombre
nodo = nodonombre

class listanombre:

    def __init__(self):
        self.cabeza = None

    def vacio(self):
        if self.cabeza==None:
           return True

    def agregarnodo(self, nombre):
        nuevo = nodo(nombre)
        if self.vacio()==True:
            self.cabeza=nuevo
        else:
            nuevo.next=self.cabeza
            self.cabeza=nuevo

    def buscarnombre(self, nombre, nombrebase):
        nuevo = self.cabeza
        while (nuevo.nombre != nombre):
            if (nuevo != None):
                nuevo = nuevo.next
                if (nuevo == None):
                    return 0
        nuevo.enviarnombre(nombrebase)

    def buscarnombrematriz(self, nombre, nombrefila, datobinario, datovalor):
        nuevo = self.cabeza
        while (nuevo.nombre!=nombre):
            if (nuevo!=None):
                nuevo = nuevo.next
                if (nuevo==None):
                    return 0
        nuevo.enviarfilas(nombrefila, datobinario, datovalor)