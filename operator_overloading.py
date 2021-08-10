# operator ko overload kaise krte hai
print(12+3)

print(int.__add__(1,2))

print('hi'+'hello')
print(str.__add__('hi','geekyshows'))

#laslflljlasllfl
class A:
    def __init__(self, x):
        self.x = x

class B:
    def __init__(self,x):
        self.x = x

a = A(111)
b= B(333)
print(a+b)      #A.__add__(a,b)

3+3               int.__add__(3,3)
'a'+'b'           str.__add__('a'+'b')
a+b               A.__add__(a,b)
