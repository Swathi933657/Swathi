template = "Hello {name}, you have {points} points and {bonus} bonus."
data = {"name": "Alice", "points": 120}

result = format_template(template, data)
print(result)
