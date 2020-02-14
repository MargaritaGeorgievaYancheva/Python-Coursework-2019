from product import *

class Cream(Product):
  
  priceOfMilk=2.50

  def __init__(self):
    self.countOfEgs=6
    self.gramOfSugar=300
    self.gramOfButter=300
    self.gramOfFlour=500
    self.milk=600
  
  def calculatePrice(self):
    sum=0
    sum += (self.countOfEgs*super().priceOfEgg)
    sum+= ((self.gramOfButter/1000)*super().priceOfButter)
    sum+=((self.gramOfSugar/1000)*super().priceOfSugar)
    sum+=((self.gramOfFlour/1000)*super().priceOfFlour)
    sum+=((self.milk/100)*self.priceOfMilk)
    return sum
