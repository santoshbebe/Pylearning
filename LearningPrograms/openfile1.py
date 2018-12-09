print("Opening the file")
fh = open("ReadmeFiles.txt",'r+')
print("Reading the files")
print(fh.tell())
fh.readlines()
fh.seek(0,1)
print(fh.tell())
fh.write("----wUNDAYSSS-----")
# fh.write("----PYTHON-----")
fh.close()


# fh = open(r"E:\Training\Batch_7Oct2018\Pylearning\LearningPrograms\temp\sample.txt",'r')
