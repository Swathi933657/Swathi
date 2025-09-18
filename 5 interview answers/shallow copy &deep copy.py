import copy

# Original nested list
original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)

print("\n--- Modifying inner list in original ---")
original[0][0] = 99

print("Original:", original)
print("Shallow:", shallow)   # Reflects change (shared inner list)
print("Deep:", deep)         # Unaffected (independent copy)

print("\n--- Modifying top-level structure ---")
original.append([7, 8, 9])

print("Original:", original)
print("Shallow:", shallow)   # No new sublist added (top-level only copied)
print("Deep:", deep)         # Still independent
