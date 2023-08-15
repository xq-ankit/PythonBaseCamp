# a way of opening file by giving the path with forward slash
File_Name=open("E:\Code\Python Programming\File Handling\\ankit.txt", "w+")
File_Name.writelines(["Ankt is my name \n","mother fuckers\n","fuck your mom"])
File_Name.seek(0)
r=File_Name.read()
print(r)
File_Name.close()

