from asyncio.format_helpers import _get_function_source
from calendar import day_name
from email.utils import parsedate_to_datetime
from glob import glob
from os import listxattr
import re
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE
from statistics import median_low
#r dice que lo que estas metiendo es literal no 
#findall todo lo que estamos buscando
#(.?) . punto cualquier caracter ? se utiliza para favorecer los matches internos, sino lo pongo se favorece lo de los extremos
#* que aparezca 0 o mas veces 
#+ 1 o mas veces -(.*?)- busco un patron que esta entre los guiones
"Hoy estuvimos trabajando re -regular expression- en python -con vscode-"
#Si no le pongo el signo de pregunta no me toma los guiones del medio
#search si te aparece y en que posicion
import re
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
#una o mas veces
import re
def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"


ej11
primero recorremos la lista
P mayuscula seguida de cualquier caracter alfanumerico un espacio y la p
(P\w*)\W(P\w*)\.[a-z]
#ejerccio mail 
caracteres alfanumericos que aparezcan cualq cantidad de veces y le ponemos algunos signos que sabemos que van 
[/W+_-]@[/W+]\
Cualquier Uno o mas caracteres alfanumericos 
el mail puede o no arrancar con un guion 
Despues viene un @
despues viene el mail de la empresa--- cualq caracter alfanumericos de 6 a 10 despyes del ALERT_DESCRIPTION_BAD_CERTIFICATE
Despues va la barra xq le digo que literalmente despues va una barra 
Un rango de la a a la z de dos a seis veces .ar. com etc 

Cuales son los delimitadores
el arroba y el punto 
SI yo quiero buscar patrones por ej guiones    
-()- meto lo que quiero en el medio 
Los delimitadores vana fuera del parantesis y el patron va adentro 
La r toma literal las secuencias de escape, no los puntos x ejemplo entonces tengo que poner \. 

patron mail = "r"
Si quiero saber \wM Cualquier caracter alfanumerico y que tenga la m 
^ afuera del rango significa que arranque con eso 
Quiero que tenga cuaquier caracter alfnumerico que arranque con m\w  


a = glob.glob*=("*txt") abre todos los archivos que sean txt
b = open("salida", "a")
for arch in a 
import glob
import os --- xq importo os?? xq voy a obtener
#os.getcwd() se en que carpeta estoy parado---- no hace falta en el parcial xq estoy en el mismo repositorio
tengo que ir a la carpeta donde estan los archivos txt 
os.chdir("../Repositorio") tengo que cambiar de carpeta e ir a la de atras e ir a la que se llama repositorio
Hacemos el ch dirc con el relative path del script que ellos nos dan 
os.mkdir("")--- creo una carpeta en donde estoy parado si le pongo ../nombre la crea en la superior a la que estoy
glob.glob
a= glob.glob("*txt")
b = open("salida", "a")
for archivo in a:
    c= open(archivo, "r")
    b.write(c.read())
    c.close()
b.close()
Abrimos la lista de archivos txt y los guardamos en la variable c, los vamos abriendo de a uno 
Leemos el archivo c y lo escribimos en la b despues cerramos la c y b


