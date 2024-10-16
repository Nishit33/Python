
d1 = {'a' : 100 , 'b' : 200 , 'c' : 300}
d2 = {'a' : 300 , 'b' : 200 , 'd' : 400}
d3 = {}








a = {'1' : ['a','b'] , '2' : ['c','d']}


for i in a['1']:
    for j in a['2']:
        print(i+j,end=" ")








d = [
        {'item' : 'item1' , 'amount' : 400} , 
        {'item' : 'item2' , 'amount' : 300} , 
        {'item' : 'item1' , 'amount':750}
        
    ]        

output = {}

for i in d:
    item = i['item']
    amount = i['amount']

    if item in output:
        output[item] += amount

    else:
        output[item] = amount

for item, i in output.items():
    print(item, i)        






for i in range(1,6):
    for j in range(i+1):
        print(j,end="")
    print()    