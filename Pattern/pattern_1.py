# *
# **
# ***
# ****
# *****
r=int(input("Enter the number of row:"))
for i in range(r): #starting from 1 and ending at r+1 as python doesn't take the last one
    for j in range(1,i+1):
        print("*",end="")
    print()