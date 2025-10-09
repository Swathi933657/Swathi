1.Design a class that supports both stack and queue operations using a single list. Implement methods for push, pop, enqueue, dequeue, and peek.
Ans:A single class that can behave like both a stack (LIFO) and a queue (FIFO) using one list internally.
We’ll implement:
Stack methods → push, pop, peek
Queue methods → enqueue, dequeue, peek (same peek works for both)
✅ Uses one list internally
✅ Supports both stack & queue operations
✅ peek works, but we can decide whether to peek stack-style (last) or queue-style (first)

2.Write a function that takes a template string with placeholders and a dictionary, and returns the formatted string by replacing placeholders with dictionary values. Handle missing keys gracefully.
Ans: Takes a template string with placeholders (like "Hello {name}")
Takes a dictionary of values
Replaces placeholders with dictionary values
Handles missing keys gracefully (instead of raising KeyError)
✅ Works like str.format()
✅ Leaves missing keys untouched instead of crashing
✅ Super clean (uses SafeDict + format map)


3.Given a list containing integers, floats, and strings, write a function that sorts the list so that all numbers come before strings, and numbers are sorted numerically, strings alphabetically.
Ans:sort a mixed list (integers, floats, strings) with these rules:
All numbers (int, float) come before strings.
Numbers are sorted numerically.
Strings are sorted alphabetically.
✅ All numbers come first
✅ Numbers sorted numerically
✅ Strings sorted alphabetically

4.Create a function that takes a string command and arguments, and dispatches to the correct function (e.g., "add", "subtract", "multiply", "divide") using a dictionary of function references.
Ans: command dispatcher that:
Takes a string command and arguments
Calls the correct function based on the command
Uses a dictionary mapping commands to function references
✅ Uses dictionary of function references
✅ Handles unknown commands gracefully
✅ Supports arbitrary number of arguments using *args

5.Design a function that processes a list of values and raises custom exceptions for invalid types, negative numbers, or division by zero, and logs all errors.
Ans:a robust processing function that:
Iterates through a list of values
Performs some operation (e.g., division or calculation)
Raises custom exceptions for:
Invalid types
Negative numbers
Division by zero
Logs all errors instead of stopping execution
✅ Custom exceptions for type, negativity, division
✅ Continues processing other values
✅ Collects all errors in a log

6.Given a matrix (list of lists), use nested list comprehensions to extract the diagonal, transpose the matrix, and filter out rows containing negative numbers.
Ans:use nested list comprehensions for multiple matrix operations:
Extract the diagonal
Transpose the matrix
Filter out rows containing negative numbers
✅ Uses nested list comprehensions
✅ Extracts diagonal
✅ Computes transpose
✅ Filters rows containing negative numbers

7.Write a function that takes a dictionary and a set, and returns a new dictionary containing only the key-value pairs where the key is in the set.
Ans:✅ Uses dictionary comprehension
✅ Returns a new dictionary with only keys in the set
✅ Leaves the original dictionary unchanged

8.Implement a recursive Fibonacci function with memoization to optimize performance. Compare its speed to the naive recursive approach.
Ans:✅ Memoization drastically improves performance by storing already computed results.
✅ Works recursively and keeps code simple.

9.Create a class that implements the iterator protocol to iterate over its elements in reverse order.
Ans :custom class that implements the iterator protocol (__iter__ and __next__) to iterate over its elements in reverse order.
✅ Implements the iterator protocol
✅ Iterates in reverse order
✅ Works with any list-like sequence

10.Write a function that partitions a list into n nearly equal parts and returns a list of lists.
Ans :a function that splits a list into n nearly equal parts, returning a list of sublists.
✅ Works for any list length and any positive n
✅ Partitions are as evenly sized as possible
✅ Handles non-divisible lengths gracefully

11.Implement a decorator that checks the types of arguments passed to a function and raises a TypeError if they do not match the expected types.
Ans: type-checking decorator that:
Takes a function
Checks the types of arguments against expected types
Raises TypeError if a mismatch is found
type-checking decorator that
✅ Checks positional argument types
✅ Raises TypeError with clear message
✅ Uses functools.wraps to preserve function metadata

12.Demonstrate deep copying of a list containing custom objects, ensuring that changes to copied objects do not affect the originals.
Ans: Demonstrate deep copying with a list containing custom objects, so that modifying the copy does not affect the original list or its objects.
✅ Explanation:
copy.deepcopy() creates a completely independent copy of the list and all objects inside it.
Changes to copied_list do not affect original_list.
This is essential when working with nested or mutable objects.

13.Write a class that allows dynamic addition, deletion, and access of attributes using __getattr__, __setattr__, and __delattr__.
Ans:A class that can dynamically manage attributes using Python’s special methods: __getattr__, __setattr__, and __delattr__.
✅ Features:
Dynamic attribute addition via __setattr__
Safe access via __getattr__
Dynamic deletion via __delattr__
Uses an internal _attributes dictionary to store all custom attributes.

14.Use map, filter, and reduce to process a list of numbers: double the even numbers, filter out numbers less than 10, and compute the product of the remaining numbers.
Ans:sing map, filter, and functools.reduce.
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

Explanation
map: Doubles only even numbers, leaves odd numbers unchanged.
filter: Keeps only numbers ≥ 10.
reduce: Multiplies all remaining numbers to get the product.

