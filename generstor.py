'''Return sends a specified value back to
its caller whereas Yield can produce a sequence
of values. We should use yield when we want to iterate over a sequence,
but don’t want to store the entire sequence in memory.
'''
def m():    
    yield 1
    yield 2
    yield 3
    yield 4
a=m()
for i in range(4):
    print(a.__next__())
