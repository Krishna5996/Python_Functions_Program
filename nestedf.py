w=11
def a():
    x=12     
    def b():        
        y=13 
        
        def c():
            #nonlocal z
            z=14            
            q=w+1
             
        c()
    b()
a() 
print(w,x,y)

        
    
