# Ejercicio 7
# Realizá un programa que encuentre un string que contenga solamente letras minúsculas, 
# mayúsculas, espacios y números.
import re 
def programa(string):
    return not bool(re.search("[^\w*\s]", string))
print(programa("hola 1234 MARTIN "))
print(programa("hola 1234 M ?? "))
