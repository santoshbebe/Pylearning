from stack_class import mystack
from Queue_class import myqueue

def main():
    max_ele = eval(input("Enter the max element for stack"))
    stack_name = "stack1"
    print("1. to Create a stack")
    print("2. to Create a queue")

    choice = eval(input("Enter the choice"))
    if(choice == 1):
        s1 = mystack("stack0")
    elif(choice == 2):
        s1 = myqueue("queue0")
    else:
        print("Wrong Option")
        return

    while (True):
        print("Options for ", stack_name)
        print("1. Push")
        print("2. PoP")
        print("3. Display")
        print("4. Exit")
        options = eval(input("Enter your choice"))
        if (options == 1):
            s1.push()
        elif (options == 2):
            s1.pop()
        elif (options == 3):
            s1.display()
        elif (options == 4):
            return
        else:
            print("Wrong Choice")

main()