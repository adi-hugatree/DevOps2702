my_items = [{"name": "aviel", "age": 33}, {"name": "moshe", "age": 20},
            {"name": "david", "age": 50}]

aa = [item["name"] for item in my_items] # this is called "list comprehension"
print(aa)

# list comprehension is python's gif to us that does the same thing as:
aa = []
for item in my_items:
    aa.append(item["name"])
print(aa)

# more list comp stuff:
aa = [item["name"] for item in my_items if item["age"] > 30]
print(aa)
