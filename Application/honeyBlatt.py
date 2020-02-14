from blatt import *
class HoneyBlatt(Blatt):
  priceForHoney=5.0
  
  def __init__(self):
    super().__init__()
    self.amountOfHoney=300

  def getPriceForHoney(self):
   return self.priceForHoney
   
  def calculatePrice(self):
    sum = (super().calculatePrice())+((self.amountOfHoney/100)*self.getPriceForHoney())
    return sum
  
    
