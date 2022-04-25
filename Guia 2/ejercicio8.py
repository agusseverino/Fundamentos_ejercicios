#Ejercicio 8
#Realizá un programa que declare tres listas lista1, lista2 y lista3, donde las dos primeras listas deben tener cinco enteros cada una, 
#ingresados por teclado y asigne para cada elemento de la lista3 la suma de los elementos de la lista1 y la lista2 
#(es decir, el primer elemento de la lista3 tiene que ser la suma del primer elemento de la lista1 y el primero de la lista2)
 
# lista=[]
#disponemos un ciclo de 5 vueltas
#for x in range(5):
#    valor=int(input("Ingrese un valor entero:"))
#    lista.append(valor)

#imprimimos la lista    
#print(lista)

lista1 = []
lista2 = []
lista3 =[]
for x in range(5):
    valor = int(input("Ingrese un valor entero: "))
    lista1.append(valor)
for x in range(5):
    valor2 = int(input("Ingrese un valor entero: "))
    lista2.append(valor2)
for x in range(len(lista1)):
    lista3.append(lista1[x]+lista2[x])

print(lista3)

