# Ejercicio 4
# Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

import re
def espacio(string):
    return (re.findall("(\w*)[_](\w*)", string))

print(espacio("hola_hola, como estas? estuve_pensando"))
print(espacio("hola"))

