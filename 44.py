a = int(input("enter number: "))
b = int(input("enter number: "))
result = 0
try:  # run the code and hope for the best but there's a safeguard
    result = a / b
except BaseException as e:
    print("something went wrong")
    print(e.args)  # tells us more about the exception that happened. Also the code keeps running.

print(result)