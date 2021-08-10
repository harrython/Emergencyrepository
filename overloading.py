#Method overloading
class Myclass:
    def sum(self, a,b,c):
        s = a+b+c
        return s

obj =Myclass()
print(obj.sum(1,23,3))          #ek arg pass nhi kr sakte
print()
print



# ab sabhi arg pass kar sakte hai 1 2 3 jo bhi ho
class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s= a+b
        else:
            s='provide at least two numbers'
            return s

obj = Myclass()
print(obj.sum(32,4))

