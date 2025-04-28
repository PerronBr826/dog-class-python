class Dog:
    """A simple attempt to model a dog.... Wow"""

    def __init__(self, name, age):
        """Initialize name and attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate dog sit"""
        print(f"Wow! {self.name} is now sitting!")

    def roll_over(self):
        """simulate dog roll"""
        print(f"Wow! {self.name} is now rolling!")


my_dog = Dog('Buddy', 3)
print(f"My dog, {my_dog.name}, is {my_dog.age} years old.")
my_dog.sit()


robert_dog = Dog('Robert', 3)
print(f"robert dog, {robert_dog.name}, is {robert_dog.age} years old.")
robert_dog.roll_over()