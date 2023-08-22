class Rectangle:

  def __init__(self,widht,weight):
     self.widht = 0
     self.height = 0

  def set_Dimentions(self,w,h):
    self.widht = w
    self.height = h

  def get_Area(self):
    print(self.widht,'x',self.height)
    print('Area do retangulo: ',self.widht * self.height)
  
retang = Rectangle(0,0)
retang.set_Dimentions(10,3)
retang.get_Area()
