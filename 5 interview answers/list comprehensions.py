numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_squares = [x**2 for x in numbers if x % 2 != 0]
print(odd_squares)  # [1, 9, 25, 49, 81]
