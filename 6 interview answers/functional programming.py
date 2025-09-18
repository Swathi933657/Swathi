#.Use map, filter, and reduce to process a list of numbers: double the even numbers, filter out numbers less than 10, and compute the product of the remaining numbers.
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Double the even numbers
doubled = list(map(lambda x: x * 2 if x % 2 == 0 else x, numbers))
print("Doubled evens:", doubled)
# Output: [1, 4, 3, 8, 5, 12, 7, 16, 9, 20]

# Step 2: Filter out numbers less than 10
filtered = list(filter(lambda x: x >= 10, doubled))
print("Filtered >= 10:", filtered)
# Output: [12, 16, 20]

# Step 3: Compute the product of remaining numbers
product = reduce(lambda x, y: x * y, filtered)
print("Product:", product)
# Output: 3840
