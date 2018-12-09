# def print_personal_details(name, age, loc):
#     print("My Name is ", name)
#     print("My age is ", age)
#     print("My loc is ", loc)
#     return None

# def print_personal_details(*args):
#     print("My Name is ", args[0])
#     print("My age is ", args[1])
#     print("My loc is ", args[2])
#     return None

# def print_personal_details(d):
#     print("My Name is ", d['name'])
#     # print("My Name is ", d[0])
#     print("My age is ", d['age'])
#     print("My loc is ", d['loc'])
#     return None
def print_personal_details(**shivraj):
    print(shivraj['name'])
    print(shivraj['age'])
    print(shivraj['loc'])

def main():
    d = {}
    name = eval(input("Enter the name"))
    age = eval(input("Enter the age"))
    loc = eval(input("Enter the loc"))
    print_personal_details(name=name,loc=loc, age=age)
    d['name'] = name
    d['age'] = age
    d['loc'] = loc
    # print_personal_details(d)

main()