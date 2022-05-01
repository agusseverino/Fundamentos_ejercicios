# Ejercicio 11
# Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen 
# con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
lista_ejemplo = ["Práctica Python", "Práctica C++", "Práctica Fortran", "Practica Petes"]

import re
def leer_lista2(lista):
    jojo = []
    for i in lista:
        if re.findall("(P\S*)\s(P\S*)\w", i):
            jojo.append(i)
    return jojo


print(leer_lista2(lista_ejemplo))

def empiezan_p(lista):
    jojo = []
    for i in lista:
        if re.findall("(P*?)\s(P*?)\s", i):
            jojo.append(esto)
    return jojo


#print(empiezan_p(lista_ejemplo))

import re
def leer_lista(lista):
    for i in lista:
        return re.findall("(P.*?)\s(P.*?)\s", i)

#print(leer_lista(lista_ejemplo))