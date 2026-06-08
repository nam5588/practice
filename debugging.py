'''Packages & Deebugging
    (1) Python packages & Core packages
    (2) Package Manager & External Package
    (3) Debugging
'''

import turtle

print('====== Python Packages & Core Package ======')
''' Python Package/Module: Core, File and External'''

# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)
# t.circle(150)

# turtle.done()

my_file = open('material/msg.txt', 'r')
try:
    content = my_file.read()
    print("my___content:", content)
finally:
    my_file.close()

print('---------------------')

# with
with open('material/msg.txt', 'r') as your_file:
    your_content = your_file.read()
    print("your_content:",your_content)
    
print("--- DONE ---")