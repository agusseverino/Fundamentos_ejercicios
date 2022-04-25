#Ejercicio 9
#Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. 
#Se debe introducir el nombre y la edad de cada alumno por teclado. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). 
# Al finalizar se deben mostrar los siguientes datos:

#La edad máxima de todos los alumnos.
#Los alumnos que tengan la edad máxima

lista = []
nombre = input("Decime tu nombre: ")
valor_maximo = 0
while nombre != "*":
    edad = int(input("Decime tu edad: "))
    if edad is None or edad >= valor_maximo:
            valor_maximo = edad
            lista.append(nombre)
    nombre = input("Decime tu nombre: ")

print(valor_maximo)
print(lista)

#xq me devuelve todos?????