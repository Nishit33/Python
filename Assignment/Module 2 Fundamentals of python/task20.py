# Write a Python function to insert a string in the middle of a string. 

def insert(main_s,s):       # def insert function and pass parameter main_s , s
        
        l = 0          # string length equal to 0
                
        for i in main_s:        # for i in main_s so l += 1 increment 
                l += 1
        
        middle = l // 2         # middle = 1 // 2

        return main_s[:middle] + s + main_s[middle:]        # return main_s[:middle]+ s+main_s[middle:]
        
        
main_string = input("Enter the main string: ")      # string input enter main string 

str=input("Enter the string to insert: ")       # str input enter string insert

print("The new string is: ",insert(main_string,str))    # print the new string is , insert(main_string,str)
