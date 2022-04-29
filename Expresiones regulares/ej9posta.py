# Ejercicio 9
# Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# (String de ejemplo:
#  "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
import re
def programa(string):
    return re.findall("-(.*?)-", string)

print(programa("oy estuvimos trabajando con re -regular expression- en python -con VSCode-"))