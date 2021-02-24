def comparar(binario1, binario2):
    if int(binario1)==int(binario2):
        return True


def suma(valor1, valor2):
    return int(valor1)+int(valor2)


class nodosuma:

    def __init__(self, binario1, binario2, valor1, valor2):
        self.binario1 = binario1
        self.binario2 = binario2
        self.valor1 = valor1
        self.valor2 = valor2
        self.suma = suma(valor1,valor2)
        self.comparacion = comparar(binario1, binario2)

