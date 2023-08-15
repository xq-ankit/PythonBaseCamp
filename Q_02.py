# wap in python to make a atm machine logic in which user enter amount and you have 
# to print 2k,5h,200,100 note's in decreasing amount.
num=int(input("Enter the Withdrawal Amount: "))
tk=num//2000
num%=2000
fh=num//500
num%=500
th=num//200
num%=200
h=num//100
rem=num%100
print('The Monetized Note are',f"2000:{tk} \n500:{fh} \n200:{th} \n100:{h}\nRemaining:{rem}",sep='\n')
