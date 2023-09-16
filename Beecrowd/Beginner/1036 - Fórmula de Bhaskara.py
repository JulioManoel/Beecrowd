num = list(map(float, input().split()))
a, b, c = num[0], num[1], num[2]
delta = (b**2) - (4 * a * c)

if delta < 1 or a == 0: 
  print('Impossivel calcular')

else: 
  x1 = (-b + (delta**0.5)) / (2 * a)
  x2 = (-b - (delta**0.5)) / (2 * a)
  print(f'R1 = {x1:.5f}')
  print(f'R2 = {x2:.5f}')