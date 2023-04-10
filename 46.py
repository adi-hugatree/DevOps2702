def get_age():
    curr_age = int(input("enter your age: "))
    if curr_age < 0:
        raise BaseException("age can not be negative, fool", curr_age)


try:
    get_age()
except BaseException as e:
    print(e.args)