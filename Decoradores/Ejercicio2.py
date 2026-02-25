def validate(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int, float):
                raise ValueError("All arguments must be integers")
        return func(*args, **kwargs)
    return wrapper

@validate
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(f"Result: {result}")
result = add_numbers(10, 20)
print(f"Result: {result}")
try:
    result = add_numbers(7, "8")
except ValueError as e:
    print(f"Error: {e}")
print(f"Result: {result}")
try:
    result = add_numbers("3", 5)
except ValueError as e:
    print(f"Error: {e}")
print(f"Result: {result}")
try:
    result = add_numbers(7, 8.5)
except ValueError as e:
    print(f"Error: {e}")
print(f"Result: {result}")
try:
    result = add_numbers(7.5, 8)
except ValueError as e:
    print(f"Error: {e}")
print(f"Result: {result}")