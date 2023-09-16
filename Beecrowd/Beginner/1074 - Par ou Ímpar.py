num = int(input())

for i in range(num):
  n = int(input())
  
  if n % 2 == 0: par = 'EVEN'
  else: par = 'ODD'

  if n > 0 : print(f'{par} POSITIVE')
  elif n < 0: print(f'{par} NEGATIVE')
  else: print('NULL')