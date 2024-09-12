
# Star pattern 
# 1 Right Angle
# 2 Left Angle
# 3 Triangle
# 4 Upside and downside Triangle


for i in range(1,6):    # 1 Right star
    print("*"*i)


for i in range(1,6):      # 2 Left star 
    print(" "*(5-i),"*"*i)


for i in range (1,6):       # 3 Triangle 
    print(" "*(5-i)," *"*i)


for i in range(1,6):          # 3 Upside and Downside
    print(" "*(5-i)," *"*i)
for i in range(4,0,-1):
    print(" "*(5-i)," *"*i)    
