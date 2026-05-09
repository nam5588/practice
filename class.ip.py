"""CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITENCE
    (3) POLIMORPHISM
"""

print("======= INHERITENCE =======")

# PARENT > CHILD [only public ande protected properties(state + method) to children!]


class Animal:  # PARENT
    # state
    description = "This class parent for animals"

    # constructor
    def __init__(self, voice):
        self.__status = 'Animal is alive'
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # CHILD
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("yes, i can protect")

    def make_voice(self):
        print(f"the {self.name} says {self.sound}")


class Cat(Animal):  # CHILD
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def paly(self):
        print("yes, i can play")


class Fish(Animal):  # CHILD
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("yes, i can play")


dog = Dog("Reks", "Wow", True)
cat = Cat("Tom", "Myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print('-----------')

dog.make_voice()
fish.make_voice()

# print('-----------')

# print(Animal.description)
# print(Dog.description)

# print('-----------')


# print("dog.status:", dog.__status)

print('-----------')

# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
print(f"the result: {a and b and c and d}")

# Fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data is:", data1, data2)
