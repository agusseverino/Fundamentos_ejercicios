class AnimalAlado:
  def esta_feliz(self):
    return self.energia > 500


class Golondrina(AnimalAlado):
  def _init_(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_débil(self):
    return self.energia < 10


class Dragon(AnimalAlado):     
  def _init_(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_débil(self):
    return self.energia < 50

class Entrenador:
  """Un entrenador tiene un equipo y puede admitir nuevos miembros a su equipo"""
  def _init_(self, equipo):
    self.equipo = equipo

  def el_equipo(self):
    """Getter: Es un método que solamente retorna el estado del objeto"""
    return self.equipo

  def agregar_animal_alado(self, animal):
    """Este método toma un objeto animal alado que tendrá todos los atributos de esa clase"""
    self.equipo.append(animal)

  def entrenar_dragon(self, dragon):
    """Para entrenar al equipo, primero defino como se entrena a uno y lo repito para todos"""
    for i in range(20):
      dragon.volar_en_circulos()
    dragon.comer_peces(3)

  def entrenar_equipo(self):
    for dragon in self.equipo:
      self.entrenar_dragon(dragon)
      """Self va afuera porque es un método propio del entrenador"""

  def entrenar_golondrina(self, golondrina):
    for i in range(20):
      golondrina.volar_en_circulos()
    golondrina.comer_alpiste(600)

  def entrenamiento_intensivo(self):
    for equipo in self.equipo:
      pass

class AvesNoVoladoras:
  def _init_(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def correr_en_circulos(self):
    self.correr(0)

  def correr(self, kms):
    self.energia -= 10 + kms

  """Las AvesNoVoladoras son parcialmente polimorficas con las aves Golondrinas.
  Comparten el método comer alpiste."""

pepita = Golondrina(100)
juanita = Golondrina(100)
anastasia = Golondrina(200)
maria = Golondrina(42)
roberta = Dragon(10, 1000)
chimuelo = Dragon(200, 1000)

hipo = Entrenador([roberta])