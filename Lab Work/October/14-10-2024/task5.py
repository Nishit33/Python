# Hybrid

class A:

    def l1(self):
        print("This is fun 1")



class B(A):

    def l2(self):
        print("This is fun 2 ")

class C(A):

    def l3(self):
        print("This is fun 3")

class D(B,C):

    def l4(self):
        print("This is fun 4")

obj = D()        
obj.l1()
obj.l2()
obj.l3()
obj.l4()