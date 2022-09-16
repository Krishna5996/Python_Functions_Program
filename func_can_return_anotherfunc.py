#function can return another function
def create_adder(x):
    def adder(y):
        return x+y
  
    return adder
  
add = create_adder(15)
  
print (add(10))
