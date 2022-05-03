
# **Consigna N°3** (Manejo de exepciones)
# Ejecutá el script_misterioso.py y realizá resolvé:
#     1. ¿Qué tipo de exepción arroja la corrida del script? La excepcion que arroja es de division por un cero
#     2. Mejorá el código para que capture dicho error específicamente y lo maneje 
#       imprimiendo una advertencia al usuario sobre las posibles causas de dicho error
#     3. ¿Qué otras excepciones deberias considerar?
muestras_2 = []

def obtener_media(lista):
    sumatoria = 0

    for valor in lista:
        sumatoria += valor
    longitud = len(lista)

    try:
        print(sumatoria / longitud)
    except ZeroDivisionError:
        print("Trataste de dividir entre cero :( ")

obtener_media(muestras_2)

