while True:
  media = 0
  i = 0

  while True:
    num = float(input())

    if 0 <= num <= 10:
      media += num
      i += 1
    else: print('nota invalida')

    if i == 2: break

  print(f'media = {media/i:.2f}')
  
  while True:
    print('novo calculo (1-sim 2-nao)')
    op = int(input())
    if op == 2 or op == 1: break

  if op == 2: break 