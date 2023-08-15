try:
    # raise ZeroDivisionError
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a/b
    print(c)
except Exception as e:
    print(e)
print("Program ran:")