def outer():
    x=3
    def inner():
        print(x)
    inner()
    return inner
a=outer()
print(a)
print(a.__name__)