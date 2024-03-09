print("OOPs Concepts")
'''
# Constructor
class trry:
   def constructor():
    print("Hello")
   def __init__ (self,name,age):
    self.name=name
    self.age=age
    print (f"The name of the employee is {self.name} and age is {self.age} ")
   
obj1 = trry("aj",22)
obj2 = trry("Rahul",34)
obj3 =  trry("John",56)
print(trry.constructor(obj1))
'''

#inheritance
class explain:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        return self.num1 + self.num2

class ppt(explain):
    def multiply(self):
        return self.num1 * self.num2

    def printt(self):
        print(f"The sum of a and b is: {self.add()}")
        print(f"The product of a and b is: {self.num1 * self.num2}")


pt = ppt(99, 9)
result_multiply = pt.multiply()
print(f"The result of multiplying a and b is: {result_multiply}")


exp = explain(33, 3)
result_add = exp.add()
print(f"The result of adding a and b is: {result_add}")
