# Polymorphism

class A:

    def myfun(self):
        print("This is Function 1")



class B(A):                         # inherit
    def myfun(self):
        super().myfun()             # Super method
        print("This is Function 2")     

obj = B()
obj.myfun()