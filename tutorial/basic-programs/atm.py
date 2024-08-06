import sys

op=sys.argv[1]

bal=10000

print('1.Check balance; 2.Deposit; 3.Withdraw')

if int(op) == 1:
  print(f'Your account balance is ${bal}')
elif int(op) == 2:
  print(f'Your account balance is ${bal + int(sys.argv[2])}')
elif int(op) == 3:
  print(f'Your account balance is ${bal - int(sys.argv[2])}')
else:
  print('Not matching the operations')
  