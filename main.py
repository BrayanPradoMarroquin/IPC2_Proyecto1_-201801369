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
    opcion=int(input("Ingrese la opcion de la acción a realizar"))
    if opcion==1:
        print("Llamar archivo")
        ruta = metodosI.llamararchivo()
        metodosI.mostrardatos(ruta)
    elif opcion==2:
        print("Archivo procesado")
    elif opcion==3:
        print("Archivo Escrito correctamente")
    elif opcion==4:
        datos()
    elif opcion==5:
        print("Grafica generada correctamente")
    elif opcion==6:
        valor=False
        print("Gracias por usar el programa")
    else:
        print("opcion incorrecta")


