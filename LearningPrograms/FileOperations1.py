#Opening the file in write and read mode
fp = open("C:\Sample.txt", 'w+')
#Writing the first sentence
fp.write("Hi this is a test sentence")
#Moving the file pointer to the start of the file
fp.seek(0)
#Performing the read
print("1st Read", fp.read())
#Moving the file pointer to the end of file
fp.seek(2)
#Writing to the end of file
fp.write("Testing end of file writing")
#moving the filepointer to the start of the file
fp.seek(0)
#Reading the file again.
print(fp.read())
fp.close()
#fp.read()