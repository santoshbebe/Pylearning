class myqueue():
    def __init__(self, queue_name, max_ele=5):
        self.l1 = []
        self.max_ele = max_ele
        self.queue_name = queue_name

    def print_attrib(self):
        print("The list is ", self.l1)
        print("The list is ", self.max_ele)


    def push(self):
        if(len(self.l1) < self.max_ele):
            self.l1 = eval(input("Enter the element to add to queue"))
        else:
            print("queue FULL!!!")

    def pop(self):
        if(len(self.l1)> 0):
            self.l1.pop(0)
        else:
            print("queue Empty!!!")


    def display(self):
        if (len(self.l1) > 0):
            print(self.l1)
        else:
            print("queue Empty!!!")

def main():
    max_ele = eval(input("Enter the max element for queue1"))
    while(True):
        queue_name = "queue1"
        s1 = myqueue(queue_name, max_ele)
        print("Options for ", queue_name)
        print("1. Push")
        print("2. PoP")
        print("3. Display")
        print("4. Exit")
        options = eval(input("Enter your choice"))
        if(options == 1):
            s1.push()
        elif(options == 2):
            s1.pop()
        elif (options == 3):
            s1.display()
        elif(options == 4):
            return
        else:
            print("Wrong Choice")
    #
    # s2 = myqueue("queue2")
    # s2.print_attrib()
    # s2.print_options()

main()
