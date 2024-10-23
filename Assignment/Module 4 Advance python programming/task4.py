# Write a Python program to read first n lines of a file. 


file = open('test1.txt', 'r')               # file open and give location file 


n = 3                               # how many line we want to see


for i in range(n):                  # loop make 
    line = file.readline()          # line file.readline()
    if line:                            # if line :
        print(line.strip())         # print(line.strip())


file.close()                    # and then file close 
