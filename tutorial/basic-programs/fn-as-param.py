def fn1():
  return 1

def fn2(a):
  return a()+2

print(fn2(fn1))
