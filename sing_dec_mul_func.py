def divisionzero(func):
    #print("inside decorator")
    def wrapper(*args):
        #print("inside nested")
        lis=[]
        lis=args
        for i in lis[1:]:
            if(i==0):
                return "give proper input"
        return func(*args)
    return wrapper
    
@divisionzero
def div(a,b):
    #print("inside nested 2 param function")
    return a/b
print(div(0,1))


@divisionzero
def div(a,b,c):
    #print("inside nested 3 param function")
    return a/b/c
print(div(0,7,5))






