# Ejercicio 10
# Obtené las substrings y las posiciones de estas en una string dada
#  considerando que las substrings están delimitadas por los caracteres @ o &.
    
import re

def substrings(string):
    lista = re.findall("[@|&](.*?)[@|&]", string)
    lista2 = []
    for i in lista:
        lista2.append(string.index(i))
    return lista, lista2

print(substrings("@hola@ @como estas& @como"))


