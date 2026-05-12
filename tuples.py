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

print(animals[0])
animals[0] = 'bird'


print()
print()
print()