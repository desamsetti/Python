l=[1,2,3,4,5]
print(l)
for x in l:
    print(x)

for num in l:
    print("something!")

#Modulo
print(10%3)
print(18%7)
print(4%2)


l=[1,2,3,4,5]
for num in l:
    if num%2==0:
        print(num)



l=[1,2,3,4,5]
list_sum = 0
for num in l:
    list_sum+=num
print(list_sum)


tup = (1,2,3,4,5)
for t in tup:
    print(t)



l = [(2,4),(6,8),(10,12)]
print(l)
print(l[0][0])
for tup in l:
    print(tup)


for (t1,t2) in l:
    print(t1)
    print(t2)
    print(t1-t2)



d={'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

for k,v in d.items():
    print(k,v)


