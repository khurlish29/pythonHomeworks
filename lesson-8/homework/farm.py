class Animal:
    def __init__(self,species,sound):
        self.species=species
        self.sound=sound

    def makeSound(self):
        print(f"{self.species} says {self.sound}")

    def eat(self,food):
        print(f"{self.species} is eating {food}")

    def sleep(self):
        print(f"{self.species} is sleeping")

class Cow(Animal):
    def __init__(self):
        super().__init__("Cow","Moo")
    def produceMilk(self):
        print(f"{self.species} produces milk")

class Rooster(Animal):
    def __init__(self):
        super().__init__("Rooster","Cock-a-doodle-do")
    def alarm(self):
        print(f"{self.species} wakes farmers up in the morning")
class Hen(Animal):
    def __init__(self):
        super().__init__("Hen","Cluck")
    def eggs(self):
        print(f"{self.species} lays eggs")


class Donkey(Animal):
    def __init__(self):
        super().__init__("Donkey","Hee-Haw")
    def helper(self):
        print(f"{self.species} helps to carry heavy loads")

