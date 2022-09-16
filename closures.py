'''
def outer():
    x=3
    def inner():        
        print(x)    
    return inner
a=outer()
a()
'''
def outer():    
    x=3
    global x
print(x)
