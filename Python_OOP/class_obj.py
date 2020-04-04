class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = "100"

    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        self.value = value

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle('ferrari', 'red', 70000.00)
car2 = Vehicle('JEEP', 'black', 50000.00)

print(car1.description())
print(car2.description())