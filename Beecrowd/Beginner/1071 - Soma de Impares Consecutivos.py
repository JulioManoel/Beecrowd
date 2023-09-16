x = int(input())
y = int(input())
soma = 0

if x > y: x, y = y, x
if x % 2 == 1: x += 1
if y % 2 == 1: y -= 1

for i in range(x+1, y, 2):
  soma += i

print(soma)