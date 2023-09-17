i = 1
j = 7
aux = 0
while True:
  print(f'I={i} J={j}')
  aux += 1
  if aux == 3:
    if i == 9 and j == 13: break
    i += 2
    j += 4
    aux = 0
  else: j-= 1

