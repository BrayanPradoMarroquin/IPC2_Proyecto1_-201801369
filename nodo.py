from listadatos import listados

lista = listados()

def forsecond(ruta):
    for sub in ruta:
        lista.agregarnodo(sub.text, sub.get("x"), sub.get("y"))
        print(sub.text + " " + sub.get("x") + " " + sub.get("y"))

class nodoMatriz:

    def __init__(self, nombreM, fila, columna, ruta):
        self.nombreM = nombreM
        self.fila = fila
        self.columna = columna
        self.ruta = ruta
        self.next= None
        forsecond(self.ruta)

