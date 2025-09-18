def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))  # recursive call
        else:
            result.append(item)
    return result
