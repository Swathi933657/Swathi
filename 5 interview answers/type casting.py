def cast_list(values, target_type):
    result = []
    for v in values:
        try:
            result.append(target_type(v))
        except (ValueError, TypeError):
            # If conversion fails, keep original value
            result.append(v)
    return result

# Example usage
data = ["10", "20.5", "abc", True, None]

print(cast_list(data, int))   # [10, 20, 'abc', 1, None]
print(cast_list(data, float)) # [10.0, 20.5, 'abc', 1.0, None]
print(cast_list(data, str))   # ['10', '20.5', 'abc', 'True', 'None']
print(cast_list(data, bool))  # [True, True, 'abc', True, None]
