# Write a Python function to check whether a number is in a given range 

def number_range(n):                                # function number _ range 


    s = int(input("Enter the start of the range: "))            # enter start of the range 
    e = int(input("Enter the end of the range: "))              # end of the range 

  
    if s <= n <= e:                                              # if s <= n <= e print range between 
        print(f"{n} is in the range between {s} and {e}.")
    else:
        print(f"{n} is not in the range between {s} and {e}.")  # else range not in between this list 




n = int(input("Enter a number: "))                  # ask number user 

number_range(n)                             # call function
