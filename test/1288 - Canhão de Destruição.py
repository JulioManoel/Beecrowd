pesos = []
danos = []

def rec(j, peso1, dano1):

  # if peso2 == -1:
  #   rec(j, peso1, dano1, pesos[j-1], danos[j-1])

  pesos.append(peso1 + pesos[j-1])
  danos.append(dano1 + danos[j-1])
  # rec()


test = int(input())
for i in range(test):
  numProjetos = int(input())

  for j in range(numProjetos):
    dano, peso = map(int, input().split())
    pesos.append(peso)
    danos.append(dano)
    if(j != 0): rec(j, peso, dano)

print(pesos)
