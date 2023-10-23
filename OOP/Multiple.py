class Add:
    def addition(self,a,b):
        return a+b

# Second parent class
class Sub:
    def substraction(self,a,b):
        return a - b
        
class Mul:
    def multiply(self,a,b):
        return a * b
        
class Div:
    def Divide(self,a,b):
        return a / b
    def FloorDivision(self,a,b):
        return a // b
        
class Mod:        
    def Remainder(self,a,b):
        return a%b

# Child class inheriting from two or more parent class

class calculator(Add,Sub,Mul,Div,Mod):
    pass
        
c=calculator()
print(c.addition(1,2))
print(c.substraction(1,2))
print(c.multiply(1,2))
print(c.Divide(1,2))
print(c.FloorDivision(1,2))
print(c.Remainder(1,2))
