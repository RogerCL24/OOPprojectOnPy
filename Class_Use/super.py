class Pet:
    def __init__(self, name):
        self.name = name
    
    def play(self):
        print(f"The pet {self.name} is playing!")

class Dog(Pet):
    def ___init__(self, name, race):
        super().__init__(name)
        self.race = race
        
    
    def play(self):
        super().play()
        print(f"He/She is {self.race} and is playing with his toy bone")

class DomesticDog(Dog):
    def __init__(self, name, race, owner):
        super().__init__(name, race)
        self.owner = owner
        
    def play(self):
        super().play()
        print(f"You have a nice dog {self.owner}, he/she running vividly all the way")

dom_dog = DomesticDog("Max", "Pastor aleman", "John Doe")

dom_dog.play()