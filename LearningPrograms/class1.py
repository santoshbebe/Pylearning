class AB():
    def __init__(self, name="zzz"):
        print("Object  created", name)
        self.name = name

    def zy(self):
        print("I am in the class AB ", self.name)

    def __del__(self):
        print("Bye bye")

def main():
    obj = AB("pop")
    obj.zy()
    # obj1 = AB()
    # obj1.zy()

    # obj.zy("pop")
    # obj.zy("pop1")
    #
    # obj1 = AB()
    # obj1.zy("pop")
    # obj1.zy("pop1")
    #
    # obj2 = AB()
    # obj2.zy("pop")
    # obj2.zy("pop1")

main()