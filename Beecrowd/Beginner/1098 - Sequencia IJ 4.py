i = 0
j = 1
aux = 0

while True:
  i_str = f'{i:.1f}' if i % 1 != 0 else f'{int(i)}'
  j_str = f'{j:.1f}' if j % 1 != 0 else f'{int(j)}'
  print(f'I={i_str} J={j_str}')

  if aux == 32:break
  aux += 1

  if aux % 3 == 0:
    i += 0.2
    j -= 1.8
  else: j += 1