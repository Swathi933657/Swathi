def parse_input_line(line: str):
    def parse_token(token: str):
        # Check for boolean
        if token.lower() == "true":
            return True
        if token.lower() == "false":
            return False
        
        # Check for int
        try:
            return int(token)
        except ValueError:
            pass
        
        # Check for float
        try:
            return float(token)
        except ValueError:
            pass
        
        # Otherwise, treat as string
        return token

    return [parse_token(token) for token in line.split()]


# Example usage:
user_input = "123 45.6 true False hello"
parsed = parse_input_line(user_input)
print(parsed)          # [123, 45.6, True, False, 'hello']
print([type(x) for x in parsed])  
# [<class 'int'>, <class 'float'>, <class 'bool'>, <class 'bool'>, <class 'str'>]

