#ejercicio 1
# interfaz de un objeto es el conjunto de mensajes que entiende, estos mensajes son los metodos
#es el conjunto de funciones que pertenecen a una misma clase---- los elementos de la clase perro pueden hacer estas 4 cosas: comer, acariciar, energia y estar debil.
#Estos objetos tienen estados, alimento y caricias.
class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2
