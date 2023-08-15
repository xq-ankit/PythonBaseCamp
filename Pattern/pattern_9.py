#   * * * * * * * * * 
#     * * * * * * *
#       * * * * *
#         * * *
#           *
n=int(input("enter no of row: "))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,n):
        print(i,end=" ")
    for l in range(i,n-1):
        print(i,end=" ")
    print()