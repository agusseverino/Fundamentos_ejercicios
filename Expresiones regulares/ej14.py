# Ejercicio 14
# Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

import re
def hola(string):
    return re.sub("[\t\s]", ";", string)

print(hola("ho?????????hola222222     				"))
