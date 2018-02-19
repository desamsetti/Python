s = 'This is a global variable'

print(globals()['s'])

def hello(name= "Jose"):
    return "hello " + name;

print(hello())
greet = hello
print(greet())
del hello
print(greet())
