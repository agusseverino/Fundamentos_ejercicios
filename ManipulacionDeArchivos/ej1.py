# Ejercicio 1
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese
#  archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas 
#  líneas no empiezan con "P").

def empiezan_p(archivo, letra):
    with open(archivo, "r") as miarch:
        count = 0
        for line in miarch:
            if line.startswith(letra):
                count += 1
    print(count)

empiezan_p("Manipulacion de archivos\manipulacion_archivos.txt", "a")


