# import numpy as np

# # # Create the initial 8x3 array
# # arr = np.arange(10, 34).reshape(8, 3)

# # print("Initial 8x3 Array:")
# # print(arr)
# # print()

# # # Split the array into 4 equal-sized subarrays
# # subarrays = np.split(arr, 4)

# # print("Subarrays:")
# # for sub in subarrays:
# #     print(sub)
# #     print()
    
# # arr=np.arange(10,34).reshape(8,3)
# # print(arr)
# # sub=np.split(arr,4)
# # for i in sub:
# #     print(i)
# #     print()
# # Get the dimensions of the matrices from the user
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# # Get the elements for matrix1
# matrix1 = [[int(input(f"Enter element at position ({i+1}, {j+1}) for matrix1: ")) for j in range(cols)] for i in range(rows)]

# # Get the elements for matrix2
# matrix2 = [[int(input(f"Enter element at position ({i+1}, {j+1}) for matrix2: ")) for j in range(cols)] for i in range(rows)]

# # Print the matrices
# print("Matrix1:")
# for row in matrix1:
#     print(row)

# print("Matrix2:")
# for row in matrix2:
#     print(row)
# result=np.dot(matrix1,matrix2)
# print("result\n",result)
import math as m
print(m.floor(2.96))