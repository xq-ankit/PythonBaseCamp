s=input("enter string")
b=len(s)
c=s[0]
count=0
for i in range(b):
    if(s[i]==c):
        count+=1
if(count==b):
    print("Same")
else:
    print("not same")
print(count)
