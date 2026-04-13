import re


print("======== number ========")
# in Java, variable is a name of storege location!
# in Python, variable is a named reference!

count = 100
count_type = type(count)
print(f"the count : {count} and type: {count_type}")

result1 = count.bit_length()     # method
result2 = count.numerator  # state
print(result1, result2)

print("======== string ========")

course = "AI Python FullStack"
result3 = type(course)
print(f"the result (1): {result3}")

result3 = course.title()
print(f"the result (2): {result3}")

result3 = course.upper()
print(f"the result (3): {result3}")

result3 = course.lower()
print(f"the result (4): {result3}")

result3 = course.replace("FullStack", "MasterClass")
print(f"the result (4): {result3}")

print("======== boolean ========")
