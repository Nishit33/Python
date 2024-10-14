# hierarchi

class A:

    def add(self):

        self.a=10
        self.b=15

class B(A):

    def add1(self):

        print("Addition : ",self.a+self.b)


class C(A):

    def sub(self):

        print("Subtraction : ",self.a-self.b)


obj = B()
obj1= C()

obj.add()
obj.add1()

obj1.add()
obj1.sub()

        

        




