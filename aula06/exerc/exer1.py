class Rectangle:
   
    def set_dimentions(self,w=0,h=0):
        self.width = w
        self.height = h

    def get_area(self):
        area = (self.height * self.width)
        print(self.width," x ",self.height," = ",area)

num = Rectangle()
num.get_area(10,5)
    