from cream import *
from blatt import *
from cakeDecoration import *

class Cake:
  
  def __init__(self,name,Cream,Blatt,countOfPiece):
    self.name=name
    self.Cream=Cream
    self.Blatt=Blatt
    self.countOfPiece=countOfPiece
    self.cakeDecoration=[]
   
  
  def addDecoration(self,CakeDecoration):
    self.cakeDecoration.append(CakeDecoration)
  
  def calculatePriceForDecoration(self):
    sum=0.0
    for i in self.cakeDecoration:
      sum=sum+CakeDecoration.priceOfDecoration(self,i)
    return sum
     
  def calculatePriceForCake(self):
    sum=0
    sum+=self.Blatt.calculatePrice()
    sum+=self.Cream.calculatePrice()
    sum+=self.calculatePriceForDecoration()
    return sum

  def calculatePriceForOnePiece(self):
    result=0
    result=self.calculatePriceForCake()/self.countOfPiece
    return result

  def printInfoForCake(self):
    
    print("Cake '{}' has {} pieces and {}.".format(self.name,self.countOfPiece,type(self.Blatt).__name__))
   
    if len(self.cakeDecoration)==0:
      print("The cake doesn't have any decoration")
    else:
      print("The cake  has decorations: ",end="")
      for i in self.cakeDecoration:
       print(i,end=",")
      print()
   
    print("The price for cake '{}' is {:.2f}.".format(self.name,self.calculatePriceForCake()))

    print("The price for one piece of cake {} is {:.2f}."
    .format(self.name,self.calculatePriceForOnePiece()))