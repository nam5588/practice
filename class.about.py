"""Class
    (1) What is class
    (2) Ordinary vs Static properties
    (3) Special methods __ @@@__
"""

from encodings.punycode import T
from hmac import new


print("======= What is class =======")
# class - blueprint object for creation!
# structure - state constructor method!


class Person:
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do yo do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}")

    @classmethod
    def explain(cls):
        print('static method property executed!')


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("Adam", 20)

# ordinary state
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()

print("======= Ordinary vs Static properties =======")
new_message = Person.message

print("new_message:", new_message)
Person.explain()

print("======= Special/magic methods =======")
# Python's most common special methods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__ ...


class Car():
    # state
    description = 'This class makes cars'

    # constructor
    def __new__(cls, *args):
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_enginee(self):
        print(f"the {self.name}, started engine!")

    def stop_enginee(self):
        print(f"the {self.name}, stopped engine!")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"

    def __call__(self):
        print("Object called as function!")
        return True


my_car = Car("SM3", 2015)
my_car.start_enginee()
my_car.stop_enginee()

print('-----')
your_car = Car("KIA", 2013)
print(your_car)  # __str__ bilan tashkil etdik aks holsa bu >=>=> <__main__.Car object at 0x104efd3d0> <=<=<= bolishi kk edi
# CALL      # __call__ orqali biz buni callable holatga keltirdik)
response = your_car()
print(response)

""""Maxsus magic methodlarni ishlatib turli amallarni bajarib olish mumkin!"""
