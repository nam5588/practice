''' OPERATION & CONDITIONS
    (1) Operators
    (2) Condition
    (3) Logical Operators
'''
print("====== Operators ======")
# + - > >= < <= == */  // % += -= **

a = 19
b = 5

result = a // b
left = a % b

print(a / b)
print(f"the result: {result} and left: {left}")

a = a + 100
print(f"a: {a}")

print(f"b**2: {b**2}")
print(f"b**3: {b**3}")

print("=" * 10)

c = dict(name="Adam", age=20)
d = dict(name="Adam", age=20)
e = c

print(f"c==d: { c == d }")
# NODEJS da reference solishitirilsa
# PYTHON da objning qiymatni ozi solishitiriladi
print(id(c), id(d))
print("=" * 10)
print(f"c-ref: {id(c)}")
print(f"d-ref: {id(d)}")
print("=" * 10)
print(f"e-ref: {id(e)}")
print("=" * 10)

print("c is d:", c is d)
print("e is c:",e is c)