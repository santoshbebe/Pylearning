def addNnumbers(add_list):
    return sum(add_list)


def main():
    add_list = []
    num = eval(input("Enter the number of values to add"))
    count = num
    while(count!= 0):
        ele = eval(input("Enter the number"))
        add_list.append(ele)
        count = count - 1
    print(addNnumbers(add_list))

main()