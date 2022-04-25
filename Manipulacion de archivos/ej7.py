#Ejercicio 7
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

def palabra_mas_larga(archivo):
    largo = 0
    mas_larga = " "
    with open(archivo, "r") as f:
        palabras = f.read().split() #el read lee por bit, readline lee por linea. En este caso necesito que trabaje con todo el archivo, separado por espacios que lo determino con el split
        for word in palabras:
            if len(word) > largo:
                largo = len(word)
                mas_larga = word
    print("la palabras mas larga es: " + mas_larga + " y su largo es " + str(largo))

palabra_mas_larga("Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt")














def palabra_mas_larga(archivo):
	palabra = "la"
	max_longitud = 2
	with open (archivo, "r") as f:
		lista_palabras = f.read().split()
		for word in lista_palabras:
			if len[word] > max_long:
				max_long = len[word]
				palabra = word
	print("la palabra es " + palabra + " y su longitud es " + str(max_long))
