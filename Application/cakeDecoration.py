class CakeDecoration:
  def __init__(self,name):
    self.name=name
  def priceOfDecoration(self,name):
    price=0.0
    if name == "Walnuts":
      price=2.20
    elif name=="Strawberries":
      price=3.50
    elif name=="Hazelnuts":
      price=2.40
    elif name=="White chocolate":
      price=2.80
    return price
