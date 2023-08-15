import random as r
l=[str(r.randrange(500,1000))+"\n"  for i in range(20)]
f=open("myfile.txt",'w+')
f.writelines(l)
print("Done appended!")
f.close()
