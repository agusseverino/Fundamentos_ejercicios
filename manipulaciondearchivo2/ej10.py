# Ejercicio 10
# Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.

# os.listdir() en Python se usa para obtener la lista de todos los archivos y directorios en el directorio especificado. 
# Si no especificamos ningún directorio, se devolverá la lista de archivos y directorios en el directorio de trabajo actual.
#os.chdir() se usa para cambiar el directorio de trabajo actual a la ruta especificada. 
# Solo toma un único argumento como nueva ruta de directorio.

import glob, os
def meter(archivo):
    os.chdir("carpetastexto")
    for file in glob.glob("*.txt"):
        with open(archivo, "w") as miarch:
            miarch.write(file)

os.chdir("my_dir")

for file in glob.glob("*.txt"):
    print(file)
import os 
 
ruta_carpetas    = '/ruta/donde/están/tus/carpetas/' 
nombres_carpetas = os.listdir(ruta_carpetas) 


def buscar_archivos(ruta): 
	archivos_texto = [] 
	archivos       = os.listdir(ruta) 
	for archivo in archivos: 
		if archivo[-4:] == '.txt': 
			archivos_texto.append(archivo) 
	return archivos_texto 

for carpeta in nombres_carpetas: 
	ruta = ruta_carpetas + carpeta 
	archivos_texto = buscar_archivos(ruta) 
	for texto in archivos_texto: 
		with open(ruta + '/' + texto, 'r') as f: 
			# Hacer algo con los archivos de texto! 