#  Write a Python program to append text to a file and display the text. 

file = open('test1.txt', 'a')           # file open and create file name and a 

file.write("This is the new line of text.\n")       # write file this is new line of text 

file.close()                                    # then file close 

file = open('test1.txt', 'r')                       # again file open 

content = file.read()                           # file.read()
print(content)

file.close()                                                # file close
