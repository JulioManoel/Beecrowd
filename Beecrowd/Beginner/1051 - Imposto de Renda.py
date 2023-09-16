num = float(input())

if num <= 2000: print('Isento')

else:
  if num > 4500: imposto = (num - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
  elif num > 3000: imposto = (num - 3000) * 0.18 + (1000 * 0.08) 
  else: imposto = (num - 2000) * 0.08
  
  print(f'R$ {imposto:.2f}')
