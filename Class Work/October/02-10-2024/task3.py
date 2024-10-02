
# File handling write +

file=open("test2.txt","w+")
file.write("Hello this is w+ method")
print(file.tell())
file.seek(0)
print(file.readline())
file.close()