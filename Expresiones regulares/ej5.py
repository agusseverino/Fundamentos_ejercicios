#Ejercicio 5
#Escribí un programa que diga si un string empieza con un número específico.
import re
def numero(string, numero_especifico):~
    return  bool((re.search("(^numero_especifico1)", string)))

print(numero("2hola", 2))