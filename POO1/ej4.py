# Ejercicio 4
# Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, 
# recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar 
# directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:

# inc()

# dis()

# reset()

# valorActual()

# valorNuevo(nuevoValor)


class Contador:
    def __init__(self, valor):
        self.valor = valor
        self.ultimo_comando = ""
    def inc(self):
        self.valor += 1
        self.ultimo_comando = "incremento"
    def dis(self):
        self.valor -= 1
        self.ultimo_comando = "disminucion"
    def valorActual(self):
        return self.valor
    def valorNuevo(self, valor_nuevo):
        self.valor = valor_nuevo
        self.ultimo_comando = "actualizacion"
    def UltimoComando(self):
        return self.ultimo_comando
    
contador = Contador(10)
contador.inc()
contador.inc()
print(contador.UltimoComando())
contador.dis()
contador.inc()
print(contador.valorActual())
contador.valorNuevo(27)
print(contador.UltimoComando())
contador.dis()
contador.dis()
print(contador.valorActual())
print(contador.UltimoComando())

# Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, 
# en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" 
# (para cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando, y el 
# resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".