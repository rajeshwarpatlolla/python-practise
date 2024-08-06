def fn1(a):
  def fn2(b):
    return b
  return a+fn2(2)

print(fn1(1))
