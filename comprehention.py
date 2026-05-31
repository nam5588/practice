''' Comprehention
    (1) What is comprehention & list comp.
    (2) Set and dictionary comp.
'''


print('===== What is comprehention & list comp. =====')
# Comprehention acts lkike spread orepators!
''' Comprehention general syntax:
    a) *iterable
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>
'''

# List comp.
numbers = [1, 2, 3, 4, 6, 20]
list_numbers = [*numbers]  # a verison

print(list_numbers)
print(numbers is list_numbers)      # ref ozgargan
print(id(numbers))
print(id(list_numbers))
print('\n\n\n')

people = [('Robert', 20), ('Steve', 19), ('Joseph', 22)]
list_people = [person[0] for person in people]  # b verison
print('list_people:', list_people)
print('\n')

cars = [
    ('Ferrari', 78),
    ('Toyota', 87),
    ('Audi', 116),
    ('BMW', 109),
    ('Pagani', 33)
]
list_cars = [car[0] for car in cars if car[1] > 80] # a version
print('list_cars:', list_cars)
print('\n')

print('===== Set and dictionary comp. =====')
numbs = [1, 5, 4, 20, 4, 20, 1, 20]

set_numbs = {*numbs}
print(set_numbs)

dict_people = {person[0]: person[1] for person in people if person[1] > 20} # b/c version
print('dict_people: ', dict_people)


print('\n')
