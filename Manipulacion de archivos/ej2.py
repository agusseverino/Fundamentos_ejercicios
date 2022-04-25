#manera1
from itertools import islice
def leer_n_lineas_archivo(archivo, n):
    with open(archivo, "r") as f:
        for line in islice(f, n):
            print(line)
leer_n_lineas_archivo("Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", 20)

#manera2

def imprimir(archivo, n):
    with open(archivo, "r") as miarch:
        for line in range(n):
            print(miarch.readline())
imprimir("Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", 25)

