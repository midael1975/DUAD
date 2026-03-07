def repeat_twice(func):
    def wrapper(*args, **kwargs):
        #result = func(*args, **kwargs)
        #result = func(*args, **kwargs)
        #return result, result
        for _ in range(2):
            func(*args, **kwargs)
    return wrapper

@repeat_twice
def greet(name):
    print(f"Hola, {name}!")
greet("Juan")
