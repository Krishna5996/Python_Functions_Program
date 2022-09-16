def simple():
    yield 1
    yield 2
    return 5
    yield 3
    
for values in simple():
    print(values)
print(simple())
