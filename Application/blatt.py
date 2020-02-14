from product import *

class Blatt(Product):

  def __init__(self):
    self.countOfEgs = 4
    self.gramOfSugar=250
    self.gramOfButter=200
    self.gramOfFlour=800
  
  def calculatePrice(self):
    sum=0
    sum += (self.countOfEgs)*super().priceOfEgg
    sum+= ((self.gramOfButter/1000)*super().priceOfButter)
    sum+=((self.gramOfSugar/1000)*super().priceOfSugar)
    sum+=((self.gramOfFlour/1000)*super().priceOfFlour)
    return sum