import metodosI
valor=True
ruta=None
menu = """""
Menú
1. Cargue el archivo
2. Procesar el archivo
3. Escribir el archivo de Salida
4. Mostrar datos del estudiante
5. Generar grafica
6. Salir 
"""
#datos del alumno
def datos():
    print("Brayan Hamllelo Estevem Prado Marroquín")
    print("201801369")
    print("Introducción a la Programación y Computación 2 Sección D")
    print("Ingeniería en Ciencias y Sistemas")
    print("Cuarto Semestre")
#generador del menu
while valor==True:
    print(menu)
    opcion=int(input("Ingrese la opcion de la acción a realizar: \n"))
    if opcion==1:
        ruta = metodosI.llamararchivo()
        if ruta !=None:
            metodosI.mostrardatos(ruta)
    elif opcion==2:
        print("Archivo procesando")
        print("Generando matriz binaria")
        if ruta !=None:
            metodosI.sobrelista(ruta)
            metodosI.nombre(ruta)
        else:
            print("No se a elegido el archivo")
    elif opcion==3:
        if ruta!=None:
            metodosI.creararchi(ruta)
            print("Archivo Escrito correctamente")
        else:
            print("No se a elegido el archivo")
    elif opcion==4:
        datos()
    elif opcion==5:
        if ruta!=None:
            matriz = input("Ingrese el nombre de la matriz a graficar: ")
            metodosI.grafo(matriz)
        else:
            print("No se a elegido el archivo")
    elif opcion==6:
        valor=False
        print("Gracias por usar el programa")
    else:
        print("opcion incorrecta")


