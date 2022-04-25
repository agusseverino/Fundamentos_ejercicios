
#Ejercicio 1
#Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.

cadena = input("cadena: ")
#opcion1
if cadena[0] == cadena[0].upper():
    print("la primera es mayuscula")
else:
    print("la primera es minuscula")
#opcion2
def que_es(cadena):
    if cadena[0] == cadena[0].upper():
        print("la primera es mayuscula")
    else:
        print("la primera es minuscula")

que_es("hola")


