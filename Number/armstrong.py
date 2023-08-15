s = 123
temp = s
sum = 0
l = len(str(s))
for i in range(l):
    n = s % 10
    sum = sum + n ** l
    s = s // 10
if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")