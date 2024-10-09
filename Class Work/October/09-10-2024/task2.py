class Myclass:
    
    def myfun1(self):

        n = input("Enter Name : ")
        n1 = n[::-1]

        if n==n1:
            print("Palindrome!!")

        else:
            print("Not Palindrome") 


class Myclass2(Myclass):                # inheritance

    def pattern(self):

        for i in range(6):
            print("*"*i)


obj = Myclass2()
obj.myfun1()
obj.pattern()