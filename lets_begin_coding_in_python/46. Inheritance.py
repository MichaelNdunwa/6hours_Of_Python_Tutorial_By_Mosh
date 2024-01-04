
class Animal:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(f"{self.name} walks.")


class Dog(Animal):
    def bark(self):
        print("The dog is barking.")


class Cat(Animal):
    def cute(self):
        print("The cat is cute.")


dog = Dog("Dog")
dog.walk()