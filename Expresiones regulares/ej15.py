# Ejercicio 15
# Realizá un programa que validar si una cuenta de mail está escrita correctamente.
import re
def validar_mail(mail):
    return bool(re.search("[a-zA-Z0-9]+(-_\.)*[a-zA-Z0-9]+@[a-z]{2,9}(\.[a-z]{2,9}){1,2}", mail))
        
print(validar_mail("agusseverino5@gmail.com"))


# [A-Za-z0-9]+[\.-_])*[A-Za-z0-9]+
#  #Tiene que haber 1 o mas de cualquier letra o numero, 
# despues puede haber 0 o mas de un . - o _ pero como los mails no terminan normalmente asi, 
# tiene que seguir de 1 o mas numeros o letras 
#@ arroba obligatorio 
#[a-z]{1,9}---- gmail, hotmail
#(\.[a-z]{2,4}) si o si tiene que haber despues del arroba un punto seguido de algunos caracteres
#(\.[a-z]{2,4}){0,1} si o si tiene que haber despues del mail algunos caracteres ej . com pero puede haber un .ar entonces contemplo que pueda aparecer ina vez mas 
#mi opcion [a-zA-Z0-9]+[-_\.]*[a-zA-Z0-9]*@[a-z]{2,9}(\.[a-z]{2,9}){1,2}
# opcion de guille ([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,}+)