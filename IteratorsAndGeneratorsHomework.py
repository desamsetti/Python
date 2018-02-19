def gensquares(N):
    for i in range(N):
        yield i**2


for x in gensquares(10):
    print(x)


import random
def rand_num(low,high,n):
#    while n!=0:
#        yield random.randint(low,high)
#        n=n-1
    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)



s = 'hello'
for let in s:
    s_iter = iter(s)


print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
#print(next(s_iter))