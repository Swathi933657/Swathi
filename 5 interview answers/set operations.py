def list_set_operations(list1, list2):
    s1, s2 = set(list1), set(list2)
    
    union = s1 | s2           # or s1.union(s2)
    intersection = s1 & s2    # or s1.intersection(s2)
    difference = s1 - s2      # or s1.difference(s2)
    
    return {
        "union": list(union),
        "intersection": list(intersection),
        "difference": list(difference)
    }

# Example
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7]

result = list_set_operations(l1, l2)
print(result)
