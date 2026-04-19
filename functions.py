''' FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''

print("<===== DEFINE (parametr) vs CALL (argument) =====>")
# Build in functions > print() type()       - ozi python tayyor qilib qo'ygan functionlar
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation! = :


# DEFINE - build
def greet(a):  # void hech nima return qilmaydi bunda (undefined) in py "None"
    print(f"How do you do, {a}")


def greeting(b):    # return bor None emas
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute
result1 = greet('Adam')
print("result1:", result1)

result2 = greeting('Justin')
print("result2:", result2)

print("<===== Keyword & default arguments =====>")

# DEFINE


def give_greet(name, age=20):           # default argument
    print("give_greet is executed")
    return f"hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name='AJAX', age=22)   # keyword argument
print("result3:", result3)

print("<===== Scope =====>")

b = 100  # 3


# DEFINE
def calculate(a, b=1):  # 2
    c = a*b     # 1
    print(f"the value of c is {c}")


# CALL
calculate(5)
