class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Any sound")


    def __str__(self):
        return f"{self.name} is an {type(self).__name__}, It is {self.age}\n{self.make_sound()}"


class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Lion(Mammal):
    def make_sound(self):
        print("Rooaarrr")


class Elephant(Mammal):
    def make_sound(self):
        print("Fooo")


class Parrot(Bird):
    def make_sound(self):
        print("Hello ! how do you do?")


class Eagle(Bird):
    def make_sound(self):
        print("woosh woosh")


def zoo_announcement(animals: list[Animal]):
    for animal in animals:
        print(animal)


lion = Lion("Simba", 5)
elephant = Elephant("Dumbo", 3)
parrot = Parrot("Polly", 2)
eagle = Eagle("Eddie", 4)

# Test the zoo_announcement function
animals_in_zoo = [lion, elephant, parrot, eagle]
zoo_announcement(animals_in_zoo)

