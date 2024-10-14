# Hierarachi

class A:

    def l1(self):

        self.l = [1,2,3,4,5,6,7,8,9,10]

class B(A):

    def l2(self):

        self.l1()
        self.l.pop()
        print(self.l)

class C(A):

    def l3(self):

        self.l1()
        self.l.append(11)
        print(self.l)

obj = B()
obj.l2()

obj1 = C()
obj1.l3()



