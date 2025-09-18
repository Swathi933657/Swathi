# Define the functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Dispatcher function
def dispatch(command, *args):
    commands = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    
    func = commands.get(command)
    if not func:
        return f"Unknown command: {command}"
    
    return func(*args)
