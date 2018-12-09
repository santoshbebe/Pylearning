fh = open("C:\hello.txt","a")
fh.write("Hello World")
fh.close()

fh = open("C:\hello.txt","w")
print(fh.read())
fh.close()
