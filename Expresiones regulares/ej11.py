# Ejercicio 11
# Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen 
# con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).

lista_ejemplo = ["Práctica Python", "Práctica C++", "Práctica Fortran", "Practica Petes"]

import re
def leer_lista2(lista):
    lista_pp = []
    for i in lista:
        if re.findall("(P\S*)\s(P\S*)\w", i):
            lista_pp.append(i)
    return lista_pp


print(leer_lista2(lista_ejemplo))

