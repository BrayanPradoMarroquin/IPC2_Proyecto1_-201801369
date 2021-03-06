#nodo con los datos ya ordenados
class nodordenlist:

    def __init__(self, dato, binario, fila):
        self.dato=dato
        self.binario = binario
        self.fila = fila
        self.next=None
        print("El dato: "+str(self.dato)+" tiene valor binario: "+str(self.binario)+" la cual esta en la fila: "+str(self.fila))

