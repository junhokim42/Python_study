# Class

class MyFirstClass:
    clsVar = 'The best way to predict the future is to invent it.'
    def clsMethod(self):
        print(MyFirstClass.clsVar + '\t- Alan Curtis Kay -')

mfc = MyFirstClass()

mfc.clsVar
mfc.clsMethod()

# Super
class A:
    def methodA(self):
        print("Calling A's methodA")
    def method(self):
        print("Calling A's method")

class B:
    def methodB(self):
        print("Calling B's methodB")

class C(A, B):
    def methodC(self):
        print("Calling C's methodC")
    def method(self):
        print("Calling C's overridden method")
        super().method()

c = C()
c.methodA()
c.methodB()
c.methodC()
c.method()