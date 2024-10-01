#  Write a Python script to sort (ascending and descending) a dictionary by value.


   
d = {'banana': 2,'apple': 5, 'grape': 1, 'orange': 8}       # dictionary key and value

    
items = list(d.items())                                     # items = list 

    
for i in range(len(items)):                             # for i in range (ken(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:                       # if items i1>itmesj1
            items[i], items[j] = items[j], items[i]             # then print asc

    
asc = {key: value for key, value in items}              # key value for key value in items

print("Ascending Order:", asc)

    
for i in range(len(items)):                             # for i in range (len(items))
    for j in range(i + 1, len(items)):                      # for j in range i + 1 
        if items[i][1] < items[j][1]:                   # if items i 1 < items j 1 then print desc
            items[i], items[j] = items[j], items[i]

    
desc = {key: value for key, value in items}

print("Descending Order:", desc)

