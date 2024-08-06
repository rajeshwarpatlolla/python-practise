l = [1,2,3,4,5, 3,'test', -1, '#']
# print(l, l[3:], l[:4], l*4)

l.append(111)
l.remove(3)
del(l[1])

# l.clear()

l2 = [1,2,3,4,5]
l2.insert(1, 121212)
# print(max(l2), min(l2))
l2.sort(reverse=True)
print(l2, tuple(l2))
