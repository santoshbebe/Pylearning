#Program to know while loop
i1 = eval(input("Enter the number"))
# if(isinstance(i1, int)):
#     print("Entered number is integer")
# else:
while(not isinstance(i1, int)):
    i1 = eval(input("Enter the number"))
print("i1 is integer")