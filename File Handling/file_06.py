f=open("ankit.txt",'r+')
n=int(input("enter no of lines: "))
count=0
for i in f:
    count+=1
print(count)
for j in range(n):
   print(f.readline(),end="")
f.close()
