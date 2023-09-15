valor = 0

for i in range(2):
  peca = input().split()
  valor += float(peca[1]) * float(peca[2])

print(f'VALOR A PAGAR: R$ {valor:.2f}')