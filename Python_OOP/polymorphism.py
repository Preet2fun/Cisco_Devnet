"""
polymorphism means we are having two different class with same methods but having different
behavior
"""


class Shark:
    def swim(self):
        print("shark can swim")

    def bones(self):
        print("shark having soft bones")


class Clownfish:
    def swim(self):
        print("clown fish can swim")

    def bones(self):
        print("clown fish having hard bones")


S1 = Shark()
C1 = Clownfish()

for fishes in (S1, C1):
    print(fishes.swim)
    print(fishes.bones)

print(S1.swim())
print(S1.bones())
print(C1.swim())
print(C1.bones())
