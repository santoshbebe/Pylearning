class ABC():
    def __init__(self, ele):
        self.a = ele

    def __str__(self):
        return self.a

    def __add__(self, other):
        return ABC(self.a + other.a)

def main():
    obj1 = ABC("Python")
    print(obj1)

    obj2 = ABC("PyCharm")
    print(obj2)

    obj3 = obj1 + obj2
    print(obj3)

main()

