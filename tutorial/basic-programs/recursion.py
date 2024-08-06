total=1

def fn1(arg):
  globals()['total']*=arg
  # print(globals()['total'])
  arg -= 1
  if arg>0:
    fn1(arg)
  return globals()['total']

print(fn1(5))
