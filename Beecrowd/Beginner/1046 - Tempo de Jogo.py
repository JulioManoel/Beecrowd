num = list(map(int, input().split()))

if num[0] >= num[1]: horas = 24 + num[1] - num[0]
else: horas = num[1] - num[0]

print(f'O JOGO DUROU {horas} HORA(S)')
  