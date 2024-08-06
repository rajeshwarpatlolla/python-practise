a=1

def getSum(val):
  a=2
  b=3
  print(a+b+val+globals()['a'])

x=getSum
x(4)
# print(b)
