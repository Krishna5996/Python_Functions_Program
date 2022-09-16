
# function can be passed as arguments to other functions
def shout(text):
    return text.upper() 

def greet(abc):    
    print(abc("func argument"))     
  
greet(shout)
