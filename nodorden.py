class nodo_orden:

    def __init__(self, nombre):
        self.nombre = nombre
        self.next = None
        print("la fila es: "+str(self.nombre))