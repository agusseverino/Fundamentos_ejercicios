# Ejercicio 10
# Obtené las substrings y las posiciones de estas en una string dada
#  considerando que las substrings están delimitadas por los caracteres @ o &.
import re
def substring(string):
    hola = re.findall("[@|&](.*?)[@|&]", string) 
    for i in hola:
        hola5 = []
        hola6 = re.search(i, string)
        hola5.append(hola6)
    print(hola, hola5)
    
    

print(substring("@hola@ @como estas& @como"))










# def substrings(string):
#     return re.match("&(\w*)&", string)
# print(substrings("&hola& hola"))