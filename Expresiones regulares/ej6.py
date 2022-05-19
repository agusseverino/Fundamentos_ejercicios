# Ejercicio 6
# Escribí un programa que dada una lista de strings verifique 
# si se encuentran en una frase dada.

import re
import string
def verificar(lista_strings, frase):
    strings_lista = []
    for i in lista_strings:
        if i in frase:
            strings_lista.append(i)
    return strings_lista
print(verificar(["hola", "bien", "vos que onda"], "hola yo muy bien"))
