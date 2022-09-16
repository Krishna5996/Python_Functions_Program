

def decorator_outer(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

def decorator_outer1(func):
    def wrapper():
        str1=func()
        return str1.split()
    return wrapper

@decorator_outer1
@decorator_outer
def modify_str():
    return "happy new year"

print(modify_str())
