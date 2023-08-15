# question: Use of floor and ceil functions on floating point values.
# Both functions are library functions and declare in math.h header file. 
# Floor ignores the fraction part and just print the same in floating point.
# E.g.
# floor(123.46) then it will return 123.000000
# ceil(123.46) then it will return 124.000000
n=float(input("Enter the Number in float"))
a=n//1
print("%.6f"%a)
print("%.6f"%(a+1))
