#  Write a Python program to copy the contents of a file to another file. 

with open('test1.txt','r')as source:            # this is with open file name as source first file data 
    content = source.read()                     # content  =  source.read() all data 



with open('test1.txt','w') as destination:      # this is with open file name as destination second file reciving 
    destination.write(content)                  # destination . write (content) all copy to first file to this file 
