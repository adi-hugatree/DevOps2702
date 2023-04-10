# A: (I created them with values. Nothing will print.)
x = 0
y = 0
if x > y:
    print("BIG")
elif x < y:
    print("small")

# B: (prints loop iterations starting from 0)
for i in range(5):
    print(i)

# C: (direct approach feels repetitive but also like anything else would be equally convoluted)
season = 2
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

# D: (loop will run 10 times, last # printed is 10)

# E: Is there a better way to do this?
age = 36
last_name_initial = "N"
nis_to_usd = 0.28
fly_abroad = True
apt_number = 3

details = [age, last_name_initial, nis_to_usd, fly_abroad, apt_number]
for detail in details:
    print(detail)

result = age + nis_to_usd
print(result)

# F:
user_phone_number = input("Can I get your number baby")
print("phone number ", user_phone_number)


# G:
def printHello():
    print("hello")
    return 0


def calculate():
    res = 5 + 3.2
    print(res)

# H:


def print_name(name):
    print(name)


def halve(num):
    res = num / 2
    print(res)


# I:

def add(a, b):
    return a + b


def add_space(str1, str2):
    res_str = str1 + " " + str2
    return res_str

# CHALLENGES
# K:


for i in range(6):
    for symbols in range(i):
        print("#", end="")
    print(end="\n")


# L:

# this one messed with my head.

# M:


def get_num():
    res = input("number?")
    return res


def silly_add():
    user_input = get_num()
    int_broken = [int(digit) for digit in str(user_input)]
    silly_sum = 0
    for num in int_broken:
        silly_sum += num
    print(silly_sum)


silly_add()
