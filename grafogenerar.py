import metodosiniciales
import os

def generargrafo(nombre, filas, columnas, dato):
    file = open("grafo.dot", "w")
    file.write("digraph G { \n")
    file.write("Fil[label=\""+filas+"\"] \n")
    file.write(nombre+"-> filas -> Fil \n")
    file.write("Col[label=\"" + columnas + "\"] \n")
    file.write(nombre+"-> columnas -> Col \n")
    cont=0
    for i in range(1, int(columnas) + 1):
        y = i - 1
        for j in range(1, int(filas) + 1):
            if cont==0:
                if (j==1) & (y==0) | (y==1):
                    dato_ant = str(j-1)+str(y)
                    dat0 = str(dato.buscardatobasegrafo((j - 1), y))
                else:
                    dato_ant=dato_ant
                    dat0=dat0
            else:
                dato_ant = dato_ant
                dat0=dat0
            dato1 = str(j)+str(i)
            dat1= str(dato.buscardatobasegrafo(j, i))
            if (j== 1):
                file.write(dato1+"[label=\""+dat1+"\"] \n")
                file.write(nombre + "->" + dato1 + "\n")
                if (y==0):
                    y=1
                    dato_ant = dato1
                else:
                    dato_ant = dato1
                    dat0 = dat1
                    cont+=1
            else:
                file.write(dato1 + "[label=\"" + dat1 + "\"] \n")
                file.write(dato_ant + "->" + dato1 + "\n")
                dato_ant = dato1
                dat0 = dat1
    file.write("}")
    file.close()
    os.system('dot -Tpng grafo.dot -o grafo.png')
    os.startfile("grafo.png")

