num = int(input())

if num % 2 == 0: num += 1
for i in range(2, num, 2):
  print(f'{i}^{2} = {i**2}')