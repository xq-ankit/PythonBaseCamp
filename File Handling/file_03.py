# here we are create a file everytime code runs as w+(write and read)
# mode is being used 
f=open("our.txt", "w+")
f.write("ankit is \n a boy\n iam \n")
#takes the cursor to 0th position:begining of the file
#as write mode took the cursor at the end of the file



# f.seek(0)
# read=f.read()
# print(read)
# f.close()  #file is been closed
# f.seek(0)  # throws an error as file is already closed!