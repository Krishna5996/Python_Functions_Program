'''
def ddugky(func):
    def inner():
        str11=func()
        str11=str11+' student'
        return str
    return inner
'''
def outer(func):
    def inne():
        str1=func()
        return str1.upper()
    return inne
'''
#@ddugky
@outer
'''
def modify_str():
    return "good morning"
print(modify_str())
print(modify_str())
'''
a=outer(modify_str)
print(a())
'''









#print(returned_inner())

