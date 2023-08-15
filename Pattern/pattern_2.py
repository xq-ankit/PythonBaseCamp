# *****
# ****
# ***
# **
# *
r=int(input("Enter Row:"))
for i in range(r):# starting from the r which is no of row and ending at 0 since python doesn't count last one.
    for j in range (1,i+1):
        print("*",end="")
    print()    
