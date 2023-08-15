l=[1,2]
try:
    x = 10 / 2  
    z=l[10]
    y=10+'5'
    print("This statement won't be executed")
except ZeroDivisionError:
    print("1 Error: Division by zero occurred")
except NameError:
    print("2 Error: Name is not defined")
except ValueError:
    print("3 Error: Invalid value")
finally:
    print("4 Cleanup code: Closing resources")
print(" 5 Statement after exception handling")