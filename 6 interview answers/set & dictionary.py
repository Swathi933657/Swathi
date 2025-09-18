data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "country": "USA"
}

allowed_keys = {"name", "city"}

filtered = filter_dict_by_keys(data, allowed_keys)
print(filtered)
