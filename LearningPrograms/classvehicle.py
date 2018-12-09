class VEHICLE():
    def __init__(self,name):
        print("Object Created", name)
        self.name = name
        self.color = "Red"
        self.fuel = "Petrol"
        self.wheels = 4

    def start_engine(self):
        print("Engine Started for", self.name)
        print(self.color)
        return True

    def stop_engine(self):
        print("Engine Stopped")
        return True


def main():
    obj = VEHICLE("POP")
    obj.start_engine()


    obj = VEHICLE("POP1")
    obj.start_engine()
    print(obj.name)



main()
