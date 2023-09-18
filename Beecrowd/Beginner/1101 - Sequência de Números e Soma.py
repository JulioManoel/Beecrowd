while True:
  value = 0
  m, n = list(map(int, input().split()))

  if m > n: n, m = m, n
  if m <= 0: break

  for i in range(m, n+1):
    print(f'{i} ', end='')
    value += i

  print(f'Sum={value}')