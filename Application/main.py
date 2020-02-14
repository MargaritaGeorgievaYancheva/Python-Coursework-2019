from cream import *
from cake import *
from honeyBlatt import *
from chocolateBlatt import *
from cakeDecoration import *

cakes=[]

cake1=Cake("Nedelq",Cream(),HoneyBlatt(),10)
cake1.addDecoration("Walnuts")
cake1.addDecoration("Hazelnuts")

cake2=Cake("Nedelq",Cream(),ChocolateBlatt(),10)

cake3=Cake("Roza",Cream(),ChocolateBlatt(),20)
cake3.addDecoration("Strawberry")

cake4=Cake("Zaharo",Cream(),Blatt(),8)
cake4.addDecoration("White chocolate")

cakes.append(cake1)
cakes.append(cake2)
cakes.append(cake3)
cakes.append(cake4)

for cake in cakes:
  cake.printInfoForCake()
  print()