# Ejercicio 4
# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
def leer_archivo(archivo):
    with open(archivo, "r") as miarch:
        palabras = miarch.read().split()
    print(len(palabras))
leer_archivo("manipulacion_archivos.txt")