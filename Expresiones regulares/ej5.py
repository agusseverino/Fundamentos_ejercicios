#Ejercicio 5
#Escribí un programa que diga si un string empieza con un número específico.
# import re
# def numero(string, numero_especifico):
#     numero_especifico1 = numero_especifico
#     return (re.match(numero_especifico1\w*, string))

# print(numero("2hola", 2))

import re
def numero(string, numero_especifico):
    return bool((re.search(str(numero_especifico), string)))

print(numero("3hola", 3))
