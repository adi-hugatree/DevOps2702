names = ["inbar", "lanir", "eran", "kfir", "alina"]
print(list(range(20, 1, -3)))

for name in names:
    print(name, end=" >> ")

for i in range(len(names)):
    print(names[i])

numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    if number == 3:
        continue
    if number == 2:
        break
    print(number)
else:
    print("success")

a = 0
while a < 5:
    print(a)
    a += 1
else:
    print("finished")

