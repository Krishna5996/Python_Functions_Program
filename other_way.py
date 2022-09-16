
def decorator_func(x, y):
 
    def Inner(func):
 
        def wrapper(*args, **kwargs):
            print("I like python")
            print("Summation of values - {}".format(x+y) )
 
            func(*args, **kwargs)
             
        return wrapper
    return Inner
 
 
# Not using decorator
def my_fun(*args):
    for ele in args:
        print(ele)
 
# another way of using decorators
decorator_func(1, 45)(my_fun)('ai', 'ml', 'dl')









