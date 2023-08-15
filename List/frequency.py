# WAP to add exact frequency of any element in a new list
a=eval(input("Enter the List"))
k=int(input())
l=[] #empty list
for i in a:
    if(a.count(i)>k and i not in l ):
        l.append(i)
print(l)