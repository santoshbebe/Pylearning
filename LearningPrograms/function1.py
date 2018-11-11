def check_type(var1, var_type):
    if(isinstance(var1, var_type)):
        return True
    else:
        return False

def main():
    print("Hello World")
    var1 = eval(input("Enter the data"))
    ret_value = check_type(var1,int)
    if(ret_value == True):
        print("Given Input is Integer")
    else:
        print("Given Input is not an Integer")

    var1 = eval(input("Enter the data"))
    ret_value = check_type(var1, str)
    if (ret_value == True):
        print("Given Input is String")
    else:
        print("Given Input is not an string")



main()
# ret_value = main()
# print("Returned Value is ", ret_value)

# def foo():
#     print("Python")
#
# def main():
#     print("hello world")
#     foo()
# main()
# #