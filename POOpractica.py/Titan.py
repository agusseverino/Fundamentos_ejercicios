# En un mundo distópico la humanidad es atacada sin descanso por titanes. Estos titanes son muy resistentes pero no inmortales, su salud (100 de máxima) 
# puede ir disminuyendo si reciben daño debido a algún ataque, y si llega a 0 se muere. Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido. 

# Además tienen la capacidad de destruir cierto número de casas dependiendo de su salud, siendo 8 casas cuando su salud es máxima o un número proporcional si su salud es 
# menor a la máxima (si tiene 60 puntos de salud destruiría 4.8 casas, es decir, 4 casas completas y más de la mitad de otra). 

# Sin embargo no tienen la capacidad de comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!", el único sonido que hacen. Definí la clase Titan con los atributos y 
# métodos correspondientes. Además instanciá a un Titan y ejecutá las siguientes líneas:
titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())

class Titan():
    def __init__(self, salud): #atributos (el estado es el conjunto de atributos) objeto es lo mismo que clase
        self.salud = salud
        self.correr = False #no sabe correr. puede ser siempre falso
    def salud_actual(self):
        return self.salud #funciona para lo mismo que nosotros antes haciamos pepita.energia
    def recibir_ataque (self, cantidad):
        self.salud -=1.5 *cantidad #porque por cada ataque le saca 1.5 de energia
    def grito(self):
        return "¡aaa!"
    def cuantas_casas(self):
        return (self.salud * 8 / 100) #te va a decir cuantas casas puede destruir (regla de 3, con 100 de salud puedo destruir 8 casas, con la salud que tiene ahora, cuantas casas?)
    def destruir_casas(self):
        if(self.cuantas_casas() >1):
            #por cada casa que destruye pierde 12.5
            if ((self.cuantas_casas() %1)>0): #si el resto de dividir por uno es mayor a 0, (o sea 0, algo)
                self.salud -= (self.cuantas_casas()//1)*12.5 #el // re trunca el número y te saca la coma -> sabemos que tiene coma el numero porque lo pusimos como condición del if. 
                #truncamos el numero para que no se quede sin salud PORQUE SI NO SE MUERE, asi le queda de salud el resto de el número truncado
            else: 
                self.salud -= (self.cuantas_casas() - 1) * 12.5  #le resto 1 para que le quede algo de energia Y NO SE MUERA
        else:
            print("no puede destruir ninguna casa") #si no puede destruir mas de una casa, no puede destruir nada

    def esta_vivo(self): #si la salud es mayor a 0 retorna TRUE que significa que esta vivo
        return (self.salud > 0)

titan1 = Titan(100) #nombre de la variable = objeto con su salud inicial
titan1.recibir_ataque(30)
print("esta vivo", titan1.esta_vivo())
print("salud actual", titan1.salud_actual())
print("cuantas casas puede destruir", titan1.cuantas_casas())
print("grito", titan1.grito())
print("cuantas casas puede destruir", titan1.cuantas_casas())
    