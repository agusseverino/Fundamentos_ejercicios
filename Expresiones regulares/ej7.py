# Ejercicio 7
# Realizá un programa que encuentre un string que contenga solamente letras minúsculas, 
# mayúsculas, espacios y números.
import re 
def programa(string):
    return re.groups("[\w\s]", string)
#print(programa("hola 1234 MARTIN "))
#print(programa("hola 1234 M ?? "))
def tiene_todo(string):
    lista = re.findall("[\w\s]", string)
    return lista


print(tiene_todo("hola, Co??M o 112 -- estas"))