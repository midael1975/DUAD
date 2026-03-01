from datetime import datetime

def multiply(a, b):
    return a * b

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("All arguments must be numbers")
        return func(*args, **kwargs)
    return wrapper

def log_calls(func):
    def wrapper(*args, **kwargs):
        date = datetime.now()
        result = func(*args, **kwargs)
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs} date:{date} Result: ", end="")
        return result
    return wrapper

@validate_numbers
@log_calls
def multiply(a, b):
    return a * b

result = multiply(3, 5)
print(result)