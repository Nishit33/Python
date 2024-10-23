#  What is used to check whether an object o is an instance of class A? 

"""
In Python, the isinstance() function is used to check whether an object o is an instance of a class A (or a subclass of A).
This function returns True if the object is an instance of the class or a subclass, and False otherwise.
"""

class Animal:       # class animal : pass 
    pass

dog = Animal()      # dog = animal 

print(isinstance(dog,Animal))       # print isinstance(dog,animal)