n=int(input("Enter the line no: "))
with open("ankit.txt",'r+') as f:        #f=open("ankit.txt",'r')
    line=f.readlines()                   # gives a list of all the line
    l=line[-n:]                          #last n lines
for i in l:
    print(i,end="")
