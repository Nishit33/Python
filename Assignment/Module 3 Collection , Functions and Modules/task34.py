# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

d = {}          # dictionary empty 


for i in range(1, 16):      # for i in range (1,16)
    d[i] = i * i            # d[i] = i*i

print(d)                    # print d