# Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa),
# CSSP y CSSV (como el CSS pero “pico” y “veces”). El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza 
# a estudiar, por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando solamente lo que voló la vez
# que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si 
# un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.

import csv


class Gorrion:
    def __init__(self):
        self.kms_actuales = 0
        self.gramos_actuales = 0
        self.lista_kms = []
        self.lista_gramos = []
        equilibrio = self.css


    def comer(self, gramos):
        self.gramos_actuales += gramos
        self.lista_gramos.append(gramos)
    
    def volar(self, kms):
        self.kms_actuales += kms
        self.lista_kms.append(kms)

    def css(self):
        if self.gramos_actuales > 0:
            return self.kms_actuales / self.gramos_actuales 
        else:
            return None

    def cssv(self):
        if len(self.lista_gramos) > 0:
            return max(self.lista_kms) / max(self.lista_gramos)
        else:
            return None
    
    def cssp(self):
        if len(self.lista_gramos)> 0:
            return len(self.lista_kms) / len(self.lista_gramos)
        else:
            return None
    
    def esta_en_equilibrio(self):
        return 0.5 < self.css() < 2

    
    
gorrion = Gorrion()
gorrion.comer(10)
gorrion.volar(15)
gorrion.volar(40)
gorrion.comer(5)
gorrion.volar(20)
gorrion.comer(50)
gorrion.volar(30)
print(gorrion.css())
print(gorrion.cssv())
print(gorrion.cssp())
print(gorrion.esta_en_equilibrio())