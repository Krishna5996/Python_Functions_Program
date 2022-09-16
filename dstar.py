def myFun(**kwargs):
    print(kwargs)
    for i, j in kwargs.items():
        print(i, j)
    
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks',second='2')
