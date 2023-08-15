n = int(input("Enter any number: ")) 
sum1 = 0 
for i in range(1, 6): 
    if(n % i == 0): 
        sum1 = sum1 + i 
if (sum1 == 6): 
    print("The number is a Perfect number") 
else: 
    print("The number is not a Perfect number")