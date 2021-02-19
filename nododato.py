def matrizbinaria(valor):
    if int(valor)!=0:
        return 1
    else:
        return 0

class nododato:

    def __init__(self, valor, fila, columna):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.next = None
        self.binario= valorbinario=matrizbinaria(self.valor)

