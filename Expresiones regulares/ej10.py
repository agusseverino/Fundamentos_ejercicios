# Ejercicio 10
# Obtené las substrings y las posiciones de estas en una string dada
#  considerando que las substrings están delimitadas por los caracteres @ o &.
import re
def substrings(string):
    return re.match("&(\w*)&", string)
print(substrings("&hola& hola"))