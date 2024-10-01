# Write a Python program to find the highest 3 values in a dictionary 


d = {'apple': 50, 'banana': 20, 'orange': 30, 'mango': 10, 'grape': 40}

values = sorted(d.values(), reverse=True)[:3]

print("The highest 3 values are:", values)

