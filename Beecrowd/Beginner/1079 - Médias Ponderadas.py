num = int(input())

for i in range(num):
  value = list(map(float, input().split()))

  value = ((value[0] * 2) + (value[1] * 3) + (value[2] * 5)) / 10
  print(f'{value:.1f}')