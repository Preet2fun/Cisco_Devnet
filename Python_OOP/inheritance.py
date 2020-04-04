'''Single inheritance'''


class Fruit:
    def __init__(self):
        print("I am parent class")


class Apple(Fruit):
    def __init__(self):
        super().__init__()
        print("I am child class")


Fruit1 = Apple()

'''Multiple inheritance'''


class A:
    def __init__(self):
        print("This is class A")

    def sport(self):
        print("This is a Cricket")


class B:
    def __init__(self):
        print("This is class B")

    def sport(self):
        print("This is a Football")


class C(B, A):
    def __init__(self):
        super().__init__()
        print("This is class C")


obj1 = C()
print(obj1.sport())


'''Multilevel inheritance'''


class A:
    def __init__(self):
        print("This is class A")

    def sport1(self):
        print("This is a Cricket")
    x = 1


class B(A):
    def __init__(self):
        print("This is class B")

    def sport(self):
        print("This is a Football")
    y = 2


class C(B):
    def __init__(self):
        super().__init__()
        print("This is class C")


obj1 = C()
print(obj1.x)
print(obj1.sport1())


''' Super funstion is used to call method from parent class'''


class vehicle:
    def start(self):
        print("Starting the vehicle")

    def stop(self):
        print("stopping the vehicle")


class byke(vehicle):
    def engine(self):
        super().start()
        super().stop()


byke1 = byke()
byke1.engine()
