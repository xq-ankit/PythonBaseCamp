# *****
#  ****
#   ***
#    **
#     *
r=int(input("Enter row"))
for i in range(r,0,-1):
    for j in range(1,(r+1)-i):
       print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print("")       