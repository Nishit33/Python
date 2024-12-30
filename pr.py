# list = [[1,2,3] , [4,5,6] , [7,8,9]]

# for item in list:
#     for i in item:
#         print(i)

# print('"python uses \\n for newline"')


# print(type(2**3**2))


# A = [1,20,18,17,35,66]

# count=0
# count1=0
# for i in A:
#     if i % 2 == 0:
#         count+=1
#     else:
#         count1+=1

# print(f"Even Number : {count} Odd Number : {count} ") 


# c ={'name': 'xyz' , 'salary' : 35000 , 'Age' : 19 , 'City' : 'Ahmedabad'}

# del c['name']
# del c['salary']

# print(c)



# a = [1,2,3,4,5,6]
# b = [7,2,9,10,11,12]


# if set(a) & set(b):
#     print(True)

# else:
#     print(False)


# d = {'a' : 20 , 'b' : 20 , 'c': 30 , 'd':40 }



# age = int(input("Enter Your Age : "))
# print(f"so next year you are will be {age+1}")


# value = None

# if value:
#     print("value is true")

# else:
#     print("value is false")



# l = [32,54,67,31,98,6,12,33]        

# largest = max(l)
# smallest = min(l)
# sum = sum(l)


# print("Largest nUmber : ",largest)
# print("smallest nUmber : ",smallest)
# print("sum : ",sum)


# l = input("Enter string seprated by space : ").split()

# count = 0

# for i in l:
#     if len(i) >= 2 and i[0]  == i[-1]:
#         count += 1 

# print("Number is count : ",count)



# l = [1,2,3,4,5,6,7,8,9,4,5,6,7,4,6,2,2,1,1,4,8,9]

# print(set(l))


# def value(l1,l2):
#     for i in l1:
#         if i in l2:
#             return True
#         return False


# l1 = int(input("Enter Number : "))
# l2 = int(input("Enter Number : "))

# result = l1+l2

# print(result)



# l = []

# num = input("Enter Number : ").split()

# for i in num:
#     if i not in l:
#         l.append(i)

# print(l)




# list = input("Enter Character : ").split()

# string = ""

# for i in list:
#     string += i

# print("After joint : ",string)


# list = [1,2,3,4,5,6,7,8,9,10]

# import random

# print("Random Number : ",random.choice(list))


# list = [32,54,76,8,98,12,3245,65,87,98,65,43,11,33,55]

# list.sort()

# print(list)


# print("Second smallest number is : ",list[1])


# list = input("enter number : ").split()

# a , b ,c ,d = list

# print("A : ",a)
# print("B : ",b)
# print("C : ",c)
# print("D : ",d)



# a = input("Enter Name : ")

# b= ""

# for i in range(len(a)-1,-1,-1):
#     b += a[i]

# if a == b:
#     print("Palindrome")

# else:
#     print("Not pal")



# year = int(input("Enter Year : "))

# if year%4==0: 
#     print("Leap Year")

# else:
#     print("Not leap year")


# n = int(input("Enter Number : "))

# fact = 1

# for i in range(1,n+1):
#     fact*=i

# print("Fact Number is : ",fact)


# def addition():
#     a = int(input("enter number : "))
#     b = int(input("enter number : "))

#     result = a+b
#     print(f"so {a} and {b} addition is : {result}")

# addition()


# def addition(a,b):
#     print(a+b)


# num1= 3 
# num2= 9
# addition(num1,num2)


# l = [1,7,5,3,2,9,10,7,5,4,3,2,1,4,5,6,7,8,9,11,45,76,99,79]

# nl=[]

# for i in l:
#     if i not in nl:
#         nl.append(i)

# nl.sort()
# print(nl)

# print(f"The second Heighest Number is : {nl[-2]}   and   second smallest number : {nl[1]}")


# a = "Hello World"

# for i in range(0,len(a)):
#     print(a[i])



# t = (1,2,3,4,5,6,7,8,9,10)

# for i in range(len(t)):
#     print(t[i]) 



# string = "python"

# for i in string:
#     print(i)





