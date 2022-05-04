
# Ejercicio 3
# Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o una golondrina. 
# Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, y 
# finalmente hacerla comer otros 10 gramos. Se propone:

# implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). 
# Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene 
# en estudio, que responden True cuando se les consulta estaEnEquilibrio().

# comprobar el código que se escribió con esta secuencia:

# definir un ornitólogo, dos golondrinas y dos gorriones,
# inicializar las aves con valores conocidos,
# decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
# decirle al ornitólogo que realice su rutina sobre aves,
# verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.

class Golondrina:
    def __init__(self, energia):
        self.energia = energia

    def comer(self, gramos):
        self.energia += 4 * gramos
    def energia_actual(self):
        return self.energia
    def volar_en_circulos(self):
        self.volar(0)
    def volar(self, kms):
        if (self.energia - (10 + kms)) > 0:
            self.energia -= 10 + kms 
        else: 
            print("no puede volar")
    def esta_en_equilibrio(self):
        print(self.energia >= 150 and self.energia <= 300)

class Gorrion: 
    def __init__(self):
        self.gramosActuales = 0
        self.kmsActuales = 0
        self.listaGramos = []
        self.listaKms = []
    def comer (self, gramos):
        self.listaGramos.append(gramos) 
        self.gramosActuales += gramos 
    def volar(self, kms):
        self.listaKms.append(kms)
        self.kmsActuales += kms
    def esta_en_equilibrio(self):
        self.gramosActuales > 100

class Ornitologo:
    def __init__(self):
        self.aves = []
    def estudiar_ave(self, ave):
        self.aves.append(ave)
    def avesEnEstudio(self):
        return self.aves
    def avesEnEquilibrio(self):
        return [self.aves[i].esta_en_equilibrio() for i in range(len(self.aves))]
    def realizarRutina(self):
        [self.aves[i].comer(80) for i in range(len(self.aves))]
        [self.aves[i].volar(70) for i in range(len(self.aves))]
        [self.aves[i].comer(10) for i in range(len(self.aves))]
ornitologo1 = Ornitologo()
gorrion1 = Gorrion()
gorrion2 = Gorrion()
golondrina1 = Golondrina(100)
golondrina2 = Golondrina(50)
ornitologo1.estudiar_ave(golondrina1)
ornitologo1.estudiar_ave(golondrina2)
ornitologo1.estudiar_ave(gorrion1)
ornitologo1.realizarRutina()
print(golondrina1.energia_actual())