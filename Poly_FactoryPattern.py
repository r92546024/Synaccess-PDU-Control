
import math
class shape (object):
    def computeArea(self):
        pass

class retangle (shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def computeArea(self):
        return self.length * self.width

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def computeArea(self):
        return math.pi * self.radius * self.radius

class shapefactory():
    def getshape(self,shape_type):
        if shape_type=='retangle':
            return retangle(20,5)
        elif shape_type=='circle':
            return circle(20)
        return null

def mainfactorydemo():
    factory = shapefactory()
    product1 = factory.getshape('retangle')
    print("product1 %s" % product1.computeArea() )

    product2 = factory.getshape('circle')
    print("product2 %s" % product2.computeArea())

def main():
    A = retangle(20,5)
    print (A.computeArea())
    B = circle(20)
    print (B.computeArea())

if __name__ == '__main__' :
    main()
    mainfactorydemo()

