numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

div_by_3 = [(x, x**2) for x in numbers if x % 3 == 0]
print(div_by_3)  # [(3, 9), (6, 36), (9, 81)]
