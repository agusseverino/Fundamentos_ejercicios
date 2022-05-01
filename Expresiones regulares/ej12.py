# Ejercicio 12
# Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).
from dataclasses import replace
import re
regularexpresion = "[\s_..]"
def hola(string):
    return re.sub(regularexpresion, "|", string)

print(hola("espacios, guiones bajos y dos puntos por la barra vertica___.."))
