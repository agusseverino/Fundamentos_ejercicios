#Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente.
#Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

numero_ingresado = int(input("Ingrese un numero"))
if 1 <= numero_ingresado <= 7:
    if numero_ingresado == 1:
        print("Lunes")
    if numero_ingresado == 2:
        print("Martes")
    if numero_ingresado == 3:
        print("Miercoles")
    if numero_ingresado == 4:
        print("Jueves")
    if numero_ingresado == 5:
        print("Viernes")
else:
    print("El numero es incorrecto")

