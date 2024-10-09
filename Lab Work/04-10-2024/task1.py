


# find the middle of string through the parameterized function 



def string(n):

    s = input("Enter String name : ")

    s1 = ()

    if len(s)%2==0:
        print(s)

    else:
        s1 = int(len(s)/2)
        print(s[s1-1] + s[s1] + s[s1+1])    

    print(s1)        


string(7)






#find the value number 

d ={}

s = input("Enter String : ")

for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)    

    
    






d = [1,2,3]
d1 = ['Virat','Bat','Ronaldo']


d2={}

for i in range(len(d)) :
    d2[d[i]] = d1[i]

print(d2)







# pattern 

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()    






# find the duplicate values from list without using built in 

l = [1,2,3,4,1,2]

l1=[]

for i in range(len(l)):
    if l[i] not in l1:
        l1.append(l[i])
print(l1)                







d1 = {1:'a' , 2: 'b'}
d2 = {1:'c' , 2: 'd'}


joint={}


for i in d1:
    joint[i] = d1[i] + d2[i]

print(joint)    
