
# Lottery 4 number winner game 

import random           # import random

l = [12,43,65,76,87,64,87,99,101,325,7868,4242,1212,9999,86753]         # list all 15 number 

for i in range(1,5):                                        # for i in range (1,5)
    print(f"Lottery Number is {i} : ",random.choices(l))        # print winner number 4 using choices