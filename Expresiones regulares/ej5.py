#Ejercicio 5
#Escribí un programa que diga si un string empieza con un número específico.
import re
def numero(string, numero_especifico):
    numero_especifico1 = numero_especifico
    return (re.match(numero_especifico1\w*, string))

print(numero("2hola", 2))
import re
def espacio(string):
    return (re.findall("(\w*)[_](\w*)", string))

print(espacio("hola_hola, como estas? estuve_pensando"))
print(espacio("hola"))
