def gencubes(n):
    out = []
    for num in range(n):
        out.append(num**3)
    return out


#for x in gencubes(1000000):
#   print(x)


def genfibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        #t = a
        #a = b
        #b = t+b
        a,b = b,a+b


for num in genfibon(10):
    print(num)




def fibon(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output

print(fibon(10))

def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))




s = 'hello'
for let in s:
    print(let)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))