class Dog():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.breed = ""
        self.energy = 10

    def set_name(self, name):
        self.name = name
    def get_name(self):
        print(f"Name: {self.name}")

    def set_age(self, age):
        self.age = age
    def get_age(self):
        print(f"Age: {self.age}")
    
    def set_breed(self, breed):
        self.breed = breed
    def get_breed(self):
        print(f"Breed: {self.breed}")

    def give_paw(self):
        if self.energy < 5:
            print(f"{self.name} is too hungry to play")
            return None
        print("Woof!")
        self.energy -= 5

    def eat(self):
        if self.energy >= 10:
            print(f"{self.name} is full")
        else:
            self.energy += 5
            print(f"{self.name} is eating")
            print(f"Current energy: {self.energy}")
