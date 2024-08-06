d = {'a':1, 'b':2}

del d['b']
print(d, d.items(), d.keys(), d['a'])


for i in d.keys():
  print(i)

for i in d.values():
  print(i)
