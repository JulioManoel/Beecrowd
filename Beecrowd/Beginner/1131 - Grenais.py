i = 0
gremio = 0
inter = 0
empate = 0

while True:
  x, y = map(int, input().split())
  
  if x > y: inter += 1
  elif y > x: gremio += 1
  else: empate += 1
  i += 1

  print('Novo grenal (1-sim 2-nao)')
  num = input()
  if num == '2': break

print(f'{i} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')
if inter > gremio: print('Inter venceu mais')
elif gremio < inter: print('Gremio venceu mais')
else: print('Nao houve vencedor')