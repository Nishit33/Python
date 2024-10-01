# Write a Python function to check whether a number is in a given range 

def number_range(n):


    s = int(input("Enter the start of the range: "))
    e = int(input("Enter the end of the range: "))

  
    if s <= n <= e:
        print(f"{n} is in the range between {s} and {e}.")
    else:
        print(f"{n} is not in the range between {s} and {e}.")




n = int(input("Enter a number: "))

number_range(n)
