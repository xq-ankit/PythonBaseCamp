"""WAP in python to take a dictionary from user where roll no is the key value and name as value
then sort that dictionary according to their roll no."""
d=dict() # d={} this is also a empy dictionary
n=int(input("Enter the number of students: "))
for i in range(n):
    k=int(input("Enter the roll no: "))
    print(i)
    if(k in d):
      print('''This roll no already exist!\nEnter agaain!!!!''')
      i-=1
      print(i)
    else:  
      v=input("Enter the Name: ")
      d[k]=v
# print(d)(the old dictinary)
r=list(d.keys())
r.sort()
nd={}
for i in r:
   nd[i]=d[i]
print(nd)
 