#Ejercicio 10
#Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.

import glob
import os
os.listdir() #obtenemos la lista de todos los archivos de esa carpeta, pero queremos solo los que son txt.
glob.glob("*.txt") #Te muestra cualquier cosa que termine en .txt

def funcion1(archivo, ruta):
    os.chdir(ruta) # te moves a la ruta donde queres ir
    lista_txt = glob.glob("*.txt") #Te muestra cualquier cosa que termine en .txt
   
    with open(archivo, "a") as s:
        for f in lista_txt:
            file = open(f, "r") # abriste el archivo
            s.write(file.read()) #ya abriste el archivo y lo leés.
            file.close() # cerras el archivo
