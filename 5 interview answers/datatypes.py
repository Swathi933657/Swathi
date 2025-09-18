def count_types(data_list):
    type_counts = {}
    for item in data_list:
        item_type = type(item).__name__  # get type name as string (e.g., 'int', 'float', 'str', 'bool')
        type_counts[item_type] = type_counts.get(item_type, 0) + 1
    return type_counts


# Example usage:
data = [1, 2.5, "hello", True, 42, "world", False, 3.14, 100]
print(count_types(data))
