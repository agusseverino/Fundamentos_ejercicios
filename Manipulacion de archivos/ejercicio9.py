def word_counter(archivo):
        frecuencias = dict()
        with open(archivo, "r") as f:
            word_list = f.read().split()
            for i in word_list:
                if i in frecuencias:
                    frecuencias[i] += 1
                else:
                    frecuencias[i] = 1
            for word in frecuencias.keys():
                frecuencias[word] = round(frecuencias[word] / len(word_list),3)
        print(frecuencias)