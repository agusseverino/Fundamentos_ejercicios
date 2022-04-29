# Ejercicio 5
# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.
def reemplazar(archivo, letra):
    with open(archivo, "r") as miarch:
        with open("salida_txt", "w") as archivo:
            for linea in miarch:
                variable = linea.replace("p", "\n" + letra)
                archivo.write(variable)

#reemplazar("Manipulacion de archivos\manipulacion_archivos.txt", "n")

def reemplazar3(archivo, letra):
    with open(archivo, "r") as miarch:
        variable = miarch.read().replace("p", letra + "\n")
    with open("salida5.txt", "w") as miarchivo:
        miarchivo.write(variable)
reemplazar3("manipulacion_archivos.txt", "n")