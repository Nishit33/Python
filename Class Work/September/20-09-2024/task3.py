
# Find out which is odd number or even number 

ev = []
od = []
l = []

for i in range(1,31):
    l.append(i)
    if i%2==0:
        ev.append(i)
    else:
        od.append(i)    

print(l)        
print(ev)
print(od)