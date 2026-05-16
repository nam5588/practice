""" Tuples
    (1) What is tuple: type vs list
    (2) Unpacking arguments
    (3) zip
"""

print("====== What is tuple: type vs list ======")
# Java/Php/NodeJS = Array ^ Pythonda List
#                          (Pythonda ham Array bor u boshqacharoq)


# Literal
numbs = [2, 4, 6, 8]
# car_dic = {'brand': 'ferrari', 'year': 2026}

# Constructor
letters = list("Hello Uzbekistan!")
# mentor_dict = dict(name="Martin", age=36)

# print(numbs)
print()
# print(letters)

fruits = ["apple", "lemon", "banana", "grape", "kiwi"]
print("fruits before: ", fruits)
fruits[2] = "melon"
print("fruits after: ", fruits)

"""LISTDAN [] FAQRLI OLAROQ TUPLE () UMUMAN O"ZGARMAYDI"""
print()
print()
print()
animals = ('cat', 'dog', 'leon', 'giraffe')
tuple_obj = ("MIT", 38, True, "Adam")

# print(animals[0])
# animals[0] = 'bird'

names = "Andrew", "Jack"         # bu ham tuple
university = "Kookmin",          # bu ham tuple 😬

# *args - tuple


print("====== Unpaking argument ======")
groups = ['MIT', 'FLEXY', 'DEVEX', 'MG']
(x, y, *z) = groups
print(f"the x: {x} / y {y} / z: {z}\n")

# args  > tuple

print('-------')


def calculate(*args):
    total = 1
    for x in args:
        total *= x
    print(f"the type of (args) value: {type(args)}")
    print(f"the total value: {total}")
    return total


calculate(1, 7, 2, 3)
print()

print('-------')
# **kwargs  > dictionary


def intorduce(**kwargs):
    print(f"the type of (**kwargs) value {type(kwargs)}")
    print(f"Hi, I am {kwargs['name']} and I am {kwargs['age']}")


# call
intorduce(name='Justin', age=22)
intorduce(name='Shawn', age=30, single=True)
print()
