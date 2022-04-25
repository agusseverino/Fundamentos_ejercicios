class Persona:
    def __init__(self, energia):
        self.energia = energia
        self.feliz = False
    
    def energia_actual(self):
        return self.energia

    def dormir(self, horas):
        if horas >= 8:
            self.energia = 100
        elif self.energia + (horas*12.5) <= 100:
            self.energia =+ horas * 12.5
        else:
            self.energia = 100
    def comer(self):
        if self.energia + 10 <= 100:
            self.energia += 10
        else:
            self.energia = 100
    def hacer_ejercicio(self, horas_de_ejercicio):
        if self.energia - ((horas_de_ejercicio/2) *25) >= 0:
            self.energia -= ((horas_de_ejercicio/2) *25)
        else:
            self.energia = 0
class Estudiante(Persona):
    def aprobar (self):
        self.feliz = True
    def estudiar(self, horas):
        if self.energia - horas*20 >= 0:
            self.energia -= horas * 20
        else:
            self.energia = 0

estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())
    