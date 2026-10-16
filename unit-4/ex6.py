''' 6. Write a program to demonstrate method overriding and polymorphism. '''

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_animal_speak(animal_obj):
    animal_obj.speak()

print("=== Method Overriding ===")
obj = Animal()
dog = Dog()
cat = Cat()

obj.speak()
dog.speak()
cat.speak()

print("\n=== Polymorphism ===")
make_animal_speak(dog)
make_animal_speak(cat)


''' OUTPUT :
        === Method Overriding ===
        Animal makes a sound     
        Dog barks
        Cat meows

        === Polymorphism ===     
        Dog barks
        Cat meows
'''