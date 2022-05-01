# Ejercicio 8
# Escribí un programa que separe y devuelva los caracteres númericos de un string.
import re
def separalos(string):
    return re.findall("[\d]", string)
print(separalos("1hola c2jojo"))