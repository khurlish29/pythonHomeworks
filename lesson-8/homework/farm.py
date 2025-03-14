class Animal:
    def __init__(self, species, sound, food):
        self.species = species
        self.sound = sound
        self.food = food

    def make_sound(self):
        print(f"{self.species} says {self.sound}.")

    def eat(self):
        print(f"{self.species} is eating {self.food}.")

    def sleep(self):
        print(f"{self.species} is sleeping.")

class Cow(Animal):
    def __init__(self):
        super().__init__("Cow", "Moo", "grass")

    def produce_milk(self):
        print("The cow is producing milk.")

class Chicken(Animal):
    def __init__(self):
        super().__init__("Chicken", "Cluck", "corn")

    def lay_egg(self):
        print("The chicken laid an egg.")

class Horse(Animal):
    def __init__(self):
        super().__init__("Horse", "Neigh", "hay")

    def run(self):
        print("The horse is running fast.")

cow = Cow()
chicken = Chicken()
horse = Horse()
