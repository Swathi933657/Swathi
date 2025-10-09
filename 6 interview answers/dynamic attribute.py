#.Write a class that allows dynamic addition, deletion, and access of attributes using __getattr__, __setattr__, and __delattr__.

obj = DynamicAttributes()

# Add attributes dynamically
obj.name = "Alice"
obj.age = 30

# Access attributes
print(obj.name)  # Alice
print(obj.age)   # 30

# Delete an attribute
del obj.age

# Access deleted attribute (raises AttributeError)
# print(obj.age)

