def fun1():
    print("in fun1")
def fun2(a):
    print("infun2")
    a()
fun2(fun1)