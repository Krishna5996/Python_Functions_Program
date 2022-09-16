def m1():
    x='hi'
    def m2():        
        global x
        x='hello'
    m2()
    return x
print(m1())
 
