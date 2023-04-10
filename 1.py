print("Hello, world!")
a = 4
b = 5
c = "aviel"
d = True
my_list = ["aviel", "buskila", 33, True]
my_dict = {"fname": "aviel",
           "lname": "buskila",
           "age": 33,
           "is_married": True}
my_tuple = ("aviel", "buskila", 33)  # tuples are immutable

print(a + b)
print(my_list[0])
my_list[2] = 34  # doing this can fuck with performance
print(my_list)

print(my_dict["fname"])

