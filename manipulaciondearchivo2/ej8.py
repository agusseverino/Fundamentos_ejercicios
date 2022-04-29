# Ejercicio 8
# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

from asyncore import write


def abrir(archivo1, archivo2):
    with open(archivo1, "r") as miarch:
        variable = miarch.read()
        with open(archivo2, "r") as miarchivo:
            variable2 = miarchivo.read()
            with open("salida6.txt", "w") as archivo_final:
                archivo_final.write(variable)
                archivo_final.write(variable2)

#abrir("manipulacion_archivos.txt", "manipulacion_archivos copy.txt")

def abrir1(archivo1, archivo2):
    with open(archivo1, "r") as f1, open(archivo2, "r") as f2, open("salida7.txt", "w") as archivo_final:
        archivo_final.write(f1.read() + f2.read())
abrir1("manipulacion_archivos.txt", "manipulacion_archivos copy.txt")      