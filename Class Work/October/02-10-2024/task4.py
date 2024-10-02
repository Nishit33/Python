
# File Handling read+

file = open ("test2.txt","r+")

print(file.readline())

file.write("\nThis is append!")

file.close()