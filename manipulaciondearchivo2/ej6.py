# Ejercicio 6
# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
def reemplazar1(archivo):
    with open(archivo, "r") as miarch:
        with open("salida2.txt", "w") as archivo:
            for linea in miarch:
                variable = linea.replace("\n", "")
                archivo.write(variable)

#reemplazar("manipulacion_archivos.txt")

def reemplazar(archivo):
    with open(archivo, "r") as miarch:
        variable = miarch.read().replace("\n", "")
    with open("salida3.txt", "w") as miarchivo:
        miarchivo.write(variable)
reemplazar("manipulacion_archivos.txt")

