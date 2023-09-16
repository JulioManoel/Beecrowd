pos = list(map(float, input().split()))

if pos[0] == 0 and pos[1] == 0: print('Origem')

elif pos[0] == 0: print('Eixo Y')
elif pos[1] == 0: print('Eixo X')

elif pos[0] > 0:
  if pos[1] > 0: print('Q1')
  else: print('Q4')

else:
  if pos[1] > 0: print('Q2')
  else: print('Q3')