# Ejercicio 2
# Escribí un programa que lea un archivo e imprima las primeras n líneas.

def primeraslineas(archivo, numero):

    with open(archivo, "r") as miarch:
        for line in range(numero):
            print(miarch.readline())

primeraslineas("Manipulacion de archivos\manipulacion_archivos.txt", 20)
