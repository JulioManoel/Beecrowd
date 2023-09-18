num = int(input())
j = 1
for i in range(1, num*2+1):
  if i % 2 == 0: 
    print(f'{j} {j**2+1} {j**3+1}')
    j += 1

  else: print(f'{j} {j**2} {j**3}')