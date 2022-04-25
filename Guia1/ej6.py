#Ejercicio 6
#Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas
#y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.

horario_ingresado = int(input("Decime los minutos: "))
horas = round(horario_ingresado/60)
minutos = horario_ingresado - (horas*60)
print(str(horas) + " " + "horas" + " "+ str(minutos) + " " + "minutos")