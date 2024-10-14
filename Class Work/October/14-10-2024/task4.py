# Multiple Polymorphism

class A:

    def myfun(self):
        
        print("This is Function 1")


class B:

    def myfun(self):
        super().myfun()
        print("This is Function 2 ")


class C(B,A):

    def myfun(self):
        super().myfun()
        print("This is Function 3 ")


obj= C()
obj.myfun()