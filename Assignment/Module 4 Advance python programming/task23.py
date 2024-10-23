#  Write a Python class named Rectangle constructed by a length and width and 
# a method which will compute the area of a rectangle


class Rectangle:                        # class rectangle 
    def __init__(self, length, width):          # def init (self,length,width)
        self.length = length                    # self.length = length 
        self.width = width                      # self.width  = width 

    def compute_area(self):                     # def compute area (self): return self.length * self.width 
        return self.length * self.width 


rect = Rectangle(10, 5)                             # rect = rectangle (10,5)
print("The area of the rectangle is:", rect.compute_area())     # print the area of the rectangle is 
