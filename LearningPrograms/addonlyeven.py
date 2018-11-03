# num = eval(input("Enter the number"))
# if(isinstance(num, int)):
#     l1 = list(range(0,10,2))
#     print(l1)
#     print(sum(l1))

# print(list(range(0,100,7)))

# t1 = (1,2,3,4,5,6,8)
num = eval(input("Enter the number"))
if(isinstance(num, int)):
    for i in range(0,num,2):
        if(not i%3 == 0):
            print(i)

    # for i in range(0,num,2):
    #     for j in range(1,num,2):
    #         print(i,j)