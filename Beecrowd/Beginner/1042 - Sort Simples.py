order = list(map(int, input().split()))
num = order.copy()
order.sort()

for i in range(3):
  print(order[i])

print()

for i in range(3):
  print(num[i])