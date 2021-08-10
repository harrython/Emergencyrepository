# A class derived from ABC class which belongs to abc module, is known as abstract class in python. ABC class is Meta class.
#   Concrete Method is a Method whose action is defind in the abstract class itself. its like normal Method

    #Note: abstract method must be defind in its child class/subclass.

from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print("Concrete Method")

class Child(Father):
    def disp(self):
        print("Child Class")
        print("Defining Abstract Method")

c = Child()
c.disp()
c.show()


# dusra example

from abc import ABC, abstractmethod

class DefenceForce(ABC):
    def __init__(self):
        self.id = 2332
    @abstractmethod
    def area(self):             #area ka definition dena hi padega o/w next class bhi abstract ban jayega
        pass

    def gun(self):
        print("Gun = AK47",self.id)

class Army(DefenceForce):
    def area(self):
        print("Army area=Land")

class AirForce(DefenceForce):
    def area(self):
        print("AirForce area=Sky")

class Navy(DefenceForce):
    def area(self):
        print("Navy area=sea")

a = Army()
af = AirForce()
n = Navy()

a.gun()
a.area()
print()
af.gun()
af.area()
print()
n.gun()
n.area()
























