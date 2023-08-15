try:
    number = (input("Enter: "))
    if(len(number)==5):
         raise ZeroDivisionError ("siddhart ka naaam not allowed")
except ZeroDivisionError as e:
    print(str(e))
else:
    print("heljiu641")
finally:
    print("hello")
