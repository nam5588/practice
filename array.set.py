''' Array & Set
    (1) Array
    (2) Set
    (3) Specific oprators with set
'''

from array import array
print("===== Array =====")

numbers = array('i', [1, 4, 9, 17, 23, 45])

print('numbers(1): ', numbers)

numbers.append(100)
numbers.insert(1, 2)

print('numbers(2): ', numbers)

numbers.remove(2)
numbers.pop()

print('numbers(3): ', numbers)

del numbers[1:3]

print('numbers(4): ', numbers)
print('\n\n\n')


print("===== Set =====")
# { set } of unique collection without keeping order!
new_numbers = array('i', [1, 4, 9, 7, 4, 1, 3, 4, 5])
numbs_set = set(new_numbers)
print(f'numbs_set: {numbs_set} and type: {type(numbs_set)}')

numbs_set.add(200)
print('numbs_set(1): ', numbs_set)

numbs_set.add(4)
print('numbs_set(2): ', numbs_set)
print('\n\n\n')


print("===== Secific oprators with set =====")
# | & - ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b # union
result2 = a & b # intersection
result3 = a - b # difference
result4 = a ^ b # symemetric difference

print(result1)
print(result2)
print(result3)
print(result4)

print('\n')
