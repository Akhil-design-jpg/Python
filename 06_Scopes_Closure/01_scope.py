username = "chaiaurcode"

def fun():
    # username = "chai"
    print(username)
    # if username not found it will take the global username
fun()
print(username)


x = 99

# def fun2(y):
#     z = x + y
#     return z

# print(fun2(2))

# def fun3():
#     global x

#     x = 12
# fun3()
# print(x)

def f1():
    x = 78
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


def chai(num):
    def actual(x):
        return x ** num
    return actual





f = chai(2) # value of num
g = chai(3) # value of num

print(f(3)) # value of x
print(g(3)) # value of x