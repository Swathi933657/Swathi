def convert_dict_types(d: dict) -> dict:
    def convert_value(val: str):
        # Handle boolean
        lower_val = val.lower()
        if lower_val == "true":
            return True
        if lower_val == "false":
            return False
        
        # Handle int
        if val.isdigit() or (val.startswith('-') and val[1:].isdigit()):
            return int(val)
        
        # Handle float
        try:
            return float(val)
        except ValueError:
            pass
        
        # Default: keep as string
        return val

    return {k: convert_value(v) for k, v in d.items()}

# Example
data = {
    "age": "25",
    "height": "175.5",
    "active": "true",
    "name": "Alice",
    "balance": "-100",
    "note": "hello123"  # stays string
}

print(convert_dict_types(data))
# Output: {'age': 25, 'height': 175.5, 'active': True, 'name': 'Alice', 'balance': -100, 'note': 'hello123'}
