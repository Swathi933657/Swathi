data = [10, -5, "abc", 20, 0]
divisor = 5

results, error_log = process_values(data, divisor)

print("Results:", results)
print("Errors:")
for err in error_log:
    print("-", err)
