unique=[]

list=input("Enter Number seprated by space : ").split()

for i in list:
    if i not in unique:
        unique.append(i)

print(unique)

