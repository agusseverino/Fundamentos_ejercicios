# Ejercicio 10
# Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.

# os.listdir() en Python se usa para obtener la lista de todos los archivos y directorios en el directorio especificado. 
# Si no especificamos ningún directorio, se devolverá la lista de archivos y directorios en el directorio de trabajo actual.
#os.chdir() se usa para cambiar el directorio de trabajo actual a la ruta especificada. 
# Solo toma un único argumento como nueva ruta de directorio.

import os, glob
def meter(archivo):
    os.chdir("carpetastexto")
    hola = glob.glob("*.txt")
    for cada_archivo in hola:
        with open(cada_archivo, "r") as miarch:
            que = miarch.read()
            with open(archivo, "a") as capomal:
                capomal.write(que)
meter("vacio.txt")