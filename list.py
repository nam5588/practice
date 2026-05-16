""" List
    (1) Working with list
    (2) List methods
    (3) Lambda function
    (4) enumarate, map and filter
"""
import numbers
from pickle import TRUE


print("====== Working with list ======")
# Java / PHP / NodeJS = Array Pythonda List

# literal
person = {'name': 'Justin', 'age': 25}      # dictionary
people = ('Andrew', 'Justin', 'Michael')    # tuple
groups = ['MIT', 'FLEXY', 'DEVEX', 'MG']    # list
for team in groups:
    print(f"The team: {team}")

print()

# constructor
result = list('Welcome Namangan!')
print(f"The result: {result} and size: {len(result)}")

print()
print('-----------')
fruits = ['apple', 'melon', 'strawbery', 'orange']

a = fruits[0]
b = fruits[0:2]  # [0:2] 2 arg'gacha
c = fruits[::3]  # toliq 3 qadamda
d = fruits[::-1]  # teskarimachasi

print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)
print()

print("====== List methods ======")
# methods: append() insert()  pop()  remove()   clear()   sort()     < mutable
# index() sorted()                                                   < immutable

letters = ['a', 'd', 'e']

letters.append('c')  # add behind
print(f"The append letters: {letters}")

letters.insert(0, 'z')  # add front     - index > add
print(f"The insert letters: {letters}")

size = len(letters)-1
result1 = letters.pop(size)  # pop behind
print(f"The pop: {result1} letters: {letters}")

result2 = letters.pop(0)  # pop front or index
print(f"The pop: {result2} letters: {letters}")

print('-----------')
animals = ['dog', 'cat', 'zebra', 'fish', 'leon', 'snake']
print('animals:', animals)

animals.remove('leon')
print('animals remove:', animals)

del animals[2:4]    # 2 dan 4 gacha [2,3]
print('animals delete:', animals)

exist = animals.index('cat')
print('cat exist:', exist)

animals.clear()
print('animals clear:', animals)

if 'cat' in animals:
    print('index of cat:', animals.index('cat'))
else:
    print('cat not exist')

print()
print('-----------')

numbers = [2, 32, 20, 4, 7, 8, 16]
numbers.sort()
print('sort default numbers:', numbers)

numbers.sort(reverse=True)
print('sort reverse numbers:', numbers)

# immutable sorted
numbs = [20, 14, 3, 12, 10]
new_numbs = sorted(numbs)
print(f'sorted numbs: {numbs} and new_numbs: {new_numbs}')

print()

print("====== Lambda function ======")
# Lambda is small anonymus functions!


def calc(x, y): return x*y


result = calc(3, 5)
print('result:', result)

people = [
    ('Justin', 26),
    ('Martin', 35),
    ('Tom', 41),
    ('Adam', 20),
    ('Robert', 23),
]

# simple sort
people.sort()   # sort by ABC -> (aplhabet)
print("people(1):", people)

# sort by age via lambda
people.sort(key=lambda person:person[1])
print("people(2):", people)


print()
