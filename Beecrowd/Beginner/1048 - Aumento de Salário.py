salario = float(input())

if salario <= 400: 
  ganho = salario * 0.15
  porcento = 15
    
elif salario <= 800:
  ganho = salario * 0.12
  porcento = 12
    
elif salario <= 1200:
  ganho = salario * 0.10
  porcento = 10

elif salario <= 2000: 
  ganho = salario * 0.07
  porcento = 7

elif salario > 2000: 
  ganho = salario * 0.04
  porcento = 4

print(f'Novo salario: {salario + ganho:.2f}')
print(f'Reajuste ganho: {ganho:.2f}')
print(f'Em percentual: {porcento} %')