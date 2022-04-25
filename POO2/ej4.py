
# Ejercicio 4
# Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

# comienzan con una cantidad que podemos establecer de combustible

# los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible por cada kilómetro recorrido

# las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;

# pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible

# saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

# Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.

class MetodoDeTranporte:
    def __init__(self, combustible = 100):
        self.combustible = combustible
    def cargar_combustible(self, cantidad):
        self.combustible += cantidad
    def entran(self, personas):
        return personas <= self.maxpersonas()
    def combustibleActual(self):
        return self.combustible
    def recorrer(self, kilometro):
        self.combustible -= kilometro * self.cantidad_transporte()
class Moto(MetodoDeTranporte):
    def maxpersonas(self):
        return 2
    def cantidad_transporte(self):
        return 1
class Auto(MetodoDeTranporte):
    def maxpersonas(self):
        return 5
    def cantidad_transporte(self):
        return 0,5

moto1 = Moto(200)
moto2 = Moto()
auto1 = Auto(300)
auto2 = Auto()

moto1.recorrer(5)
print(moto1.combustibleActual())