
class Person():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} just talked.")


michael = Person("Ndunwa")
print(michael.name)
michael.talk()
