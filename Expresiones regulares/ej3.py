# Ejercicio 3
# Creá un programa que verifique las siguientes condiciones:

# si un string dado tiene una h seguida de ninguna o más e.

# si un string dado tiene una h seguida de una o más e.

# si un string dado tiene una h seguida de una o más e.

# si un string dado tiene una h seguida de dos o tres e.

#b)
import re   
def tieneh(string):
    return bool((re.search("(he*)", string)))

print(tieneh("heleee"))
print(tieneh("hola"))
print(tieneh("lol"))

#b)
import re   
def tieneh1(string):
    return bool((re.search("(he+)", string)))

print(tieneh1("holeee"))
print(tieneh1("hele"))

#d)
import re
def tieneh3(string):
    return bool((re.search("(he{2,3}\b)", string)))
print(tieneh3("heee"))
print(tieneh3("hee"))
print(tieneh3("heeeeee"))
print(tieneh3("he"))
#nose si la ultima me tendria que dar false, xq tiene mas de 3 e y me da true.



def espacio(string):
    return bool((re.findall("(\w*)[_](\w*)", string)))
