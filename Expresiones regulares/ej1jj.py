#Escribí un programa que verifique si un string tiene al menos un carácter permitido. 
#Estos caracteres son a-z, A-Z y 0-9.

import re 
def caracter_permitido(string):
    return bool((re.search("[\w]", string)))

print(caracter_permitido("//////????"))

# \w matches any word character (equivalent to [a-zA-Z0-9_])
#Tambien contempla el "_", si no lo quiero puedo meter en el rango de search lo que dice la consigna
#Como el search me devuelve la primer coincidencia, uso el bool para que me devuelva true or false
# re.search() function will search the regular expression pattern and return the first occurrence. Unlike Python re.match(), 
# it will check all lines of the input string. The Python re.search() function returns a match object when the pattern is found and “null” if the pattern is not found

