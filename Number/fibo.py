# program to print fibonacci series
n=int(input("ENTER THE NUMBER:"))
a=0
b=1
print(a,b,end=' ')
for i in range(1,n+1):
    c=a+b
    print( c ,end=' ')
    a=b
    b=c
