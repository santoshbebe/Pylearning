my_stack = []

def my_push(my_stack):
    ele = eval(input("Enter the element to push"))
    my_stack.append(ele)
    return my_stack

def my_pop(my_stack):
    my_stack.pop()

def main():
    while(True):

        print("1. Push")
        print("2. PoP")
        print("3. Display")
        print("4. Exit")
        choice = eval(input("Enter your Choice"))
        if(choice == 1):
            print("Entering Push method")
            my_push(my_stack)
            print(my_stack)
        elif (choice == 2):
            print("Entering Push method")
            my_pop(my_stack)
            print("pop", my_stack)
main()