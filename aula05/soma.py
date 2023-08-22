class Point:

    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2
        
    def mete(self):
        print(self.point1+self.point2)

ateu = Point(10,20)
ateu.mete()