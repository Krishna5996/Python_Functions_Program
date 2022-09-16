def global_outer(exp):
    def outer(func):
        def wrapper():
            return func()+exp
        return wrapper
    return outer

@global_outer("student")
def ordinary():
    return "good morning "
print(ordinary())
