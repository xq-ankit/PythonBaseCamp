l=input("Enter the sentence: ").split()
print(l)
a="aeiouAEIOU"
for i in l:
    if(i[0] not in a and i[-1] in a):
        print(i,end=" ")
        