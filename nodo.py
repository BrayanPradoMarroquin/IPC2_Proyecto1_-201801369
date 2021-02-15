class nodoMatriz:

    def __init__(self, nombreM, fila, columna):
        self.nombreM = nombreM
        self.fila = fila
        self.columna = columna
        self.next= None

    def getElemento(self):
        return  self.elemento