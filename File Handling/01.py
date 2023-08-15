n=input("enter:")
let=0
dig=0
for i in n:
    if(i.isalpha()):
        let+=1
    elif(i.isdigit()):
        dig+=1
print(f"LETTER={let}")
print(f"Digits={dig}")