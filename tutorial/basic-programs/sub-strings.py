a = "This is a very big bus. This bus has 100 paasengers capacity. This is a very big bus. This bus has 100 paasengers capacity."

index=-1

while True:
  index = a.find('is', index+1, len(a))
  if(index < 0):
    break
  else:
    print('Found at: ', index)
