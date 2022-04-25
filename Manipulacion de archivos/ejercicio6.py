#Ejercicio 6
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

from tkinter import N

#como eliminar solo los saltos
#def eliminar_saltos_solo(archivo):
#    with open(archivo, "r") as miarch:
#        for line in miarch: 
#           print(line.strip("\n"), end="") #el print x definicion lo imprime con saltos de linea entonces 
   

#eliminar_saltos_solo("Ejercicios guias\Manipulacion de archivos\manipulacion_archivos.txt")

def eliminar_saltos(archivo):
    with open("salida.txt", "w") as salida:
        with open(archivo, "r") as miarch:
            for line in miarch:
                salida.write(line.strip("\n"))

eliminar_saltos("Ejercicios guias\Manipulacion de archivos\manipulacion_archivos.txt")