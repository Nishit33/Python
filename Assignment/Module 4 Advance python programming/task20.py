#  Write python program that user to enter only odd numbers, else will raise an exception. 


class EvenNumberError(Exception):           
    pass

def odd_number():                               # def odd number ()
    try:                                                        # try : num = int(input("Enter an odd number : "))
        num = int(input("Enter an odd number: "))
        
        
        if num % 2 == 0:                                # if num % 2 == 0 : raise evennumbererror "the number is even ! "
            raise EvenNumberError("The number is even! Please enter an odd number.")
        
        
        print(f"Thank you! {num} is an odd number.")            # print thankyou number is an odd number 
    
    except EvenNumberError as e:                    # except evennumbererror as e : print (e)
        print(e)
    
    except ValueError:                              # except valueerror print ("invalid input please input valid integer")
        print("Invalid input! Please enter a valid integer.")


odd_number()


