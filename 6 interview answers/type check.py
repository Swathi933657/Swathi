#.Implement a decorator that checks the types of arguments passed to a function and raises a TypeError if they do not match the expected types.

@type_check(int, int)
def add(a, b):
    return a + b

@type_check(str, int)
def repeat(s, n):
    return s * n

print(add(5, 3))        # 8
print(repeat("Hi", 3))  # HiHiHi

# Type errors
# add(5, "3")       -> raises TypeError
# repeat(5, "Hi")   -> raises TypeError

