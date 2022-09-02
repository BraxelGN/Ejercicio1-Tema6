class vehiculo: 
  def __init__(self, color, ruedas, puertas):
    self.color = color
    self.ruedas = int(ruedas)
    self.puertas = int(puertas)
    
  def DarColor(self):
    return self.color

  
  def DarRuedas(self):
    return self.ruedas 
    

  def DarPuertas(self):
    return self.puertas
    
class coche(vehiculo):
  def __init__(self,color, ruedas, puertas,velocidad,cilindrica):
    self.color = color
    self.ruedas = int(ruedas)
    self.puertas = int(puertas)
    self.velocidad = float(velocidad)
    self.cilindrica = int(cilindrica)

  def DarVelocidad(self):
    return self.velocidad
  
  def DarCilindrica(self):
    return self.cilindrica

FordKa = coche("gris", 4, 5, 120.0,22)
print("AUTO FORD KA: ",end="")
print("color:",FordKa.DarColor(),
      " ,ruedas:",FordKa.DarRuedas(),
      " ,puertas:",FordKa.DarPuertas(),                
      " ,velocidad:",FordKa.DarVelocidad(),
      " ,Cilindrica:",FordKa.DarCilindrica()
     )
