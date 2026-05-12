"""LOOP Operators
    (1) for
    (2) break/else
    (3) while
"""

print("===== for operator =====")
# Iterable objects > string dict tuple list range map filter
text = "MIT"
numbs = [10, 5, 3, 1]
car_obj = dict(brand='ferrari', year=2025)
range_obj = range(5)  # [0, 1, 2, 3, 4]

for letter in text:
    print(f"the letter: {letter}")

print("-----")

for number in numbs:
    print(f"the number: {number}")

print("-----")

for x in range_obj:
    print(f"the x: {x}")

print("-----")

for key in car_obj:
    print(f"the key: {key} ===> value: {car_obj.get(key)}")

print("-----")

for x in range(1, 20, 5):   # (start, end, step)
    print(f"the x: {x}")

print()
print()
print()
print("===== break / else =====")
for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print('Reached break')
        break
else:
    print('looped successfully')

print()
print()
print()
print("===== while operation =====")
number = 40
while number > 0:
    number -= 10
    print(f"the number equals: {number}")

print('------')
count = 0
while True:
    count += 1
    x = int(input("Find number: "))    # inputdan kiruvchi mantiq String bo'ladi

    if x == 41:
        print(f"Niceeee ⚡️, you found number in {count} steps")
        break
    elif x < 41:
        print(f'Nooo 😬, try again [Hint: bigger than {x}]')
    elif x > 41:
        print(f'Nooo 😬, try again [Hint: smaller than {x}]')