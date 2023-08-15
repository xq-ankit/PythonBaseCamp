# wap in python to check two numbers given by 
# the user are disible by 5,9 or by both or by none
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
if(a%5==0 and a%9==0):
    if(b%5==0 and b%9==0):
        print("Both the Number %d and %d is divible by 5 and 9"%(a,b))
    else:
        print("Only %d is divible by 5 and 9" %(a))
