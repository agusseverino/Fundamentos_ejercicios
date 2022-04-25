#Ejercicio 7
#Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo.
# Una vez hecho esto se deben imprimir los elementos de la lista.
#manera1
numeros_leidos = int(input("Decime un numero: "))
numeros_positivos = []
if numeros_leidos > 0:
    numeros_leidos = int(input("Decime un numero: "))
    numeros_positivos.append(numeros_leidos)
else:
        print(numeros_positivos)
#xq me corta a la segunda vuelta???
 
#manera2
lista=[]
valor=int(input("Ingresar valor (0 para finalizar):"))
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar):"))

print(lista)





