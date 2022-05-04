# Ejercicio 9
# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
# Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con 
# respecto a la cantidad total de palabras.


def abrir2(archivo):
    total = {}
    with open(archivo, "r") as miarch:
        separar = miarch.read().lower().split()
        for i in separar:
            if i in total:
                total[i] += 1
            else:
                total[i] = 1
    for word in total:
         total[word] = round((total[word] / len(separar)),3)
    print(total)

print(abrir2("manipulacion_archivosopy.txt"))