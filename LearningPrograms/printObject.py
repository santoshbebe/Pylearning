class ABC():
    def __init__(self, ele):
        self.a = ele

    def __str__(self):
        return self.a

def main():
    obj = ABC("Python")
    print(obj)

    obj1 = ABC("PyCharm")
    print(obj1)

main()

