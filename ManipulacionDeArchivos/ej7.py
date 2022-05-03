# Ejercicio 7
# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

def abrir(archivo):
    with open(archivo, "r") as miarch:
        mas_larga = 0
        palabra_larga = ""
        variable = miarch.read().split()
        for palabra in variable:
            if len(palabra) > mas_larga:
                mas_larga = len(palabra)
                palabra_larga = palabra
        print("La palabra mas larga es ", palabra_larga, " y su largo es: ", mas_larga)

abrir("manipulacion_archivos.txt")

def maslarga(archivo):
    with open(archivo, 'r') as f:
        palabras = f.read().split()
        maslarga = max(palabras, key=len)
    return print("La palabra mas larga es:", maslarga, "con", len(maslarga), "caracteres")
