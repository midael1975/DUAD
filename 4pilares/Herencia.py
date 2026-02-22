class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class WalkMixin:
    def walk(self):
        return f"{self.name} is walking."


class FlyMixin:
    def fly(self):
        return f"{self.name} is flying."


class SoundMixin:
    def make_sound(self, sound):
        return f"{self.name} says {sound}"


class Dog(Animal, WalkMixin, SoundMixin):
    def speak(self):
        return self.make_sound("Woof!")


class Cat(Animal, WalkMixin, SoundMixin):
    def speak(self):
        return self.make_sound("Meow!")


class Bird(Animal, FlyMixin, SoundMixin):
    def speak(self):
        return self.make_sound("Chirp!")


def get_animal_sound(animal):
    return animal.speak()


# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

print(get_animal_sound(dog))    # Buddy says Woof!
print(dog.walk())               # Buddy is walking.

print(get_animal_sound(cat))    # Whiskers says Meow!
print(cat.walk())               # Whiskers is walking.

print(get_animal_sound(bird))   # Tweety says Chirp!
print(bird.fly())               # Tweety is flying.




# class Bird:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} says Chirp!"


# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} says Woof!"

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} says Meow!"

# class AnimalSound(Bird, Dog, Cat):
#     pass

# hybrid = AnimalSound()
# print(hybrid.speak())   # Output: Chirp!


#     # def __init__(self, animal):
#     #     self.animal = animal

#     # def make_sound(self):
#     #     return self.animal.speak()

# # Example usage
# bird= Bird("Tweety")
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# print(AnimalSound(bird).make_sound())  # Output: Tweety says Chirp!
# print(AnimalSound(dog).make_sound())   # Output: Buddy says Woof!
# print(AnimalSound(cat).make_sound())   # Output: Whiskers says Meow!print(AnimalSound(bird).make_sound())  # Output: Tweety says Chirp!