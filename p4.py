#Accepting file name and printing its extension
file_name = input("Input the filename : ")
x=file_name.split(".")
print("The extension of the file is : " + repr(x[1]))
