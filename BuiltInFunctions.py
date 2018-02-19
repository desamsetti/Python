import functools


def fahrenheit(T):
    print((9.0/5)*T+32)
fahrenheit(0)
temp = [0,22.5,40,100]
map(fahrenheit,temp)


print(list(map(lambda T:(9.0/5)*(T+32),temp)))

print(map(lambda x,y:x+y,(1,2)))


lst = [47,11,42,13]
print(functools.reduce(lambda x,y:x+y,lst))

lst = range(0,11)
print(list(filter(lambda x:x%2==0,lst)))



x=[1,2,3]
y=[4,5,6]
print(list(zip(x,y)))


a=[1,2,3,4,5,6]
b=['a','b','c','d','e','f','g','h']
print(list(zip(a,b)))


l=['a','b','c','d','e','f','g','h','i','j']

for i,item in enumerate(l):
    print((i,item))


lst = [True,True,False,False]
print(all(lst))
print(any(lst))


print(complex(2,3))
print(complex(10,1))
print(complex('10+2j'))
