x = int(input())
y = int(input())

if x > y: y, x = x, y

for i in range(x+1, y):
  resto = i % 5
  if resto == 2 or resto == 3: print(i)