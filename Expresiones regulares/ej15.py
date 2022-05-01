# Ejercicio 15
# Realizá un programa que validar si una cuenta de mail está escrita correctamente.
import re
def validar_mail(mail):
    if bool(re.search("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", mail)):
        print("este mail es válido")
    else:
        print("este mail no es válido")