# Write a Python program to calculate surface volume and area of a cylinder 

# Surface Area = 2πr² + 2πrh
# Volume = πr²h


    
r = float(input("Enter a Radius of a cylinder : "))         # Get the Radius value from user.

    
h = float(input("Enter a Height of a cylinder : "))          # Get the Height value from user.

    
a = 2*3.14*r*(r+h)                                      # Calculate the Surface Area of Cylinder

    
v = 3.14*r*r*h                                      # Calculate the Volume of Cylinder

print(f"Surface Area of Cylinder : {a}")                        # surface area of cylinder 

print(f"Volume of Cylinder       : {v}")                    # volume of cylinder 