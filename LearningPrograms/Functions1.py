def my_print_var_args(*args):
    str1 = ""
    for ele in args:
        str1 = str1 + ' ' +str(ele)
    print(str1)

def my_print(l1):
    print(l1)
    str1 = ""
    for ele in l1:
        str1 = str1 + ' ' + str(ele)
    print(str1)

my_print((1,"Python", 3.14))
my_print_var_args(1,"Python", 3.14)
