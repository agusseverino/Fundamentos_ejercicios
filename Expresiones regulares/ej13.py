# Ejercicio 13
# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

import re
def remplazar_por_guion(string):
    print(re.sub("(\W{2})", "_", string, 1))

remplazar_por_guion("hola???como")