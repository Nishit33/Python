
s = input("Enter Name : ")      # s intput enter  name

d={}        # empty dictionary

for i in s:         # for loop i in s 
    if i in d:
        d[i]+=1         # d[i]+=1 in name letter second time print + 1 

    else:
        d[i]=1   # otherwise print 1 
print(d)        
