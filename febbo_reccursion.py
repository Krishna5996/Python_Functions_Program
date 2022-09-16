def fib(n,start,end):
    
    if n-1==0:
      return end
    
    if n>0:     
     temp=end      
     end=start+end
     return fib(n-1,temp,end)
 

print(fib(2,0,1))
