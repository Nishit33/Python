s = input("Enter String : ")        # TO find middle value of string in odd string 

if len(s)%2==0:
    print(s)

else:
    s1 = int(len(s)/2)
    print(s[s1-1]+s[s1]+s[s1+1])


