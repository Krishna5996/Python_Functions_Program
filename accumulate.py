from itertools import accumulate
import operator

lis=[1,2,3,4,5]
'''
#using operator function
z=reduce(operator.add,lis)
print(z)

#using user defined function
def addd(a,b):
    return a+b
print(reduce(addd, lis))
'''
#using accumulate
b=accumulate(lis,lambda a, b: a+b )
print(list(b))
