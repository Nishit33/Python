#  How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

"""
In Python, you can handle exceptions using a combination of try, except, and finally blocks to manage errors
and ensure certain code always runs, whether an exception occurs or not.

Here's how each part works:

try block: Contains code that may raise an exception.
except block: Catches and handles specific exceptions that may occur in the try block.
finally block: Executes regardless of whether an exception occurred or not.
"""

try:
    num = int(input("Enter a number: "))    # try enter number 
    result = 10 / num 

except ValueError:                                              # except valueerror print invalid integer 
    print("Invalid input! Please enter a valid integer.")

except ZeroDivisionError:                                       # except zerodivisionerror print division by zero is not allowed 
    print("Error: Division by zero is not allowed.")

finally:                                                       # finally this will always run whether exception occurs or not 
    print("This will always run, whether an exception occurs or not.")
