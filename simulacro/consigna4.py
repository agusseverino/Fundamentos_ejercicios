# **Consigna N°4** (Manejo de archivos)

# Escribí un programa que, por un lado, debe crear una nueva carpeta en la 
# posición actual llamada _Resultado_ y, por otro, que lea todos los archivos con extensión `.txt` 
# y escriba el contenido de todos en un único archivo llamado *texto_completo.txt*, que tiene que estar 
# dentro de la carpeta _Resultado_. **NO se pueden usar rutas absolutas**
# ruta_relativa = os.path.join("Documentos", "UCEMA", "Fundamentos", "Práctica4", "archivo.txt")
# >>> print(ruta_relativa)

import os, glob
def crear2():
    os.mkdir('_Resultado_')
    lista_archivos = glob.glob("*.txt")
    for archivo in lista_archivos:

        with open(archivo, "r") as archivo_entrada:
            leer = archivo_entrada.read()

            with open(r"_Resultado_\nuevo_texto.txt", "a") as archivo_salida:
                archivo_salida.write(leer)
    
crear2()
    
    
import os, glob
    
def crear():
    os.mkdir('_Resultado_')
    path_archivos = os.getcwd()
    ruta_relativa = os.path.join(os.getcwd(), "_Resultado_")
    hola = glob.glob("*.txt")
    for archivo in hola:
        os.chdir(path_archivos)
        with open(archivo, "r") as miarch:
            leer = miarch.read()
            os.chdir(ruta_relativa)
            with open("nuevo_texto", "a") as archivos_txt:
                archivos_txt.write(leer)
#crear()
# import os
# ruta_relativa = os.path.join(os.getcwd(), "_Resultado_")
# print(ruta_relativa)
# os.chdir(ruta_relativa)
#_Resultado_
# import os, glob
# def meter(archivo):
#     os.chdir("carpetastexto")
#     hola = glob.glob("*.txt")
#     for cada_archivo in hola:
#         with open(cada_archivo, "r") as miarch:
#             que = miarch.read()
#             with open(archivo, "a") as capomal:
#                 capomal.write(que)
# meter("vacio.txt")