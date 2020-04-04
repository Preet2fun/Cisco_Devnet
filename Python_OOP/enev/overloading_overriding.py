"""
overloading menas we are using same method name just we supply different parameters
overloading does not required same return type
overloading can happen in same clase or sub classes

overriding means we have to define method in sub class with same name, parameter and returen type
overriding can not be done in same class

"""

'''overloading'''

class Math:
    def add(self,type,*args):
        if type == 'int':
            result = 0
        if type == 'str':
            result = ''
        if type == 'float':
            result = 0.0
        for i in args:
            result += i
        return result

sum = Math()
print(sum.add('int',2,3))
print(sum.add('int',4,5,6))
print(sum.add('float',4.1,5.6))
print(sum.add('float',2.1,1.2,1.6))
print(sum.add('str','a','5','6'))
print(sum.add('str','My name',' is ', 'Pratik'))

'''Overriding'''

class A:
    def delta(self):
        print("I love USA")
class B(A):
    def delta(self):
        print("I love INDIA")

nation = B()

print(nation.delta())