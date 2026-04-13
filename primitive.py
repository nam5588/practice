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
