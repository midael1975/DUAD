class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Chirp!"


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Meow!"

class AnimalSound(Bird, Dog, Cat):
    def __init__(self, animal):
        self.animal = animal

    def make_sound(self):
        return self.animal.speak()

# Example usage
bird= Bird("Tweety")
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(AnimalSound(bird).make_sound())  # Output: Tweety says Chirp!
print(AnimalSound(dog).make_sound())   # Output: Buddy says Woof!
print(AnimalSound(cat).make_sound())   # Output: Whiskers says Meow!print(AnimalSound(bird).make_sound())  # Output: Tweety says Chirp!