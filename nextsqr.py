def nextsqurae():
    i=1
    while True:
        yield i*i
        i+=1

for num in nextsqurae():
    print(num)
