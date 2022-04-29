# Ejercicio 3
# Escribí un programa que lea un archivo, guarde las líneas del archivo en una 
# \lista y luego imprima las n últimas.

def leer_archivo(archivo, numero):
    variable = []
    with open(archivo, "r") as miarch:
        for line in miarch:
            variable.append(line)
    print(variable[-numero:])

leer_archivo("Manipulacion de archivos\manipulacion_archivos.txt", 20)