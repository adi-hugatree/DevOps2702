a = "avielush" # changed for git branch demo
b = "buskila"
print(a + " " + b)  # allocates every time and clean afterwards, can create memory issues
print(f"{a} {b}")
print("%s %s" % (a, b))
print("{0} {1}" .format(a, b))  # this makes it more predictable for the interpreter
# just be consistent with how you choose to print

print("name: {} lname: {}" .format(a, b))

aaa = "bbb" # just added for git branch demo