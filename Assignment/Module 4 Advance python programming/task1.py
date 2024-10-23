#  What is File function in python? What is keywords to create and write file. 

"""
In Python, a file function refers to how we handle files (like creating, reading, and writing files). 
The most important function is open(), which is used to open a file so we can work with it.

'w': Write  Create a new file or overwrite an existing one.
'a': Append  Add data to the end of the file without deleting what's already there.


file = open('test1.txt', 'w')

file.write("Hello! This is my first file.\n")
file.write("I am learning how to write to files in Python.")

file.close()


"""