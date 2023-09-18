combustivel = [0, 0, 0] 

print('MUITO OBRIGADO')
while True:
  num = int(input())

  if num == 4: break
  elif 1 <= num <= 3: combustivel[num-1] += 1

print(f'Alcool: {combustivel[0]}')
print(f'Gasolina: {combustivel[1]}')
print(f'Diesel: {combustivel[2]}') 