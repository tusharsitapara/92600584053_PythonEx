''' 8. Write a program to demonstrate encapsulation and abstraction using classes. '''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod  #Abstraction
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self):
        self.__name = "Tomy"  #Encapsulation

    def sound(self):
        print(self.__name, "barks")

d = Dog()
d.sound()


''' OUTPUT :
        Tomy barks
'''