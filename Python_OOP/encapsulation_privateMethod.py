"""
Encapsulation = Abstraction + data hiding
encapsulation means we are only going to show required part and rest will keep as private

"""


class Data:

    __speed = 0 #private variable
    __name = ''

    def __init__(self):
        self.a = 123
        self._b = 456   # protected
        self.__c = 789  # private
        self.__updatesoftware()
        self.__speed = 200
        self.__name = "I10"

    def __updatesoftware(self):
        print("Updating software")

    def updatespeed(self,speed):
        self.__speed = speed

    def drive(self):
        print("Max speed of car is : " + str(self.__speed))


num = Data()
"""print(num.a, num._b, num.__c) --> we can not directly acces __C as it is define as 
private for class and no object of that class has access to it"""

print(num.a, num._b, num._Data__c)

#print(num.__updatesoftware) --> not able to access as its proivate method

print(num.drive())
print(num._Data__speed)


num.__speed = 300
print(num.drive())

num.updatespeed(300)
print(num.drive())
