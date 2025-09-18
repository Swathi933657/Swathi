filtered_rows = [row for row in matrix if all(x >= 0 for x in row)]
print("Rows without negatives:", filtered_rows)
# Output: [[1, 2, 3], [7, 8, 9]]
