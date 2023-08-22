class Rectangle:

    def __init__(self, w=0,h=0):
        self.width = w
        self.height = h

    def getArea(self):
        area = (self.width * self.height)
        return area
    
rectangle = Rectangle
rectangle.__init__(10,5)
print(rectangle.getArea())            


