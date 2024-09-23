
# Python Dictionary

d ={1:"Hello",2:"Welcome",3:"To",4:"India"}     # dictionary

print(type(d))      # type 

print(d.get(1))     # only value get 

print(d.items())    # All key and values 

print(d.keys())     # only keys show

d.popitem()     # bydefalut last key and values remove
print(d)

d.pop(1)        # we pass key that is remove from dictionary
print(d)

d.update({5:"Morning",6:"Namste"})      # update that we can add values and key 
print(d)

t=(1,2,3)       # tuple only keys 
d1={}

print(d1.fromkeys(t,20))    # with fromkeys to input values in dictionary 
