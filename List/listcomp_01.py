# wap in python to take two list and make third list having tuple 
# of coresponding element without using zip
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[(l1[i],l2[i]) for i in range(min(len(l1),len(l2)))]
print(l3)