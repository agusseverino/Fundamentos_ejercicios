#Ejercicio 1
#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra
#(por ejemplo que imprima cuántas líneas no empiezan con "P").

from itertools import count


def empiezan_con(letra, archivo):
    with open(archivo, "r") as miarch:
        count = 0
        for line in miarch:
            if line[0] != letra.upper or line[0] != letra.lower():
                count +=1
    print("el numero de lineas que no empiezan con " + letra + " es " + str(count))


empiezan_con("s", "Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt")
 #no entiendo xq me da siempre lo mismo?????

