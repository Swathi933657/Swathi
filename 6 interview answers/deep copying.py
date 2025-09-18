#.Demonstrate deep copying of a list containing custom objects, ensuring that changes to copied objects do not affect the originals.
original_list = [
    Person("Alice", 25),
    Person("Bob", 30)
]

print("Original List:", original_list)
