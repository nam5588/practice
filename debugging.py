'''Packages & Deebugging
    (1) Python packages & Core packages
    (2) Package Manager & External Package
    (3) Debugging
'''

import turtle
from PIL import Image


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
    print("your_content:", your_content)

print("--- DONE ---")


print('====== Package Manager & External Package ======')
''' Package Managers: Python (pip pipenv) & nodeJS (npm yarn)
    PHP > composer
    MacOS > brew
'''
# External packages > https://pypi.org/

# with Image.open('material/logo.png') as img_obj:
#     resized = img_obj.resize((200, 200))
#     resized.show()
#     resized.save("material/sample.png")
print("\n\n\n\n\n\n\n\n\n")

print('====== Debugging ======')


def get_summary(*args):     # DEFINE
    total_amount = 0
    for a in args:
        total_amount += a
    return total_amount


# CALL
res = get_summary(1, 2, 3, 4, 6)

print(res)
print("\n\n\n\n\n\n\n")

