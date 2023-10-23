# method overiding in python inheritance 

class Animal:
    name="Herbivorous"
    
    def eat(self):
        print("Animal will eating")
    
    def eat(self,food):                         # method overiding
        print(f"This Animal will eat {food}")
        
class Dog(Animal):
    name = ""
    
    def eat(self):
        print(f"{self.name} is eating")
        
    def eat(self,f,foo):                        # method overiding
        super().eat(f)
        print(f"{self.name} is an {super().name} eating {foo}") 
         

lab= Dog()
x=Animal()
#x.eat("vegiterian")
#x.eat()
lab.name="gunda"
#lab.name="pummy"
lab.eat("veg","bone")
#lab.eat()
#print(x.name)

