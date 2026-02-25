def log_parameters(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(f"Result: {result}")
result = add_numbers(a=10, b=20)
print(f"Result: {result}")
result = add_numbers(7, b=8)
print(f"Result: {result}")


