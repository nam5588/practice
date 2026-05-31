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
