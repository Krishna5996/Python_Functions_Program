def upper_d(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

def split_d(fun):
    def wrapper():
        str2=fun()
        return str2.split()
    return wrapper



@split_d
@upper_d
def modify_str():
    return "good morning"

print(modify_str())
