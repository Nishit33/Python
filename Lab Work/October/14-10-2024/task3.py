# Multiple Inheritance 

class A:

    def add(self):

        self.e = int(input("Enter Number 1 : "))

class B:

    def add1(self):

        self.f = int(input("Enter Number 2 : "))        

class C(A,B):        

    def add2(self):

        print("Addition : ",self.e+self.f)


obj = C()
obj.add()
obj.add1()
obj.add2()