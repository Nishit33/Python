# Multiple Inheritance

class A:

    _a = int(input("Enter Number 1 : "))
    def fun1(self):
        print("This is fun1")



class B:

    _b = int(input("Enter Number 2 : "))

    def fun2(self):
        print("This is fun2!!")


class C(A,B):

    def merger(self):

        print("Addition : ",self._a+self._b)

obj = C()
obj.fun1()
obj.fun2()
obj.merger()

