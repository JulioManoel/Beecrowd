par = 0
negativo = 0
positivo = 0

for i in range(5):
  num = int(input())
  if num % 2 == 0: par += 1
  if num > 0: positivo += 1
  elif num < 0: negativo += 1

print(f'{par} valor(es) par(es)')
print(f'{5-par} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')