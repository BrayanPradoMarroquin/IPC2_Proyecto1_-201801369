valor=True
menu = """""
Menú
1. Cargue el archivo
2. Procesar el archivo
3. Escribir el archivo de Salida
4. Mostrar datos del estudiante
5. Generar grafica
6. Salir 
"""

while valor==True:
    print(menu)
    opcion=int(input("Ingrese la opcion de la acción a realizar"))
    if opcion==1:
        print("Llamar archivo")
    elif opcion==2:
        print("Archivo procesado")
    elif opcion==3:
        print("Archivo Escrito correctamente")
    elif opcion==4:
        print("Mostrar Datos del alumno")
    elif opcion==5:
        print("Grafica generada correctamente")
    elif opcion==6:
        valor=False
        print("Gracias por usar el programa")
    else:
        print("opcion incorrecta")


