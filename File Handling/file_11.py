# write a function largest() which accepts a file name as parameter and reports the 
# longest line in the file along with the number of character it has
def largest( filename):
    with open(filename ,'r') as f:
        content=f.read()
        line=content.split("\n")
    count=0
    for i in line:
        if(len(i)>count):
            count=len(i)
            li=i
    print(li,count)
largest(input("enter the file name: "))
