# Ejercicio 7
# Realizá un programa que encuentre un string que contenga solamente letras minúsculas, 
# mayúsculas, espacios y números.
import re 
def programa(string):
    return not bool(re.findall("[^\w\s]", string))
print(programa("hola 1234  "))
print(programa("hola 1234 M ?? "))

