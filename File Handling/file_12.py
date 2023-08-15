import random as rm
l=[str(rm.randint(500,1000))+"\n" for i in range(20)]
with open("random.txt",'w') as f:
    f.writelines(l)
   
      