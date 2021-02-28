def suma(valor1, valor2):
    return int(valor1)+int(valor2)

class nodosuma:

    def __init__(self, binario1, binario2, valor1, valor2, j):
        self.binario1 = binario1
        self.binario2 = binario2
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor = j
        self.suma = suma(valor1,valor2)
        self.next=None

