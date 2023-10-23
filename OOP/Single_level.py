class Animal:
  def speak(self):
    print("Animal is speaking")
class Dog(Animal):
  def bark(self):
    print("Dog is barking")

d=Dog()
d.bark()         # Dog is barking
d.speak()        # Animal is speaking
