# cada chef tiene un atributo plato_del_dia;
# las instancias de Chef pueden picantear ese plato solo si no está demasiado picante, en caso de estarlo arrojan una excepción que dice El plato ya está demasiado picante;
# las instancias de AyudanteDeCocina no tienen atributos ya que pueden suavizar cualquier plato que reciban como argumento.
# Mientras que de los platos podemos contar lo siguiente:

# las Pastas tienen un atributo ajies que inicialmente es 0;
# están demasiado picantes cuando tienen más de 10 ajies;
# al ser picanteadas aumenta en 5 su cantidad de ajies y al ser suavizadas pierden 1;
# las Pizzas tienen condimento que inicialmente es "adobo";
# se considera que una pizza está demasiado picante si su condimento es "cayena";
# al suavizar una pizza su condimento pasa a ser "orégano" y al picantearla, "cayena"
class Chef:
  def __init__(self, plato_del_dia):
    self.plato_del_dia = plato_del_dia
    
  def picantear(self):
    if not self.plato_del_dia.demasiado_picantes():
      self.plato_del_dia.picantear()
    else:
      raise Exception("El plato ya está demasiado picante")
    
class AyudanteDeCocina:
  def suavizar(self, plato):
    plato.suavizar()
 
class Pasta:
  def __init__(self):
    self.ajies = 0
    
  def demasiado_picantes(self):
    return self.ajies > 10
  
  def suavizar(self):
    self.ajies -= 1
  
  def picantear(self):
    self.ajies += 5
    
class Pizza:
  def __init__(self):
    self.condimento = "adobo"
    
  def demasiado_picantes(self):
    return self.condimento == "cayena"
  
  def suavizar(self):
    self.condimento = "orégano"
    
  def picantear(self):
    self.condimento = "cayena"