positivo = 0
media = 0
for i in range(6):
  num = float(input())
  if num > 0:
    media += num
    positivo += 1

print(f'{positivo} valores positivos')
print(f'{media/positivo:.1f}')