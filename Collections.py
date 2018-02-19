from collections import Counter
l = [1,1,1,1,2,3,4,5,6,6,7,8]

print(Counter(l))
s="asdadwasdasdwasdwasdsadwasdassdasdw"
print(Counter(s))


s="How many times does each word show up in this sentence word word shoe up up"
words = s.split()
print(Counter(words))
c=Counter(words)
print(c.most_common(2))
print(sum(c.values()))

from collections import defaultdict
d = {'k1':1}
print(d['k1'])
d = defaultdict(object)
print(d['one'])
for item in d:
    print(item)

d = defaultdict(lambda:0)
d['two']=2
print(d['two'])
print(d)


d1 = {}
d1['a']=1
d1['b']=2
d1['c']=3
d1['d']=4
d1['e']=5
print(d1)
for k,v in d1.items():
    print(k,v)

from collections import OrderedDict
d1 = {}
d1['a']=1
d1['b']=2
d1['c']=3
d1['d']=4
d1['e']=5
print(d1)
for k,v in d1.items():
    print(k,v)


d2=OrderedDict()
d2['a']=1
d2['b']=2

d3=OrderedDict()
d3['b']=2
d3['a']=1
print(d2==d3)

from collections import namedtuple
Dog = namedtuple('Dog','age breed name')
sam = Dog(age=2,breed='Lab',name='Sammy')
print(sam.age)
print(sam[0])
print(sam[1])
print(sam[2])
