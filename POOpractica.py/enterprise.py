# Se está pensando en el diseño de un juego que incluye la nave espacial Enterprise. En el juego, esta nave tiene un nivel de potencia de 0 a 100, 
# y un nivel de coraza de 0 a 20. La Enterprise puede:

# encontrarse con una pila atómica, en cuyo caso su potencia aumenta en 25.
# encontrarse con un escudo, en cuyo caso su nivel de coraza aumenta en 10.

# recibir un ataque, en este caso se especifican los puntos de fuerza del ataque recibido. 
# La Enterprise "detiene" el ataque con la coraza, y si la 
# coraza no alcanza, el resto se descuenta de la potencia. Por ejemplo si la Enterprise con 80 de potencia y 12 de coraza recibe un ataque de 20 puntos
#  de fuerza, puede parar solamente 12 con la coraza, los otros 8 se descuentan de la potencia. La nave debe quedar con 72 de potencia y 0 de coraza. 
#  Si la Enterprise no tiene nada de coraza al momento de recibir el ataque, entonces todos los puntos de fuerza del ataque se descuentan de la potencia.
# La potencia y la coraza tienen que mantenerse en los rangos indicados, por ejemplo, si la Enterprise tien 16 puntos de coraza y se encuentra con un escudo, 
# entonces queda en 20 puntos de coraza, no en 26. Tampoco puede quedar negativa la potencia, a lo sumo queda en 0. La Enterprise nace con 50 de potencia y 5 de coraza. 
# Implementar este modelo de la Enterprise, que tiene que entender los siguientes mensajes:

# potencia()

# coraza()

# encontrarPilaAtomica()

# encontrarEscudo()

# recibirAtaque(puntos)

class Enterprise():
    def __init__(self, potencia, coraza):
        self.potencia = potencia #pudo poner el rango de los estados. tipo que el nivel de potencia vaya de 0 a 100
        self.coraza = coraza
    def encontrarPilaAtomica(self):
        self.potencia += 25
        if self.potencia > 100:
            self.potencia = 100
    def encontrarEscudo(self):
        self.coraza += 10
        if self.coraza > 20:
            self.coraza = 20
    def recibirAtaque(self, puntos_de_fuerza):
        if self.coraza >= puntos_de_fuerza:
            self.coraza -= puntos_de_fuerza
        else:
            if self.potencia >= puntos_de_fuerza:
                self.potencia -= (puntos_de_fuerza - self.coraza)
                self.coraza = 0
            else:
                self.potencia = 0
                self.coraza = 0
    def fortalezaDefensiva(self):
        print("el máximo nivel de ataque es", str(self.coraza + self.potencia))
    def necesitaFortalecerse(self):
        return print(bool((self.coraza == 0) and (self.potencia < 20)))
    def fortalezaOfensiva(self):
        if self.potencia < 20:
            return print("0")
        else:
            return print(str((self.potencia -20)/2))

#
enterprise = Enterprise(50, 5)  
enterprise.necesitaFortalecerse()
enterprise.fortalezaDefensiva()
enterprise.encontrarPilaAtomica() #75, 5
enterprise.recibirAtaque(14) #66 ;0
enterprise.encontrarEscudo() #66 ;10
print("potencia", str(enterprise.potencia), "coraza", str(enterprise.coraza))  