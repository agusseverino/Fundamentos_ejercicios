#Ejercicio 4
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.


def cantidad_palabras(archivo):
    with open(archivo, "r") as miarch:
        lista_palabras = miarch.read().split()
    print(len(lista_palabras))

cantidad_palabras("Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt")  

