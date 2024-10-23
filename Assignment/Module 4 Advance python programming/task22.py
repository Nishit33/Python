#  How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

"""
A class is a blueprint for creating objects. 
A class can define attributes (variables) and methods (functions) that are common to all objects created from that class.



"""


"""
What is self?
self refers to the instance of the class (the object) itself.
It is used to access the class's attributes and methods from within the class.
When you create an object from the class, self allows the object to access its own data and methods.
"""

class Car:                                      # class car 

    def __init__(self, brand, model, year):     # def init (self,brand,model,year )
        self.brand = brand                      # self.brand = brand
        self.model = model
        self.year = year


    def display_info(self):                 # def display info (self):  print car details self.year self.brand self.model
        print(f"Car Details: {self.year} {self.brand} {self.model}")


    def start_engine(self):             # def start engine self print self.brand self.model engine is now running 
        print(f"{self.brand} {self.model}'s engine is now running.")


my_car = Car("Toyota", "Corolla", 2020)         # mycar = car toyota corolla 2009 


my_car.display_info()               # call the function displayinfo 
my_car.start_engine()               # call the function startengine
