# Get the input from the user
k = int(input("Enter the position (k): "))

count = 0
num = 1

while count < k:
    if num % 3 != 0 and str(num)[-1] != '3':
        count += 1
        if count == k:
            result = num
    num += 1

# Print the result
print("The k-th element of the sequence is:", result)
