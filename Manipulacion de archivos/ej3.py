#Ejercicio 3
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def guardar_lineas(archivo, n):
    archivo_lineas = []
    with open(archivo, "r") as miarch:
        for line in miarch:
            archivo_lineas.append(miarch.readline())
    print(archivo_lineas[-n:])
  

guardar_lineas("Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", 1)


