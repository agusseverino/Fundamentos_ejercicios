# Ejercicio 3
# Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, 
# el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook 
# si se aplicase el descuento. 
# Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

class Notebook:
    def _init_(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = 0

    def discount(self, integer):
        print(self.precio - ((self.precio*integer)/100))

notebook1 = Notebook("apple", "air", 185000)