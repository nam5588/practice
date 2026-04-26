"""Class
    (1) What is class
    (2) Ordinary vs Static properties
    (3) Special methods
"""

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
