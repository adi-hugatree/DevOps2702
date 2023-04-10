# ASSIGNMENT 3
from PIL import Image

# 1, 2:

try:
    a = 1/0
except ZeroDivisionError as e:
    print("Cannot divide by zero", e.args)

#3: legal but doesn't really make sense bc no excption handling

try:
    x = 1
finally:
    print("finally")

# 4: I don't think it will catch any exceptions.
# The syntax makes you expect exception handling
# but then nothing happens.

# 5: The "scope" for "except:" opens but there's nothing in it.

# 6:
# except IOError can handle user input errors
# except ZeroDivisionError can handle the error of zero in the denominator

# 7 creating words.txt
my_file = open("words.txt", "w")
my_file.close()

# 8:
my_file = open("words.txt", "w")
my_file.write("adi")
my_file.close()

# 9:
my_file = open("words.txt", "r")
name_from_file = my_file.readline()
print(name_from_file)
my_file.close()

# 10:
my_file = open("words.txt", "a")
my_file.newlines
try:
    my_word = my_file.write("יופי")
except BaseException as e:
    print("error, ", e.args)
try:
    print(my_word)
except BaseException as e:
    print("error, ", e.args)
my_file.close()

# 11: CHALLENGE:

w = 300
h = 300
hot_pink = (227, 28, 121)
img = Image.new(mode = "RGB", size = (w, h), color = hot_pink)
img.show()




