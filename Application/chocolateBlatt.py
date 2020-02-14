from blatt import *

class ChocolateBlatt(Blatt):
  priceForCoccoa=2.50
  
  def __init__(self):
    super().__init__()
    self.amountOfCoccoa=200
  
  def calculatePrice(self):
    sum = super().calculatePrice()+((self.amountOfCoccoa/100)*self.priceForCoccoa)
    return sum
  