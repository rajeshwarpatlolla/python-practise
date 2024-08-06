s={1,2,3,4,1}
# no indexing, wont consider duplicate elements

s.update([22, 33, 44])
s.remove(22)

s2 = frozenset(s)
# s2.update(1212121)
print(s, type(s), isinstance(s, set), s2)


d=1234

del d
# print(d)
