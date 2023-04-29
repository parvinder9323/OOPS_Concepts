class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll(self):
        print(f"{self.name} is now rolling")


my_dog = Dog("Danny", 10)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")

# Calling a Method

my_dog.sit()
my_dog.roll()

your_dog = Dog("Jimmy", 9)
print("-------------------------------------")
print(f"My dog's name is {your_dog.name}.")
print(f"My dog's age is {your_dog.age}.")
your_dog.sit()








