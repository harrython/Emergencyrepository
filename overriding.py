# Method overriding   do class banana jaruri hai madrchod
class Add:
    def result(self, x, y):
        print('Addition:', x+y)

class Multi:
    def result(self, a, b):
        super().result(1 , 3)
        print('Multiplication:', a*b)

#class Multi(Add):
#        pass

m = Multi()
m.result(10, 20)

#inheritance rule isiliye hota hai child class k object se sara class ko access kr le


