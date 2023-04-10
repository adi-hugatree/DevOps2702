my_file = open("my_file.txt")
for line in my_file.readlines():
    print(line)


def append_name_to_file(name, filename):
    name = " " + name
    temp_file = open(filename, "a")  # append puts the cursor at the end of the file for adding stuff
    temp_file.write(name)
    temp_file.close()


with open("names.txt") as my_file:  # my file is available only in the scope of this little script
    for line in my_file.readlines():
        print(line)



def greet(filename):
    temp_file = open(filename, "r")
    for name in temp_file:
        print("Have a blessed day, ", name)
    temp_file.close()

append_name_to_file("aviel", "names.txt")
greet("names.txt")



