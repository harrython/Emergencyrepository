from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

class Child(Father):
    def disp(self):
        print("Child Class")
        print("Defining Abstract Method")

c = Child()
c.disp()

##jitne bhi abstract method honge unko child class me define karna hoga

from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass

class Child1(Father):
    def disp1(self):
        print("Child 1 Class")
        print("Disp 1 Abstract Method")

class Grandchild(Child1):
    def disp2(self):
        print("GrandChild Class")
        print("Disp 2 Abstract Method")

gc = Grandchild()
gc.disp1()
gc.disp2()














