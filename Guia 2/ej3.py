#Ejercicio 3

numero_dado = float(input("numero_dado: "))
def es_numero_del_dado (numero_dado):
    return 7 > numero_dado > 0

if es_numero_del_dado (numero_dado) and numero_dado == 1:
    print("6")
elif es_numero_del_dado (numero_dado) and numero_dado == 6:
    print("1")
elif es_numero_del_dado (numero_dado) and numero_dado == 2:
    print("5")
elif es_numero_del_dado (numero_dado) and numero_dado == 5:
    print("2")
elif es_numero_del_dado (numero_dado) and numero_dado == 3:
    print("4")
elif es_numero_del_dado (numero_dado) and numero_dado == 4:
    print("3")
else:
    print ("el numero asignado es incorrecto")