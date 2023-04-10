# 1. input for 5 ages from the user
# print out the biggest age from the user
# 2. write a function that gets name as input from the user
# until the name 'moshe' and returns a list of those names.

# 1.
ages = []

for i in range(5):
    ages.append(input("enter some age "))
print(ages)
print(max(ages))

# trying it using list comp
# ages = (input("enter age") for i in range(5))
# print(ages)

names = []
name = "str"
while name != "moshe":
    name = input("input name ")
    names.append(name)
print(names)

