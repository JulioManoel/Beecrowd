media = 0
j = 0
while True:
  value = float(input())

  if 0 <= value <= 10:
    media += value
    j += 1

  else: print('nota invalida')
  if j == 2:
    break

print(f'media = {media/j:.2f}')