from functools import reduce
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
#using lambda
print(reduce(lambda a, b: a+b, lis))
