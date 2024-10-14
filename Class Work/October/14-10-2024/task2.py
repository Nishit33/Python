# hybrid

class A:

    def add(self):

        self.a=10
        self.b=5

class B(A):

    def add1(self):

        print("Addition : ",self.a+self.b)


class C(A):

    def sub(self):

        print("Subtraction : ",self.a-self.b)


class D(B,C):

    def Total(self):
        self.add()
        self.add1()
        self.sub()
        print("Multiplication : ",self.a*self.b)



obj = D()
obj.Total()

        




