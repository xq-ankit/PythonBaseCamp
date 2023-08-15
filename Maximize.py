# The first line contain 2 space seperated integer K and M
# the next K lines each contain an integer Ni denoting the number of 
# element in the of list followed by Ni space separated in  integers denoting the elements in the list.
# K is the number of element in the list.
# 3 458 451 142,here 3 is the number of element
# need a combination such that % modulas is the maximum.

from itertools import product 
k,m=map(int,input().split())
l=[]
for i in range(k):
#since the first element is not needed as it is the number of element
#hence it is removed before converting into integer.
    n =map(int,input().split()[1:]) 
    l.append(list(n))
max_val=0
# ---------------------------------------------------------------------
# *l is unpacking to list
# a=[1,2,3]
# print(*a)   output:  1,2,3
# b=[[1,2,45],[1,5,55],[1,6256,41]]
# print(*b)   output:  [1, 2, 45] [1, 5, 55] [1, 6256, 41]
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# product function of itertools give 
# all iterable object combination and return them as tuple
# [1,2] [5,4] output:(1,5) (1,4) (2,5) (5,4)  
# ---------------------------------------------------------------------
for i in product(*l): 
    val=(sum(i**2 for x in i))%m   # this could be avoided as directly 
    if(val>=max_val):
        max_val=val
print(max_val) 
      