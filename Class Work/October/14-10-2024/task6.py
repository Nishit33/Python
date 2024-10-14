# Hybrid polymorphism


class A:

    def fun(self):

        print("This is fun 1")

class B(A):

    def fun(self):
        super().fun()
        print("This is fun 2")        

class C(A):

    def fun(self):
        super().fun()
        print("This is fun 3")


class D(C,B):

    def fun(self):
        super().fun()
        print("This is fun 4")



obj = D()
obj.fun()




