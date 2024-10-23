#  Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

"""
Inheritance in Python

Inheritance allows a class (called the child class or subclass) to inherit attributes and methods from another class 
(called the parent class or superclass). 
This promotes code reusability and makes it easier to maintain.
"""


# Inheritance python example 

class Animal:                       # class Animal 
    def __init__(self, name):               # make def init (self,name): self.name = name
        self.name = name

    def speak(self):                # def speak(self): return i am an animal 
        return "I am an animal."


class Dog(Animal):                  # class dog(animal): def speak(self): return woof my name is plus self.name 
    def speak(self):
        return "Woof! My name is " + self.name


class Cat(Animal):          # class cat def speak return meow my name is + self.name 
    def speak(self):
        return "Meow! My name is " + self.name


dog = Dog("Buddy")      # dog = dog"buddy"
cat = Cat("Wish")       # cat = cat"wish"


print(dog.speak())  # call and print dog 
print(cat.speak())  # call and print speak





"""

What is __init__? (Constructor)

The __init__ method in Python is a special method called a constructor. 
It is automatically called when you create a new instance of a class. 
The primary purpose of the constructor is to initialize the attributes of the new object.

"""



"""
What is constructor in python ?

A constructor in Python is a special method used to initialize objects of a class. 
In Python, the constructor is defined using the __init__ method. When you create an instance of a class, 
the constructor is automatically called to set up the initial state of the object, typically by assigning values to its attributes.

Key Points about Constructors in Python:

The constructor is called when an object is created from a class.
The __init__ method is the constructor in Python.
It is typically used to initialize the attributes of the object.

"""

# example constructor in python 

class person:                       # class person

    def __init__(self,name,age):    # def init self,name,age: self.name = name self.age = age

        self.name = name
        self.age = age

    def display_info(self):         # def display info self : print name and age 
        print(f"Name : {self.name} , Age : {self.age}")

person1 = person("Noor",23)        # person 1 = person name and age 

person1.display_info()          # person1 . display info call function 