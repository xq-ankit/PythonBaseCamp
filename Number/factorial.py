n=int(input("Enter the Number: "))
s=n
fac=1
while(n):
    fac*=n
    n-=1
print(f"The factorial of {s} is {fac}")