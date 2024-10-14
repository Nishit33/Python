# single level inheritance


class A:

    def add(self):

        t = int(input("Enter Number 1 : "))
        c = int(input("Enter Number 2 : "))

        print("Addition is : ",t+c)

        print("This is function 1 ")

class B(A):

    def add1(self):

        y = int(input("Enter Number 1 : "))
        d = int(input("Enter Number 2 : "))

        print("Multiplication : ",y*d)

        print("This is function 2 ")        


obj = B()
obj.add()
obj.add1()