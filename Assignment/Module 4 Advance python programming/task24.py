#  Write a Python class named Circle constructed by a radius and two 
#        methods which will compute the area and the perimeter of a circle


import math                             # import math 

class Circle:                           # class circle

    def __init__(self , radius):        # def init self,radius
        self.radius = radius            # self.radius = radius 

    def compute_area(self):             # one method def compute_area(self) : return math.pi * (self.radius ** 2)
        return math.pi * (self.radius ** 2)
    
    def compute_parimeter(self):        # second method def compute parimeter(self) : return 2 * math.pi * self.radius
        return 2 * math.pi * self.radius
    



Circle = Circle(5)                      # circle = circle(5)
print("The area of the circle is : ",Circle.compute_area())         # print the area of the circle is 
print("The perimeter of the circle is : ",Circle.compute_parimeter())   # and perimeter of the circle is 

