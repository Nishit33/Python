# hierarchi polymorphism

class A:

    def fun(self):

        print("This is function 1")


class B(A):

    def fun(self):
        super().fun()
        print("This is function 2")


class C(A):

    def fun(self):

        print("This is function 3")       


obj = B()
obj.fun()

obj1 = C()
obj1.fun()
