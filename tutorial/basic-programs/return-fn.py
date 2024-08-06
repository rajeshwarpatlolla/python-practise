def fn1():
  return 1

def fn2():
  return fn1

print(fn2()())
