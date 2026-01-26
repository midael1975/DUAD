class AnimaL:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(AnimaL):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(AnimaL):
    def speak(self):
        return f"{self.name} says Meow!"


def get_animal_sound(animal):
    return animal.speak()

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(get_animal_sound(dog))   # Output: Buddy says Woof!
print(get_animal_sound(cat))   # Output: Whiskers says Meow!print(get_animal_sound(bird))  # Output: Tweety says Chirp!
