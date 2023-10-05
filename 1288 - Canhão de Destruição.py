pesos = []
danos = []

def rec(peso1, dano1, peso2 = -1, dano2 = -1):
  if peso2 == -1:

  


test = int(input())
for i in range(test):
  numProjetos = int(input())

  for j in range(numProjetos):
    dano, peso = map(int, input().split())
    pesos.append(peso)
    danos.append(dano)
    rec(peso, dano)

print(pesos)
