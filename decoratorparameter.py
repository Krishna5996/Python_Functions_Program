def div_decorator(funn):
    def inner(x,y):
        if(y==0):
            return "enter proper value"
        return funn(x,y)
    return inner

@div_decorator
def div(a,b):
    return a/b
print(div(10,0))
