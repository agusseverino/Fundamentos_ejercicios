# Ejercicio 2
# Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
import re
def caracteres_permitidos(string):
    return (re.search('[\W_]', string)) is None

print(caracteres_permitidos("holaa"))
print(caracteres_permitidos("!!!!"))
print(caracteres_permitidos("aaa!!"))