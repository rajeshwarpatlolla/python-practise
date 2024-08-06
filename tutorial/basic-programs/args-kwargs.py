def fn(a, *args, **kwargs):
  print(a,args, kwargs)

  for i in args:print(i)
  for i in kwargs:print(i, kwargs[i])


fn(10, 20, 30)

fn(1, 2, 3, b=1, c=2)
