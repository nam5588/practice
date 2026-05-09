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
print("e is c:", e is c)

print("====== Condition ======")
x = 5

if x > 50:
    print('case A')
elif x > 10:
    print('case B')
else:
    print('case C')

print("=" * 10)

print("====== Logical Operators ======")
age = 18
# person = None

# if age > 16:
#     person = "adult"
# else:
#     person = "child"
# print("person:", person)


""" TERNARY """
person = 'adult' if age > 18 else "minor"
print("person:", person)

print("=" * 10)

is_student = True
is_parent = False
is_guest = True
is_admin = False

if not is_student:
    print("Welcome Here, Do you want to be Student!")
elif is_admin:
    print("Please, go to this office!")
elif is_guest or is_parent:
    print("Waiting room is over there!")
else:
    print("Other cases")
    