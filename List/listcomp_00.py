# wap in python to make a list of list using comprehension for making
# multiplication table of a given no

print("Enter the number:"end=" ")
num=int(input())
l=[[num,'X','=',i*num] for i in range(1,11)]
for i in l:
  print(i)