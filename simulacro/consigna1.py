# **Consigna N°1** (RE)
# Escribir funciones que, dado un String, permitan obtener

#  - cuántas veces aparece el string bc9. P.ej. aparece 2 veces en xsabc9cabcb3sabc9, y ninguna en hola amigos mios.
#  - la lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’. P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.

import re 
def aparece_bc9(string):
    return len((re.findall("(bc9)", string)))

print(aparece_bc9("xsabc9cabcb3sabc9"))

import re
def substrings_delimitados(string):
    return (re.findall("aa([^c].*?)gg", string))
print(substrings_delimitados("ttaatatggttaacatgg"))
