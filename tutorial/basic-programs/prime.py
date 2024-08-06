a = int(input('Enter a number: '))
divs =0
for i in range(2, int(a/2)):
  if a%i == 0:
    divs+=1

if divs == 0:
  print('Prime')
else:
  print('Not Prime')
