#!/usr/bin/python
"""
Use Abstract parent-class and create many sub-class inherit from parent-class to provide a consistent interface.
The consistent interface will be override to have different behavior from different sub-class.

簡單來說，多型是指子類別繼承父類別時，同時改寫父類別的函式或變數，而我們可以宣告一個屬於父類別的變數，去存取子類別中改寫自父類別的函式或變數，這我們稱之為多型 Polymorphism



Create an abstract class called Shape and then inherit from it other shapes
like diamond, rectangle, circle, triangle etc. Then have each class override
the area and perimeter functionality to handle each shape type.
"""
import math

class Shape(object):

    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):

    def __init__(self, side_length):
        self.side = side_length

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

def main():
    print("##########1 Poly Demo#############")
    rect = Rectangle(20, 30)
    print("Rectangle(20, 30)")
    print("  Area: " + str(rect.area()))
    print("  Perimeter: " + str(rect.perimeter()))

    rect = Rectangle(400, 30)
    print("Rectangle(400, 30)")
    print("  Area: " + str(rect.area()))
    print("  Perimeter: " + str(rect.perimeter()))

    circle = Circle(20)
    print("Circle(20)")
    print("  Area: " + str(circle.area()))
    print("  Perimeter: " + str(circle.perimeter()))

##############################################################


class shapefactory():

    def getshape(self,shape_type):
        if shape_type == 'cycle':
            return Circle(20)
        elif shape_type == 'rectangle':
            return Rectangle(400, 30)
        elif shape_type ==  'square':
            return Square(10)

        return null


def factorydemo():
    factory = shapefactory()
    cycleproduct = factory.getshape('cycle')
    rectangleproduct = factory.getshape('rectangle')
    squareproduct = factory.getshape('square')

    print ( "cycleproduct " + str(cycleproduct.area()) )
    print ( "rectangleproduct " + str(rectangleproduct.area()) )
    print ( "squareproduct " + str(squareproduct.area()) )

def main4():
    print("##########4 FactoryDemo#############")
    factorydemo()



##############################################################

class Singleton(object):
    __single = None
    instanceN= None

    def __new__(self):
        if  Singleton.__single == None:
            Singleton.__single = object.__new__(self)
        return Singleton.__single

    def doSomething(self):
        print("do something...XD " + str(self.instanceN) )

def main2():
    print("##########2 Singleton Demo#############")
    singleton1 = Singleton()
    singleton2 = Singleton()

    singleton1.doSomething()
    print (singleton1.instanceN)
    singleton1.instanceN = 2
    print (singleton1.instanceN)

    singleton2.doSomething()
    print (singleton2.instanceN)


##############################################################

class A (object):
    def foo1(self):
        print ("Hello foo1", self)

    @staticmethod
    def foo2():
        print ("hello foo2")

    @classmethod
    def foo3(cls):
        print ("hello foo3", cls)

def main3():
    print("##########3 staticmethod/classmethod#############")
    a = A()

    a.foo1()
    A.foo1(a)

    a.foo2()
    A.foo2()

    A.foo3()
    a.foo3()


##########################################




if __name__ == '__main__':
    main()
    main2()
    main3()
    main4()
