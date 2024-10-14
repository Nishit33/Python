# Multi level inheritance

d = {}

class A:

    def fun1(self):

        name = input("Enter Your Name : ")
        id = int(input("Enter Yoour Roll Number : "))


        d['name']=name
        d['id']=id


class B(A):

    def add2(self):

        self.maths = 79
        self.science = 99
        self.english = 88

        

class C(B):

    def add3(self):

        self.name= input("Enter Your Name : ")
        self.id = int(input("Enter Yoour Roll Number : "))

        if d['name']==self.name and d['id']==self.id:

            print("Your Name : ",self.name)

            print("Maths : ",self.maths)
            print("Science : ",self.science)
            print("English : ",self.english)

        else:
            print("Invalid Number !!")


obj = C()
obj.fun1()
obj.add2()
obj.add3()