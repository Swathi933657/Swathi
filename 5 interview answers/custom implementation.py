def my_max(lst):
    if not lst:
        raise ValueError("my_max() arg is an empty list")
    maximum = lst[0]
    for x in lst[1:]:
        if x > maximum:
            maximum = x
    return maximum


def my_min(lst):
    if not lst:
        raise ValueError("my_min() arg is an empty list")
    minimum = lst[0]
    for x in lst[1:]:
        if x < minimum:
            minimum = x
    return minimum


def my_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total
