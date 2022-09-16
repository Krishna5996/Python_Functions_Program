def m():    
    yield 1
    yield 2
    yield 3
    yield 4
a=m()
for i in range(4):
    print(a.__next__())
