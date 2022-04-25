#Ejercicio 10
#Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena 
#(considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter 
#"a" también tiene 1).

#manera 1
diccionario = {}
cadena = input("cadena: ")
lista =list(cadena)
for i in lista: 
    diccionario[i] = lista.count(i)

print(diccionario)
#manera2
cadena = input("Cadena: ")
def contador_ocurrencias(cadena):
    diccionario = {}

    for i in cadena:
        if i in diccionario.keys:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario