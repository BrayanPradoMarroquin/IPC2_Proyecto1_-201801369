from listadatos import listados


def forsecond(ruta, lista):
    for sub in ruta:
        lista.agregarnodo(sub.text, sub.get("x"), sub.get("y"))
        print(sub.text + " " + sub.get("x") + " " + sub.get("y"))

class nodoMatriz:

    def __init__(self, nombreM, fila, columna, ruta):
        self.lista = listados()
        self.nombreM = nombreM
        self.fila = fila
        self.columna = columna
        self.ruta = ruta
        self.next= None
        if self.ruta!=0:
            forsecond(self.ruta, self.lista)

    def imprmir(self):
        self.lista.imprimir()

