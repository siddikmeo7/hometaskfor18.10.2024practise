def log_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Calling function: {func}")
        print(f"Arguments: {args}, {kwargs}")
        print(f"Returned: {result}")
        return result
    return wrapper


@log_calls
def add(a, b):
    return a + b

@log_calls
def greet(name):
    return f"Hello, {name}!"


add(3, 2)
greet("John")
