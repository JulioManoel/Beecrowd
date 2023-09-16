num = int(input())
out = 0
den = 0

for i in range(num):
  value = int(input())
  if value >= 10 and value <= 20: den += 1
  else: out += 1

print(f'{den} in')
print(f'{out} out')
