num = int(input())
soma = 0

for i in range(num):
  x, y = map(int, input().split())

  if x > y: x, y = y, x

  if x % 2 != 0: x += 1
  for j in range(x+1, y, 2):
    soma += j

  print(soma)
  soma = 0