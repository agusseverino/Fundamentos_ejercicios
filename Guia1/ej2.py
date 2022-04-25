#Ejercicio 2
#Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayúscula 
#(Asegurarse de que el string tenga la cantidad de caracteres suficientes).

def imprimir(string):
    if len(string) >= 6:
        print(string[4:6].upper())


