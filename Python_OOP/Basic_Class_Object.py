class NewClass:
    var1 = 'Today is sunday'

    def func(self):
        print("I like sunday")


obj1 = NewClass()
obj2 = NewClass()


print(obj1.var1)
print(obj1.func())

obj2.var1 = 'I also like monday'

print(obj1.var1)
print(obj2.var1)


class Student:
    def __init__(self, name, dep, year):
        self.name = name
        self.dep = dep
        self.year = year
        print("object of class is crated")

    def print_method(self):
        print('Name is : ' + self.name)
        print('dep is : ' + self.dep)
        print('yesr is : ' + self.year)


student1 = Student('Pratik', 'EC', '2009')
print(student1.print_method())
