from listadatos import listados

lista = listados
class nodoMatriz:

    def __init__(self, nombreM, fila, columna):
        self.nombreM = nombreM
        self.fila = fila
        self.columna = columna
        self.next= None
        lista.agregarnodo()

    def getElemento(self):
        return  self.nombreM+" "+self.fila+" "+self.columna