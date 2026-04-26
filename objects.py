"""OBJECTS
    (1) What us object
    (2) Iterable objects & Range
    (3) DICTIONARY
    (4) Error handling
"""

import array
import math

print("======== What is Object ========")
# An object has state and methods
# Eveting is object in PYTHON!

print(type("Hello Python"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Programming Paradigm > Functional + OOP
# OOP concepts > Abstraction | Encapsulation | Inheritence | Polimorphism

result1 = math.ceil(97.7)
print("result1:", result1)
result2 = math.ceil(98.7)
print("result2:", result2)
# print("-----------")

print("======== Error handling system ========")

car_dict = dict(name="Toyota", year=2026, electric=True)


try:
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No data - state property found:", err)
except AttributeError as err:
    print("No data - state property found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")
