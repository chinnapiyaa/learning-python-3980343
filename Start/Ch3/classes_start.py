# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

#from Finished.Ch3.classes_finished import Motorcycle


class vehicle:
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle

class car(vehicle):
  def __init__(self, enginetype):
    super().__init__("car")
    self.wheels = 4
    self.doors = 4
    self.enginetype = enginetype

class Motorcycle(vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Motorcycle")
    if(hassidecar):
      self.wheels = 3
    else:
      self.wheels = 2
      self.doors = 0
      self.enginetype = enginetype

  car1 = car("gas")
  car2 = car("electric") 
  mc1 = Motorcycle("gas",True)

  print(mc1.wheels)
  print(car1.engine)
  print(car2.doors)   
        