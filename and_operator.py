#AND operator for strings
a="hello"
b="ho"
#if any value is false it return false value which is '' in this case that is empty string
# doesn't matter the position of empty it will return false value which is empty string 
c= '' and 'a' 
e='a' and ''
d= "as" and 'b'
# both string is true only empty string is said to be false when both are 
#true it return second value which is "b" in this case.
print(d)
print(e)
print(type(c))
print(eval(d))#'b' becomes b which have value as ho