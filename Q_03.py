# WAP in python to print to print the longest string
n=int(input("No of element"))
l=[]
for i in range(n):
    l.append(input())
maxi=0
index=0
for i in range(n):
    if(len(l[i])>maxi):
        maxi=len(l[i])
        index=i
print(l)
print(l[index])